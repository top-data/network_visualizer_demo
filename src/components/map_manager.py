import folium
from folium import plugins
from typing import List, Dict
import streamlit as st
import ee

from src.data.sample_data import (
    PHYSICAL_NODES, PHYSICAL_LINKS,
    BGP_NODES, BGP_PATHS,
    DNS_NODES, DNS_LINKS,
    NTP_NODES, NTP_LINKS,
    AFFECTED_AREAS,
)

class MapManager:
    def __init__(self):
        # Extract Earth Engine credentials from Streamlit secrets
        service_account = st.secrets["service_account"]
        key_data = st.secrets["private_key"]

        # Initialize Google Earth Engine
        credentials = ee.ServiceAccountCredentials(service_account, key_data=key_data)
        ee.Initialize(credentials, project='ee-mhdsaki')

        self.sydney_coords = (-33.8688, 151.2093)  # Sydney coordinates
        self.status_colors = {
            'active': 'green',
            'warning': 'orange',
            'failed': 'red',
            'degraded': 'yellow'
        }

    def create_base_map(self) -> folium.Map:
        """Create the base map with satellite imagery."""
        m = folium.Map(
            location=self.sydney_coords,
            zoom_start=13,
            tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr='Google Satellite'
        )
        return m

    def _create_node_popup(self, node: Dict) -> str:
        """Create HTML popup content for a node."""
        return f"""
            <div style='font-family: Arial; font-size: 12px;'>
                <strong>{node['name']}</strong><br>
                Type: {node['type']}<br>
                Status: {node['status']}<br>
                ID: {node['id']}
            </div>
        """

    def _create_link_popup(self, link: Dict) -> str:
        """Create HTML popup content for a link."""
        return f"""
            <div style='font-family: Arial; font-size: 12px;'>
                <strong>Connection</strong><br>
                Type: {link['type']}<br>
                Status: {link['status']}<br>
                {f"Capacity: {link['capacity']}<br>" if 'capacity' in link else ''}
            </div>
        """

    def _add_nodes_and_links(
        self,
        m: folium.Map,
        nodes: List[Dict],
        links: List[Dict],
        layer_name: str,
        node_icon: str = 'info-sign',
    ):
        """Add nodes and links to the map in a feature group."""
        fg = folium.FeatureGroup(name=layer_name)

        # Add nodes
        for node in nodes:
            folium.Marker(
                location=[node['lat'], node['lon']],
                popup=folium.Popup(self._create_node_popup(node), max_width=300),
                icon=folium.Icon(
                    color=self.status_colors.get(node['status'], 'gray'),
                    icon=node_icon,
                    prefix='fa',
                ),
            ).add_to(fg)

        # Add links
        for link in links:
            source = next(n for n in nodes if n['id'] == link['source'])
            target = next(n for n in nodes if n['id'] == link['target'])
            points = [[source['lat'], source['lon']], [target['lat'], target['lon']]]
            folium.PolyLine(
                points,
                weight=3,
                color=self.status_colors.get(link['status'], 'gray'),
                popup=folium.Popup(self._create_link_popup(link), max_width=300),
                opacity=0.8,
            ).add_to(fg)

        fg.add_to(m)

    def add_physical_layer(self, m: folium.Map):
        """Add physical infrastructure layer."""
        self._add_nodes_and_links(m, PHYSICAL_NODES, PHYSICAL_LINKS, 'Physical Infrastructure', 'server')

    def add_routing_layer(self, m: folium.Map):
        """Add BGP routing layer."""
        self._add_nodes_and_links(m, BGP_NODES, BGP_PATHS, 'BGP Routing', 'random')

    def add_addressing_layer(self, m: folium.Map):
        """Add DNS infrastructure layer."""
        self._add_nodes_and_links(m, DNS_NODES, DNS_LINKS, 'DNS Infrastructure', 'database')

    def add_timing_layer(self, m: folium.Map):
        """Add NTP timing layer."""
        self._add_nodes_and_links(m, NTP_NODES, NTP_LINKS, 'NTP Timing', 'clock-o')

    def add_heatmap_layer(self, m: folium.Map):
        """Add heatmap of affected areas."""
        data = [[p['lat'], p['lon'], p['intensity']] for p in AFFECTED_AREAS]
        plugins.HeatMap(
            data,
            name='Affected Areas',
            min_opacity=0.4,
            max_zoom=18,
            radius=50,
            blur=30,
            gradient={0.4: 'blue', 0.65: 'yellow', 1: 'red'},
        ).add_to(m)

        if not any(isinstance(ctrl, folium.LayerControl) for ctrl in m._children.values()):
            folium.LayerControl().add_to(m)
