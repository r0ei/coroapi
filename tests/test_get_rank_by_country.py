from coroapi import Corona

instance = Corona()
highest_country_cases = instance.get_rank_by_country('usa', text=False)

print(highest_country_cases)

