from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in scn/__init__.py
from scn import __version__ as version

setup(
	name="scn",
	version=version,
	description="Simple payment management application",
	author="venkatesh",
	author_email="venkatesh112k@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
