#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:00:19 2018

@author: mh70
"""
import numpy as np
from  collections import namedtuple, Counter
import matplotlib.pyplot as plt


Compet = namedtuple('Compt',
                    'id diffic boulder speed pt_sum pt_mul pos_sum pos_mul')

num_comp = 30  #počet závodníků




def random_competetion(num_comp):
    diffic = np.random.permutation(np.arange(1, num_comp + 1))
    boulder = np.random.permutation(np.arange(1, num_comp + 1))
    speed = np.random.permutation(np.arange(1, num_comp + 1))
    
    
    pt_sum = diffic + boulder + speed # body sečteno podle pořadí
    pt_mul = diffic * boulder * speed # body vynásobeno podle pořadí
    
    pt_sum_srt = np.argsort(pt_sum) #setříděné indexy součtu bodů
    pt_mul_srt = np.argsort(pt_mul) #setříděné indexy součinu bodů
    
    compets = []    
    for i in range (num_comp):
        compet = Compet(i, diffic[i], boulder[i], speed[i],
                        pt_sum[i], pt_mul[i], 
                        #pořadí (1-based) podle součtu , podle součinu
                        np.where(pt_sum_srt == i)[0][0] + 1, 
                        np.where(pt_mul_srt == i)[0][0] + 1
                        )
        compets.append(compet)
    return compets 
    
  
num_simulations = 8000
arr_abs_diff_sum_mul = np.zeros(num_comp)
arr_pos_diff_sum_mul = np.zeros(num_comp)
arr_neg_diff_sum_mul = np.zeros(num_comp)
cnt = Counter()

for i in range(num_simulations ):
    compets = random_competetion(num_comp)
    # podle pořadí dle součinu bodů
    compets_pos_mul = sorted(compets, key= lambda x: x.pos_mul)
    # rozdíl v pořadí 
    diff_sum_mul = [c.pos_sum - c.pos_mul for c in compets_pos_mul]
    cnt_local = Counter(diff_sum_mul)
    cnt += cnt_local
    # absolutní rozdíl v pořadí
    abs_diff_sum_mul = [abs(c.pos_sum - c.pos_mul) for c in compets_pos_mul]
    arr_abs_diff_sum_mul += abs_diff_sum_mul
    
    # pozitivní rozdíl v pořadí
    pos_diff_sum_mul = [(c.pos_sum - c.pos_mul) 
    if (c.pos_sum - c.pos_mul) > 0 else 0  for c in compets_pos_mul]
    arr_pos_diff_sum_mul += pos_diff_sum_mul
    # negativní rozdíl v pořadí
    neg_diff_sum_mul = [(c.pos_sum - c.pos_mul) 
    if (c.pos_sum - c.pos_mul) < 0 else 0  for c in compets_pos_mul]
    arr_neg_diff_sum_mul += neg_diff_sum_mul

arr_abs_diff_sum_mul_avg  = arr_abs_diff_sum_mul / num_simulations
arr_pos_diff_sum_mul_avg  = arr_pos_diff_sum_mul / num_simulations   
arr_neg_diff_sum_mul_avg  = arr_neg_diff_sum_mul / num_simulations    
cnt_avg = {k: v/num_simulations for k, v in cnt.items()}



#plotting
plt.bar(cnt_avg.keys(), cnt_avg.values(), color='g')
plt.xlabel("součet dílčích umístění - součin dílčích umístění")
plt.ylabel("Průměrná četnost")
plt.title("četnost rozdílu pozic v celkovém umístění ")
plt.show()

x = np.arange(1, num_comp +1)
plt.plot(x, arr_abs_diff_sum_mul_avg, color="blue", linestyle='dashed', label="absolute")
plt.plot(x, arr_pos_diff_sum_mul_avg, color="green", label="positive")
plt.plot(x, arr_neg_diff_sum_mul_avg * (-1), color="red", label="negative")
plt.xlabel("Umístění")
plt.ylabel("Průměrný rozdíl pozic ")
plt.title("Vliv metodiky výpočtu bodování (součet vs součin) \n na umístění")
plt.xticks(np.arange(1, num_comp +4, step=5))
plt.legend()
plt.show()

"""
for c in compets_pos_mul:
    print(c)
"""


"""
compets_pos_mul = sorted(compets, key= lambda x: x.pos_mul)
print ("-----")    
    
#výpis podle rozdílu pořadí dle součtu - pořadí dle rozdílu
comptes_pos_sum_minus_mul = sorted(compets, key= lambda x: x.pos_sum - x.pos_mul)
for c in comptes_pos_sum_minus_mul:
    print(c)
"""