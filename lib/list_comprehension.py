#!/usr/bin/env python3

def return_evens(num_list):
    lst2 = list()
    for n in range(len(num_list)):
        if num_list[n] % 2 == 0:
            lst2.append(num_list[n])
    
    return lst2
    pass

def make_exclamation(sentence_list):
    lst2 = list()
    exPoint = "!"
    for n in range(len(sentence_list)):
        sentence_list[n] += exPoint
        lst2.append(sentence_list[n])
    return lst2
    pass