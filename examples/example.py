# list of supported countries can be printed out | print(instance.countries)

import coroapi

instance = coroapi.Corona()
usa_infected_people = instance.get_country_infected('usa', text=False)
print(usa_infected_people)

israel_total_deathes = instance.get_country_deathes('israel', text=True)
print(israel_total_deathes)
