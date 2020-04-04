"""create a dictionary from lists"""
# Definition of countries and capitals
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create the dictionary europe
europe = {}
for country in countries:
    europe[country] = capitals[countries.index(country)]

print(europe)

eur1 = {country: capitals[countries.index(country)] for country in countries}
print(eur1)

eur2 = {countries[n]: capitals[n] for n in range(len(countries))}
print(eur2)

eur3 = {country:capital for country, capital in zip(countries, capitals)}
print(eur3)

print('all dicts are equal: ' +  str(europe == eur1 == eur2 == eur3))
