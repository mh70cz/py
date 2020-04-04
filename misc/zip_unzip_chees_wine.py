import random


'''http://montypython.wikia.com/wiki/Cheese_Shop_sketch

43 cheeses are mentioned
in the in the "Cheese Shop" sketch (from Monty Python's Flying Circus)
'''

cheeses_43 = (
    'Red Leicester',
    'Tilsit',
    'Caerphilly',
    'Bel Paese',
    'Red Windsor',
    'Stilton',
    'Emmental',
    'Gruyère',
    'Norwegian Jarlsberg',
    'Liptauer',
    'Lancashire',
    'White Stilton',
    'Danish Blue',
    'Double Gloucester',
    'Cheshire',
    'Dorset Blue Vinney',
    'Brie',
    'Roquefort',
    "Pont l'Evêque",
    'Port Salut',
    'Savoyard',
    'Saint-Paulin',
    "Carré de l'Est",
    'Bresse-Bleu',
    'Boursin',
    'Camembert',
    'Gouda',
    'Edam',
    'Caithness',
    'Smoked Austrian',
    'Japanese Sage Derby',
    'Wensleydale',
    'Greek Feta',
    'Gorgonzola',
    'Parmesan',
    'Mozzarella',
    'Pipo Crème',
    'Danish Fynbo',
    "Czech sheep's milk",
    'Venezuelan Beaver Cheese',
    'Cheddar',
    'Ilchester',
    'Limburger')

'''http://www.frenchscout.com/types-of-wines'''
red_wines = ("Syrah", "Merlot", "Cabernet sauvignon",
             "Malbec", "Pinot noir", "Zinfandel", "Sangiovese", "Barbera",)
white_wines = ("Chardonnay", "Sauvignon blanc", "Semillon", "Moscato",
               "Pinot grigio", "Gewürztraminer", "Riesling")

wines = red_wines + white_wines
cheeses = tuple(random.sample(cheeses_43, len(wines))) #terrible pairs BTW

cheese_wine_pairs = tuple(zip(wines, cheeses))  # zipped
uz_wines, uz_cheeses = zip(*cheese_wine_pairs) # unzipped


assert(wines == uz_wines)
assert(cheeses == uz_cheeses)
