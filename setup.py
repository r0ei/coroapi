from setuptools import setup, find_packages

with open('README.md', 'r') as f:
	long_description = f.read()
	
setup(
	name='coroapi',
	version='1.0',
	author='Roi Levi',
	author_email='roeil4939@gmail.com',
	description='coroapi is fast and up-to-date Covid-19 API',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/r0ei/coronavirus-api',
	packages=find_packages(),
	install_requires=[
          'requests',
          'beautifulsoup4',
	  'numpy',
      ]
)
