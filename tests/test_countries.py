from coroapi import Corona

instance = Corona()
supported_countries = instance.countries

print(supported_countries)
