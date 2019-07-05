#!/usr/bin/python
import random
import time
import sys

RULE={
        'major' : [ 0, 4, 7 ],
        'sus4' : [ 0, 5, 7 ],
        'sus2' : [ 0, 2, 7 ],
        'minor' : [ 0, 3, 7 ],
        '5' : [ 0, 4 ],
        '7' : [ 0, 4, 7, 10 ],
        'maj7' : [ 0, 4, 7, 11 ],
        'm7' : [ 0, 3, 7, 10 ],
        'add9' : [ 0, 4, 7, 14 ]
}
BASICTYPE=['major', 'minor', '5' ,'7', 'maj7', 'm7', 'add9', 'sus2', 'sus4']
TYPE=list(set(BASICTYPE).intersection(set(sys.argv)))


if len(TYPE)==0:
    print 'no chord type inputed!'

CHORD=['C','#C','D','#D','E','F','#F','G','#G','A','#A','B']
CHORDS = CHORD + CHORD + CHORD
LEVEL=[0,2,4,5,7,9,11]

while True:
    level = random.choice(LEVEL)
    type = random.choice(TYPE)
    print CHORD[level]+type
    time.sleep(5)
    rule=RULE[type]
    chord=''
    for i in rule:
        chord=chord+' ' + CHORDS[level + i] 
    print chord.lstrip()
        

