#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import main_script as sc

run = True
menu = "Press 1 for problem 1 output\nPress 2 for problem 2 output\nPress 3 for problem 3 output\nPress 4 to exit!"

news_obj = sc.NewsAnalyzer()
while(run):
    print (menu)
    a = input()
    a = int(a)
    if a == 1:
        t1 = input("Enter timestamp 1:")
        t2 = input("Enter timestamp 2:")
        print (news_obj.prob1(float(t1),float(t2)))
    elif a ==2:
        print (news_obj.prob2())
    elif a == 3:
        n = input("Enter the number n:")
        print (news_obj.prob3(int(n)))
    elif a == 4:
        run = False
    else:
        print ("Invalid Input")
