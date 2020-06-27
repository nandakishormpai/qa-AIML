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

questions=["i need names of tools for gardening and hardware with a rating of 4 star rating where category is pet_supplies_toys",
   "search for all labels that sell shirts of brand Alisha and has stripes suitable for party where category is furniture_living_room ",
   "what are the companies that sell shirts where name Style Foot Bellies and has stripes suitable for party of Alisha WHERE CATEGORY IS asics_ge ",
   "list all the brands of baby products of good quality with a costs somewhere above 200 and where category is home_furnishing_bath_linen",
   "which all are the names of electronic items with great battery with a good discount higher than 500  where category is footwear_womens_footwear_ballerinas",
   "why dont you get all companies who sell watch and batteries in a price range between 200 and 600 where category is jewellery_pendants_lockets"]

for i,question in enumerate(questions):
    print(str(i+1)+")Response = %s" % my_bot.ask_question(question))
