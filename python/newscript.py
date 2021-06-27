#!/bin/python3

import sys # system functions and parameters
from datetime import datetime as dt #import with alias

print(sys.version)

print(dt.now())

my_name = "Nick"

print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

another_quote = "He said, \"hello!\""

too_much_space = "                          hello                        "
print(too_much_space.strip())

print("A" in "Apple")
print("A" in "apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())

movie = "The Hangover"
print("My favorite movie is {}".format(movie))
print(f"My favorite movie is {movie}")

### Dictionaries - key/value pairs {}

drink = {"White Russian":7, "Old Fashion":8} #drink is key, price is value
print(drink)

employees = {"Fineance":["Bob","Linda"], "IT": ["Gene", "Bill"], "HR": ["Shit", "shitter"]}
print(employees)

employees['Legal'] = ["mr.fronz"]
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drink["White Russian"] = 8
print(drink)

print(drink.get("White Russian"))


