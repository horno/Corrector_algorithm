#!/usr/bin/env python3

import sys

def save_original_text():
    if len(sys.argv) > 1:
        file_d = open(sys.argv[2], "r")
        text = file_d.read()
        file_d.close() 
    else:
        file_d = sys.stdin
        text = file_d.read()
    
    return text.rstrip("\n").split()

def save_dictionary():
    if len(sys.argv) > 1:
        file_d = open(sys.argv[1], "r")
        text = file_d.read()
        file_d.close() 
    else:
        file_d = sys.stdin
        text = file_d.read()
    
    return text.rstrip("\n").split()

def put_correct_text(text):
    if len(sys.argv) > 1:
        file_d = open(sys.argv[3], "w")
        file_d.write(text)
        file_d.close()
    else:
        print(text)

def put_editions(editions):
    if len(sys.argv) > 1:
        file_d = open(sys.argv[4], "w")
        file_d.write(str(editions))
        file_d.close()
    else:
        print(editions)

def check_distances(original, corrected, dictionary, editions):
    for tocheck_word in original:
        minimum_distance=sys.maxsize
        for checking in dictionary:
            dist = lev_distance(tocheck_word, checking)
            if dist<minimum_distance:
                correct=checking
                minimum_distance=dist
        corrected=corrected+" "+correct
        editions=editions+dist   
    return corrected, editions

def lev_distance(str1, str2):
    d=dict()
    for i in range(len(str1)+1):
        d[i]=dict()
        d[i][0]=i
    for i in range(len(str2)+1):
        d[0][i] = i
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
    return d[len(str1)][len(str2)]

def main():
    dictionary = save_dictionary()
    original = save_original_text() 

    corrected_text, editions = check_distances(original, "", dictionary, 0)
    
    put_correct_text(corrected_text)
    put_editions(editions)

if __name__=="__main__":
    main()