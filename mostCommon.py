import json
import csv
from collections import Counter
import pandas

data = pandas.read_csv("portugueseWords.csv", header=None)
j = 0
for each in data:
    print(data[0][j])
    j+=1

#forbidden_words = []

#print(forbidden_words)

with open('./data/output-backup.json', 'r', encoding='utf-8') as f:
    output_dict = json.load(f)

content = output_dict['articles']
i = 0
contentArray = ''

for each in content:    
    contentArray = output_dict['articles'][i]['content'] + contentArray
    i+=1

split_it = contentArray.lower().split()

for each in split_it:
    each.replace("'","")

Counter = Counter(split_it)

most_occur = Counter.most_common(200)

print(most_occur)
