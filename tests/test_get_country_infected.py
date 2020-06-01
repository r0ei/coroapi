from coroapi import Corona

instance = Corona()
usa_infected_people = instance.get_country_infected('usa', text=False)

print(usa_infected_people)
