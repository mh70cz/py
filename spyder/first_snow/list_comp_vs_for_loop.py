#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 15:48:02 2018; @author: mh70
dictionary comprehension vs for loops
"""
import dis
import time
def cmp(cheeses):
    ''' use dictionary comprehension '''
    return [c.lower() for c in cheeses]

def flp(cheeses):
    ''' use for loop '''
    out_cheeses = list()
    for c in cheeses:
        out_cheeses.append(c.lower())
    return out_cheeses

print('cmp use dictionary comprehension:')
print(dis.dis(cmp))
print('\nflp use for loop:')
print(dis.dis(flp))

cheeses_43 = [
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
 'Limburger']

cheeses_43_cmp = cmp(cheeses_43)
cheeses_43_flp = flp(cheeses_43)    

assert (cheeses_43_cmp == cheeses_43_flp)

# compare the execution time (simple, inaccurate approach)
repetitions = 25000

start_time = int(round(time.time() * 1000))
for i in range(repetitions):
    cheeses_43_cmp = cmp(cheeses_43)
end_time = int(round(time.time() * 1000))
time_exec_cmp = end_time - start_time

start_time = int(round(time.time() * 1000))
for i in range(repetitions):
    cheeses_43_flp = flp(cheeses_43)
end_time = int(round(time.time() * 1000))
time_exec_flp = end_time - start_time

start_time = int(round(time.time() * 1000))
for i in range(repetitions):
    pass
end_time = int(round(time.time() * 1000))
time_exec_pass = end_time - start_time

print ("\n\ncompare the execution time (simple, inaccurate approach)")
print ("Use dictionary comprehension: " + str(time_exec_cmp - time_exec_pass))
print ("Use for loop:                 " + str(time_exec_flp - time_exec_pass))