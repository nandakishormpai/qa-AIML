#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jun 28 Sun
@author: nandakishormpai2001
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
   "what are the companies that sell shirts where name Style Foot Bellies and has stripes suitable for party of Alisha where category is asics_ge ",
   "list all the brands of baby products of good quality with a costs somewhere above 200 and where category is home_furnishing_bath_linen",
   "which all are the names of electronic items with great battery with a good discount higher than 500  where category is footwear_womens_footwear_ballerinas",
   "why dont you get all companies who sell watch and batteries in a price range between 200 and 600 where category is jewellery_pendants_lockets",
   "Please show me the names of food items of Alisha and costs below 400 where category is newgen_tech_e ",
   "i need some brands that sell clothes for men that have a rating of 5 and discount above 300 where category is pet_supplies_toys ",
   "what are the ratings of clothes suitable for sports and athletics of Kennel whose price ranges between 300 and 600 where category is asics_ge ",
   "which are the companies that sell good furnitures with rating near 3 and having a discount between 500 and 700 where category is home_furnishing_bath_linen",
   "Please show me the names of food items that costs below 400 of Alisha where category is newgen_tech_e ",
   "i need some brands that sell clothes for men that have a discount above 300  rating of 5 where category is pet_supplies_toys ",
   "what are the ratings of clothes suitable for sports and athletics in a price ranges between 300 and 600 of Kennel where category is asics_ge",
   "which are the companies that sell good furnitures with a discount between 500 and 700 with rating near 3 where category is home_furnishing_bath_linen"]

for i,question in enumerate(questions):
    print(str(i+1)+")Response = %s" % my_bot.ask_question(question))
