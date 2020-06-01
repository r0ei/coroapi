from coroapi import Corona

instance = Corona()

israel_total_deathes = instance.get_country_deaths('israel', text=True)
print(israel_total_deathes)
