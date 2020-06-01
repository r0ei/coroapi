from coroapi import Corona

instance = Corona()
usa_recovered_people = instance.get_country_recovered('usa', text=True)

print(usa_recovered_people)
