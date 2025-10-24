"""Sample data for network visualization layers."""

# Sydney CBD area coordinates for random point generation
SYDNEY_BOUNDS = {
    'north': -33.8568,
    'south': -33.8888,
    'east': 151.2293,
    'west': 151.1893
}

# Physical Layer Data
PHYSICAL_NODES = [
    {'id': 'dc1', 'name': 'Data Center 1', 'type': 'datacenter', 'lat': -33.8688, 'lon': 151.2093, 'status': 'active'},
    {'id': 'dc2', 'name': 'Data Center 2', 'type': 'datacenter', 'lat': -33.8788, 'lon': 151.2193, 'status': 'active'},
    {'id': 'pop1', 'name': 'PoP Sydney CBD', 'type': 'pop', 'lat': -33.8588, 'lon': 151.2153, 'status': 'warning'},
    {'id': 'pop2', 'name': 'PoP Pyrmont', 'type': 'pop', 'lat': -33.8708, 'lon': 151.1953, 'status': 'failed'},
]

PHYSICAL_LINKS = [
    {'source': 'dc1', 'target': 'pop1', 'type': 'fiber', 'capacity': '100G', 'status': 'active'},
    {'source': 'dc2', 'target': 'pop1', 'type': 'fiber', 'capacity': '100G', 'status': 'active'},
    {'source': 'pop1', 'target': 'pop2', 'type': 'fiber', 'capacity': '100G', 'status': 'degraded'},
]

# BGP Routing Layer Data
BGP_NODES = [
    {'id': 'as1', 'name': 'AS 1001', 'type': 'transit', 'lat': -33.8688, 'lon': 151.2093, 'status': 'active'},
    {'id': 'as2', 'name': 'AS 1002', 'type': 'transit', 'lat': -33.8788, 'lon': 151.2193, 'status': 'active'},
    {'id': 'as3', 'name': 'AS 1003', 'type': 'edge', 'lat': -33.8588, 'lon': 151.2153, 'status': 'failed'},
]

BGP_PATHS = [
    {'source': 'as1', 'target': 'as2', 'type': 'peer', 'prefixes': 1000, 'status': 'active'},
    {'source': 'as2', 'target': 'as3', 'type': 'customer', 'prefixes': 500, 'status': 'failed'},
]

# DNS Layer Data
DNS_NODES = [
    {'id': 'ns1', 'name': 'NS1 Sydney', 'type': 'authoritative', 'lat': -33.8688, 'lon': 151.2093, 'status': 'active'},
    {'id': 'ns2', 'name': 'NS2 Sydney', 'type': 'authoritative', 'lat': -33.8788, 'lon': 151.2193, 'status': 'active'},
    {'id': 'resolver1', 'name': 'Resolver CBD', 'type': 'resolver', 'lat': -33.8588, 'lon': 151.2153, 'status': 'warning'},
]

DNS_LINKS = [
    {'source': 'ns1', 'target': 'ns2', 'type': 'zone_transfer', 'status': 'active'},
    {'source': 'resolver1', 'target': 'ns1', 'type': 'query', 'status': 'active'},
]

# NTP Layer Data
NTP_NODES = [
    {'id': 'ntp1', 'name': 'Stratum 1 Sydney', 'type': 'stratum1', 'lat': -33.8688, 'lon': 151.2093, 'status': 'active'},
    {'id': 'ntp2', 'name': 'Stratum 2 CBD', 'type': 'stratum2', 'lat': -33.8788, 'lon': 151.2193, 'status': 'active'},
    {'id': 'ntp3', 'name': 'Stratum 2 Pyrmont', 'type': 'stratum2', 'lat': -33.8588, 'lon': 151.2153, 'status': 'failed'},
]

NTP_LINKS = [
    {'source': 'ntp2', 'target': 'ntp1', 'type': 'sync', 'stratum': 1, 'status': 'active'},
    {'source': 'ntp3', 'target': 'ntp1', 'type': 'sync', 'stratum': 1, 'status': 'failed'},
]

# Affected Areas Data (for heatmap)
AFFECTED_AREAS = [
    {'lat': -33.8708, 'lon': 151.1953, 'intensity': 0.9},  # High impact around failed PoP
    {'lat': -33.8588, 'lon': 151.2153, 'intensity': 0.5},  # Medium impact around warning PoP
]