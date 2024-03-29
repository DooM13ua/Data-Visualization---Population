# from pygal.maps.world import COUNTRIES
#
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

from pygal.maps.world import COUNTRIES
from country_codes import get_country_code


def find_missing_countries():
    """Find and return a list of countries missing codes."""
    missing_countries = []
    for country_name in COUNTRIES.values():
        if get_country_code(country_name) is None:
            missing_countries.append(country_name)
    return missing_countries


missing_countries = find_missing_countries()
print("Countries missing codes or not on the map:")
for country in missing_countries:
    print(country)