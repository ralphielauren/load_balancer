import os
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()


setup(
    name="loadbalancer",
    version="1.0",
    description="Testing creating a load balancer",
    author="Lia Tasoudi",
    author_email="liatasoudi@gmail.com",
    install_requires=install_requires,
    packages=find_packages(),
    data_files=[os.path.join("configs", "loadbalancer.yaml")],
    include_package_data=True,
    python_requires=">=3.8",
)
