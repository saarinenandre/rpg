# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:53:08 2019

@author: andre
"""
import random

places1 = ["lake","pond","city","field","woods","swamp","wetlands",'laboratory','power plant','a beach','a tower','a hospital']

places2 = ["house","barn","hut","garage","sauna","camp","caravan",'computer room','school','a shopping mall','a train station']

items = ["nothing", "a stick","a spoon","a leaf", "water","a snail","a mug","a shoe","medipack",'landmine','bear trap','a mouse','a beard','a cable','a speaker','a book','a brick']

enemy = ['wolf','bear','ålänning','guy from Geta','fish','robot','dog','angry human','spider','snail','bird','manbearpig','sysadmin']

class Person:
    
    def __init__(self,hp,attack):
        self.hp = hp
        self.attack = attack
        
    def getInfo(self):
        print('Stats:\nHP:',self.hp,'\nAttack:',self.attack)

class Player(Person):
    def __init__(self, hp, attack, name):
        Person.__init__(self,hp,attack)
        self.name = name
        self.alive = True
    
    def getInfo(self):
        print('Name:',self.name)
        super().getInfo()
        
char = Player(10,100,'Gubb')

while char.alive:
    choose = int(input('What to do?\n1: Show stats\n2: Go left\n3: Go right\n4: Kill player\n>'))
    
    if choose==1:
        char.getInfo()
        
    elif choose==2:
        print('You went left')
        
    elif choose==3:
        print('You went right')
        
    elif choose==4:
        char.alive = False
        
print('You died. Game over')