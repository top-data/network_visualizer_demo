# Network Infrastructure Visualizer

A Streamlit-based application for visualizing and monitoring network infrastructure in Sydney, featuring multiple layers of network information and failure analysis.

## Features

- High-resolution satellite base map using Google Earth Engine
- Multiple visualization layers:
  - Physical infrastructure layer
  - BGP routing layer
  - DNS infrastructure layer
  - NTP timing layer
- Failure detection and analysis
- Impact visualization with heatmaps
- Recovery recommendations

## Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd network_visualizer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Google Earth Engine authentication:
```bash
earthengine authenticate
```

5. Run the application:
```bash
streamlit run src/app.py
```

## Project Structure

```
network_visualizer/
├── src/
│   ├── app.py                    # Main Streamlit application
│   ├── components/
│   │   ├── map_manager.py        # Map visualization management
│   │   ├── knowledge_graph.py    # Network knowledge graph components
│   │   ├── failure_analyzer.py   # Failure detection and analysis
│   │   └── recovery_recommender.py # Recovery recommendations
│   ├── data/                     # Data storage
│   └── utils/                    # Utility functions
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Dependencies

- Streamlit
- Folium
- NetworkX
- Google Earth Engine
- RDFLib
- Scikit-learn
- Plotly
- NumPy
- Pandas