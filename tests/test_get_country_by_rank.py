from coroapi import Corona

instance = Corona()
country_by_rank = instance.get_country_by_rank('4', text=False)

print(country_by_rank)
