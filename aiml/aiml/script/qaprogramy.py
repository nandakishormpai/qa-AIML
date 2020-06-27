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

questions=["get all rating of SWAGGA Women Clogs by dongli thing,WHERE CATEGORY IS pet_supplies_toys",
   "how many Expatriate ladies between age 40 and 44 have Stomach Cancer in year 2011",
   "how many National between age 40 and 44 have Breast Cancer in year 2013",
   "Which is the type of cancer that cause the death of men below age 40",
   "What all are the type of cancer that cause death in year 2016",
   "how many men with Oesophagus cancer died in year 2018",
   "how many women with Colorectum  cancer died in year 2011",
   "how many women with Oesophagus cancer died in year 2013",
   "how many national men with Oesophagus cancer died in year 2018",
   "how many expatriate men with Oesophagus cancer died in year 2018"]

for i,question in enumerate(questions):
    print(str(i+1)+")Response = %s" % my_bot.ask_question(question))
