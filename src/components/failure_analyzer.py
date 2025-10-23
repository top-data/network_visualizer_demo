from typing import List, Dict
from sklearn.ensemble import IsolationForest
import numpy as np
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.data.sample_data import (
    PHYSICAL_NODES, PHYSICAL_LINKS,
    BGP_NODES, BGP_PATHS,
    DNS_NODES, DNS_LINKS,
    NTP_NODES, NTP_LINKS,
    AFFECTED_AREAS
)

class FailureAnalyzer:
    def __init__(self):
        self.anomaly_detector = IsolationForest(contamination=0.1)
        
    def analyze_metrics(self, metrics: Dict) -> List[Dict]:
        """Analyze network metrics for anomalies."""
        # This is a placeholder - implement actual anomaly detection
        return []
    
    def get_current_failures(self) -> List[Dict]:
        """Get current system failures and their details."""
        failures = []
        
        # Check physical layer
        for node in PHYSICAL_NODES:
            if node['status'] == 'failed':
                failures.append({
                    'id': node['id'],
                    'name': node['name'],
                    'type': 'Physical Node',
                    'description': f"Physical node {node['name']} is down",
                    'severity': 'high'
                })
            elif node['status'] == 'warning':
                failures.append({
                    'id': node['id'],
                    'name': node['name'],
                    'type': 'Physical Node',
                    'description': f"Physical node {node['name']} is showing warning signs",
                    'severity': 'medium'
                })
        
        for link in PHYSICAL_LINKS:
            if link['status'] == 'failed':
                failures.append({
                    'id': f"{link['source']}-{link['target']}",
                    'type': 'Physical Link',
                    'description': f"Connection between {link['source']} and {link['target']} is down",
                    'severity': 'high'
                })
            elif link['status'] == 'degraded':
                failures.append({
                    'id': f"{link['source']}-{link['target']}",
                    'type': 'Physical Link',
                    'description': f"Connection between {link['source']} and {link['target']} is degraded",
                    'severity': 'medium'
                })
        
        # Check BGP layer
        for node in BGP_NODES:
            if node['status'] == 'failed':
                failures.append({
                    'id': node['id'],
                    'name': node['name'],
                    'type': 'BGP Node',
                    'description': f"BGP node {node['name']} is not responding",
                    'severity': 'high'
                })
        
        for path in BGP_PATHS:
            if path['status'] == 'failed':
                failures.append({
                    'id': f"{path['source']}-{path['target']}",
                    'type': 'BGP Path',
                    'description': f"BGP peering between {path['source']} and {path['target']} is down",
                    'severity': 'high'
                })
        
        # Check DNS layer
        for node in DNS_NODES:
            if node['status'] == 'failed':
                failures.append({
                    'id': node['id'],
                    'name': node['name'],
                    'type': 'DNS Node',
                    'description': f"DNS server {node['name']} is not responding",
                    'severity': 'high'
                })
            elif node['status'] == 'warning':
                failures.append({
                    'id': node['id'],
                    'name': node['name'],
                    'type': 'DNS Node',
                    'description': f"DNS server {node['name']} is experiencing issues",
                    'severity': 'medium'
                })
        
        # Check NTP layer
        for node in NTP_NODES:
            if node['status'] == 'failed':
                failures.append({
                    'id': node['id'],
                    'name': node['name'],
                    'type': 'NTP Node',
                    'description': f"NTP server {node['name']} is not responding",
                    'severity': 'high'
                })
        
        return failures
    
    def get_affected_areas(self) -> List[Dict]:
        """Get geographical areas affected by failures."""
        return AFFECTED_AREAS
    
    def calculate_impact_severity(self, failure: Dict) -> float:
        """Calculate the severity of a failure's impact."""
        severity_scores = {
            'high': 1.0,
            'medium': 0.6,
            'low': 0.3
        }
        return severity_scores.get(failure.get('severity', 'low'), 0.3)