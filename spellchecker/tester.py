from collections import Counter
from string import ascii_lowercase as alphabet
import re

def words(text):
    return re.findall(r'\w+', text.lower())

allWords =words(open('big.txt').read())
totalWords = len(allWords)
wordSet = set(allWords)
w = Counter(allWords)

def P(word):
    return w[word] / totalWords

def edits1(word):
    new = set([])
    #first add letters in everywhere
    for i in range(0,len(word)+1,1):
        firsthalf = word[0:i]
        secondhalf = word[i:len(word)+1]
        for l in alphabet:
            new.add(firsthalf + l + secondhalf)
    #now with a letter removed or swapped
    for i in range(0,len(word)+1,1):
        firsthalf = word[0:i]
        middle = word[i:i+1]
        secondhalf = word[i + 1:len(word)+1]
        new.add(firsthalf + secondhalf)
        for l in alphabet:
            new.add(firsthalf + l + secondhalf)
    return new


def edits2(word):
    new = set([])
    #get first edits
    first = edits1(word)
    for w in first:
        new.update(edits1(w))
    return new

def realWord(word):
    return word in wordSet

def candidates(word):
    edit1 = edits1(word)
    edit2 = edits2(word)
    edited = edit1.union(edit2)
    return (edited & wordSet)

def correction(word):
    fix = ""
    cans = candidates(word)
    p = 0
    for c in cans:
        if P(c) > p:
            fix = c
            p = P(c)
    return fix

print(correction("reciet"))
print(correction("adres"))

