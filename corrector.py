#!/usr/bin/env python3
import sys

''' Levenshtein distance algorithm '''
def lev_distance(word_1, word_2):
    len1 = len(word_1)
    len2 = len(word_2)
    cost = 0
   
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
        
    cost = 0 if word_1[-1] == word_2[-1] else 1
    return min(
            lev_distance(word_1[:-1], word_2) + 1,
            lev_distance(word_1, word_2[:-1]) + 1,
            lev_distance(word_1[:-1], word_2[:-1]) + cost
            )
    
def save_original_text():
    if len(sys.argv) > 1:
        file_d = open(sys.argv[2])
        text = file_d.read()
        file_d.close() 
    else:
        file_d = sys.stdin
        text = file_d.read()
    
    return text
def save_dictionary():
    if len(sys.argv) > 1:
        file_d = open(sys.argv[2])
        text = file_d.read()
        file_d.close() 
    else:
        file_d = sys.stdin
        text = file_d.read()
    
    return text

def main():
    original = save_original_text()
    dictionary = save_dictionary()
    

if __name__=="__main__":
    main()


