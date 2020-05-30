   # Covid-19 Tracker API :microbe:

Provides up-to-date data about Coronavirus outbreak. Includes numbers about confirmed cases, deaths and recovered.

## Available data-sources:
Currently only 1 data-source is available to retrieve the data:

- [Epidemic Stats](https://epidemic-stats.com/coronavirus/) - **All statistics data about coronavirus COVID-19 comes from World Health Organization and Johns Hopkins CSSE. Charts includes number of infected, deaths and recovered.**

## How it works

*The module emulates the browser actions by sending requests to the site server. The module doesn't load any type of files while sending requests to the site and that makes it faster. The module is scraping the website source code, and returning the final result.*

## Features

- Provides Fast, and Up-to-Date data about the Coronavirus outbreak
- Can output with text or not
- A lot of supported countries (up to 100)

## Installation
- `pip install coroapi`
1. Make sure you have [python3 installed and on your PATH](https://docs.python-guide.org/starting/installation/)

## Simple Usage

```python
# All results is right to today (5/30/2020)
# list of supported countries can be printed out | print(instance.countries)

import coroapi

instance = Corona()
usa_infected_people = instance.get_country_infected('usa', text=False)
print(usa_infected_people)

<< 1802086

israel_total_deathes = instance.get_country_deathes('israel', text=True)
print(israel_total_deathes)

<< Deaths: 284
```

> if there's any problem, please let me know - roeil4939@gmail.com
