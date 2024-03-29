import json
from country_codes import get_country_code
import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal.maps.world import COUNTRIES

# Load the data into a list
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')


all_country_codes = set(COUNTRIES.keys())  # Отримати всі можливі коди країн
countries_on_map = set(cc_populations.keys())  # Отримати коди країн, які відображаються на карті

# Отримати коди країн, які не відображаються на карті
missing_countries = all_country_codes - countries_on_map

print("Countries not on the map:")
for country_code in missing_countries:
    country_name = COUNTRIES.get(country_code)
    print(f"{country_name} : ({country_code})")