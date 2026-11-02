from setuptools import find_packages, setup

setup(
    name="simple_inventory_enhanced",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"custom_components.simple_inventory_enhanced": ["translations/*.json"]},
)
