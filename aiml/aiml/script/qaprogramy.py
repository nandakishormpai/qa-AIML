#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:27:13 2020

@author: abhijithneilabraham
"""

from programy.clients.embed.basic import EmbeddedDataFileBot
import os

#filepath = os.path.dirname(__file__) + os.sep
filepath =os.path.split(os.path.realpath(__file__))[0]

files = {'aiml': [filepath+'/aiml/'],
         'sets':[filepath+'/sets/'],
         'maps':[filepath+'/maps/'],
          }
print("filepath=",filepath,files['aiml'])

my_bot =EmbeddedDataFileBot(files,defaults=True)

questions=["i need names of tools for gardening and hardware with a 4 star rating where category is pet_supplies_toys",
   "search for all labels that sell shirts of brand Alisha and has stripes suitable for party where category is pet_supplies_toys ",
   "what are the companies that sell shirts where name Style Foot Bellies and has stripes suitable for party of Alisha WHERE CATEGORY IS pet_supplies_toys "]

for i,question in enumerate(questions):
    print(str(i+1)+")Response = %s" % my_bot.ask_question(question))
