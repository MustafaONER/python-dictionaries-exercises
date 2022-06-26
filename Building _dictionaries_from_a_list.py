#1. Building Dictionaries from a List
#The code below contains a list of words. Build a dictionary that contains all these words as keys, and their quantities as values. Print the words with their quantities.


wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]

fruits={}
for fruit in wordlist:
    fruits[fruit]= wordlist.count(fruit)
    
print( fruits)
