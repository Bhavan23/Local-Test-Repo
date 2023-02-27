from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in local_test_app/__init__.py
from local_test_app import __version__ as version

setup(
	name="local_test_app",
	version=version,
	description="Development Testing App",
	author="Bhavansathru",
	author_email="bhavan@aerele.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
