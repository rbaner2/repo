# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:01:50 2020

@author: ritbaner
"""

#print('Hello World')
#print(2**3)
my_income = 2
#print (my_income)

str1 = "hello"
#print (str1[-6])
print('The value is:{}' .format(my_income))

def my_pig_latin(word):
    fl=word[0]
    rl=word[1:]
    vowel = ['a','e','i','o','u']
    if fl.lower() in  vowel:
        print ("Pig latin word is:" + word + 'ay')
    else:
        print ("Pig latin word is:" + rl + fl +'ay')

my_pig_latin('word')
my_pig_latin('apple')
