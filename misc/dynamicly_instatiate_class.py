# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:06:34 2017

@author: m.houska
"""
class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

class Player:
    def __init__(self,name):
        self._name = name
        
#player_names = ["franta", "pepa", "honza", "karel"]
#player_insts = dict()
#
#for idx, p in enumerate(player_names):
#    inst_of_player = Player(str.capitalize(player_names[idx]))
#    player_insts[p] = inst_of_player


player_names = ["stepan", "pepa", "jan", "karel", "jana"]    
def inst_player_class(player_names):
    player_insts = dict()
    for idx, p in enumerate(player_names):
        inst_of_player = Player(str.capitalize(player_names[idx]))
        player_insts[p] = inst_of_player
    return player_insts

player_insts = inst_player_class(player_names)