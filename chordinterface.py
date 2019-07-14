#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time
import sys
from time import gmtime, strftime
import datetime
import os

RULE = {
    'major': [0, 4, 7],
    'sus4': [0, 5, 7],
    'sus2': [0, 2, 7],
    'minor': [0, 3, 7],
    '5': [0, 4],
    '7': [0, 4, 7, 10],
    'maj7': [0, 4, 7, 11],
    'm7': [0, 3, 7, 10],
    'add9': [0, 4, 7, 14]
}
BASICTYPE = ['major', 'minor', '5', '7', 'maj7', 'm7', 'add9', 'sus2', 'sus4']
CHORD = ['C', '#C', 'D', '#D', 'E', 'F', '#F', 'G', '#G', 'A', '#A', 'B']
CHORD_id = [i for i in range(len(CHORD))]
CHORDS = CHORD + CHORD + CHORD
LEVEL = [0, 2, 4, 5, 7, 9, 11]

RIGHR_ANSWER = ["本题答对，你很优秀哦～", "本题答对，是我的小可爱没错了～", "本题答对，胜不骄败不馁～", "本题答对，厉害了～",
                "本题答对，叉腰！", "本题答对，奖励白利利拥抱一个～", "本题答对，奖励椰子汁一袋～"]
WRONG_ANSWER = ["本题答错，嘤嘤嘤～", "本题答错，再接再厉！", "本题答错，谁还没个手误的时候呢～", "本题答错，加油加油加油～",
                "本题答错，胜不骄败不馁！", "本题答错，接受白利利夺命连环踢～", "本题答错，锅都是白利利的～", "本题答错，给小可爱买奶茶～"]

def output_and_input(TYPE):
    train_count = int(raw_input("本次想做几道题啊："))
    right_count = 0
    starttime = datetime.datetime.now()
    start = starttime.strftime('%Y-%m-%d %H:%M')
    for i in range(train_count):
        os.system('clear')
        print "从 " + start + " 开始答题，总共 " + str(train_count) + " 题，当前第 " + str(i + 1) + " 题，已答对 " + str(
            right_count) + " 题"
        chord_list = []
        level = random.choice(LEVEL)
        type = random.choice(TYPE)
        print CHORD[level] + ' ' + type
        answer = str(raw_input(strftime("%H:%M:%S", time.localtime(time.time())) + '\t' + "Your  answer is: "))
        rule = RULE[type]
        chord = ''
        for i in rule:
            chord = chord + ' ' + CHORDS[level + i]
            chord_list.append(str(CHORDS[level + i]))
        print strftime("%H:%M:%S", time.localtime(time.time())) + "\tRight answer is: " + chord.lstrip()
        if set(chord_list) == set(answer.upper().strip().split()):
            right_count += 1
            print random.choice(RIGHR_ANSWER)
        else:
            print random.choice(WRONG_ANSWER)
        answer = str(raw_input())

    endtime = datetime.datetime.now()
    seconds = (endtime - starttime).seconds
    minutes = seconds // 60
    second = seconds % 60
    timeStr = str(minutes) + '分钟' + str(second) + "秒"
    print("从 " + start + ' 开始答题，答题时间为：' + timeStr)
    print "总共\t" + str(train_count) + " 题，答对:\t" + str(right_count) + ' 题'


if __name__ == '__main__':
    TYPE = list(set(BASICTYPE).intersection(set(sys.argv)))
    if len(TYPE) == 0:
        print 'no chord type inputed!'
    result = output_and_input(TYPE)
