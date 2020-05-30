from distutils.core import setup
setup(
  name = 'coroapi',
  packages = ['coroapi'],
  version = '1.00',
  license='MIT',
  description = 'Fast, and Up-to-Date Corona Virus API with up to 100 supported countries',
  author = 'Roi Levi',
  author_email = 'roeil4939@gmail.com',
  url = 'https://github.com/r0eilevi/coronavirus-api',
  download_url = 'https://github.com/r0eilevi/coronavirus-api/archive/v1.00.tar.gz', # change this
  keywords = ['api', 'corona', 'virus', 'fast', 'covid19', 'up-to-date'],
  install_requires=[
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
