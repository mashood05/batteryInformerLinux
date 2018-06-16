#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:06:20 2018

@author: mashood
"""

import subprocess
import pyttsx3 as pyttsx
import time

while True:

    result = subprocess.check_output(['acpi'])
    string = str(result).capitalize()
    ss=string.split(' ')

    bettery_persentatge_low = "30"

    bettery_persentatge_high = "95"

    bettery_charging_persentage = str(ss[3]).replace(",","")
    bettery_charging_persentage = bettery_charging_persentage[:3]
    print("i am working",bettery_charging_persentage[:3])

    ## clean sextion
    clean_low_persentage = bettery_persentatge_low.replace("%","")
    clean_high_persentage = bettery_persentatge_high.replace("%","")
    clean_charging_persentage = int(bettery_charging_persentage.replace("%",""))


    ## converting section

    bettery_persentatge_low = int(clean_low_persentage)

    bettery_persentatge_high = int(clean_high_persentage)

    bettery_charging_persentage = clean_charging_persentage


    if "charging,"  == ss[2] and bettery_charging_persentage == bettery_persentatge_high:

        engine = pyttsx.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', "english+f4")

        engine.say('Bettery Full')
        engine.runAndWait()



    if "discharging,"  == ss[2] and bettery_charging_persentage == bettery_persentatge_low :
        
        engine = pyttsx.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', "english+f4")
        engine.say('Bettery Low. ')
        engine.runAndWait()

    time.sleep(60)

print("i am working",bettery_charging_persentage)

