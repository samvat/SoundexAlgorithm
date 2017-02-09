# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 01:04:56 2017

@author: Samvat
"""
input_string = input("String: ")
sounds = {"bfpv": "1", "cgjkqsxz":"2", "dt":"3", "l":"4", "mn":"5", "r":"6", "aeiuohwy":""}
soundcode = ""
soundcode += input_string[0].upper()

for char in input_string[1:]:
    for key in sounds.keys():
        if char in key:
            if sounds[key]!=soundcode[-1]:
                soundcode+=sounds[key]

soundcode = soundcode[:4].ljust(4,"0")
print(soundcode)