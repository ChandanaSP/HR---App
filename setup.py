from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ts_hr/__init__.py
from ts_hr import __version__ as version

setup(
	name="ts_hr",
	version=version,
	description="Ts Hr",
	author="Ts Hr",
	author_email="ts_hr@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
