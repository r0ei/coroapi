from setuptools import setup, find_packages

with open('README.md', 'r') as f:
	long_description = f.read()
	
setup(
	name='coroapi',
	version='1.03',
	author='Roi Levi',
	author_email='roeil4939@gmail.com',
	description='coroapi Is fast and up-to-date corona virus news in the world, support up to 100 countries',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/r0eilevi/coronavirus-api',
	packages=find_packages(),
	install_requires=[
          'requests',
          'beautifulsoup4',
      ]
)
