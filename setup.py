from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='GOSTRocks',
    packages=['GOSTRocks'],
    install_requires=[
        'rasterio',
        'geopandas',
        'pandas',
        'numpy',
        'scikit-image',
        'pyproj',
        'ogr',
        'rtree',
    ],
    extras_require = {
        'osm':  ["GOSTNets", "osmnx", "networkx"],
        'xrio': ["xarray", "rioxarray"],
        'graphs' : ["seaborn"]
    },
    version='0.0.2',
    description='Miscellaneous geospatial functions concerning vector, raster, and network analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bpstewar/gostrocks",    
    author='Benjamin P. Stewart',
    license='MIT',    
    package_dir= {'':'src'}
)