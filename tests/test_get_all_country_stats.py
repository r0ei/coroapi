from coroapi import Corona

instance = Corona()
all_country_stats = instance.get_all_country_stats('usa', text=False)

print(all_country_stats)
