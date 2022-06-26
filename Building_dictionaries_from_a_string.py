#2. Building Dictionaries from a String
#The code block below contains a string that is a list of words, separated by commas. Build a dictionary that contains all these words as keys, and how often they occur as values. Then print the words with their quantities.

text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

list=text.split(',')
fruits={}
for fruit in list:
    fruits[fruit]= list.count(fruit)
    
print( fruits)
