travel_log = [
    {
        'country': 'Zimbabwe',
        'visits': '12',
        'cities': ['Harare', 'Mutare', 'Bulawayo']
    },
    {
        'country': 'South Africa',
        'visits': '5',
        'cities': ['Cape Town', 'Pretoria', 'Johannesburg']
    },
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {'country': country_visited, 'visits': times_visited, 'cities': cities_visited}
    travel_log.append(new_country)


add_new_country('France', 12, ['Paris', 'Lille', 'Dijon'])
print(travel_log)
