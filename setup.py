from setuptools import setup, find_packages

setup(
    name="network_visualizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'folium',
        'networkx',
        'geopy',
        'pandas',
        'numpy',
        'earthengine-api',
        'google-cloud-storage',
        'rdflib',
        'plotly',
        'scikit-learn'
    ],
)