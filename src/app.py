import streamlit as st
import folium
from streamlit_folium import folium_static
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.components.map_manager import MapManager
from components.knowledge_graph import (
    PhysicalLayerGraph,
    RoutingLayerGraph,
    AddressingLayerGraph,
    TimeSyncLayerGraph
)
from components.failure_analyzer import FailureAnalyzer
from components.recovery_recommender import RecoveryRecommender

def main():
    st.set_page_config(page_title="Network Visualizer", layout="wide")
    st.title("Network Infrastructure Visualizer")

    # Initialize components
    map_manager = MapManager()
    failure_analyzer = FailureAnalyzer()
    recovery_recommender = RecoveryRecommender()

    # Sidebar controls
    st.sidebar.title("Layer Controls")
    show_physical = st.sidebar.checkbox("Physical Layer", True)
    show_routing = st.sidebar.checkbox("Routing Layer (BGP)")
    show_addressing = st.sidebar.checkbox("Addressing Layer (DNS)")
    show_timing = st.sidebar.checkbox("Time Sync Layer (NTP)")
    show_heatmap = st.sidebar.checkbox("Show Affected Areas")

    # Main map view
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.subheader("Network Infrastructure Map")
        m = map_manager.create_base_map()
        
        # Add selected layers
        if show_physical:
            map_manager.add_physical_layer(m)
        if show_routing:
            map_manager.add_routing_layer(m)
        if show_addressing:
            map_manager.add_addressing_layer(m)
        if show_timing:
            map_manager.add_timing_layer(m)
        if show_heatmap:
            map_manager.add_heatmap_layer(m)
            
        folium_static(m)

    # Side panel for failures and recommendations
    with col2:
        st.subheader("System Status")
        failures = failure_analyzer.get_current_failures()
        if failures:
            st.error("Detected Issues:")
            for failure in failures:
                st.write(f"- {failure['description']}")
            
            st.subheader("Recovery Recommendations")
            recommendations = recovery_recommender.get_recommendations(failures)
            for rec in recommendations:
                st.info(rec)
        else:
            st.success("All systems operational")

if __name__ == "__main__":
    main()