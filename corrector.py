#!/usr/bin/env python3
''' Levenshtein distance algorithm '''
import sys

def save_original_text():
    ''' Reads the text to correct from a file '''
    if len(sys.argv) > 1:
        file_d = open(sys.argv[2], "r")
        text = file_d.read()
        file_d.close()
    else:
        file_d = sys.stdin
        text = file_d.read()

    return text.rstrip("\n").split()

def save_dictionary():
    ''' Reads the dictionary from a file '''
    if len(sys.argv) > 1:
        file_d = open(sys.argv[1], "r")
        text = file_d.read()
        file_d.close()
    else:
        file_d = sys.stdin
        text = file_d.read()

    return text.rstrip("\n").split()

def put_correct_text(text):
    ''' Saves the correct text in a file '''
    if len(sys.argv) > 1:
        file_d = open(sys.argv[3], "w")
        file_d.write(text)
        file_d.close()
    else:
        print(text)

def put_editions(editions):
    ''' Saves the correct text in a file '''
    if len(sys.argv) > 1:
        file_d = open(sys.argv[4], "w")
        file_d.write(str(editions))
        file_d.close()
    else:
        print(editions)

def check_distances(original, corrected, dictionary, editions):
    ''' Iterates recursively through the words to correct '''
    corrected_words = corrected
    num_editions = editions
    for tocheck_word in original:
        minimum_distance = sys.maxsize
        for checking in dictionary:
            dist = lev_distance(tocheck_word, checking)
            if dist < minimum_distance:
                correct = checking
                minimum_distance = dist
        corrected_words = corrected_words+" "+correct
        num_editions = num_editions+minimum_distance
    return corrected_words, num_editions

def lev_distance(str1, str2):
    ''' Levenshtein distance algorithm '''
    dic = dict()
    for i in range(len(str1)+1):
        dic[i] = dict()
        dic[i][0] = i
    for i in range(len(str2)+1):
        dic[0][i] = i
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            dic[i][j] = min(dic[i][j-1]+1, dic[i-1][j]+1,
                            dic[i-1][j-1]+(not str1[i-1] == str2[j-1]))
    return dic[len(str1)][len(str2)]

def main():
    ''' Main function '''
    dictionary = save_dictionary()
    original = save_original_text()

    corrected_text, editions = check_distances(original, "", dictionary, 0)

    put_correct_text(corrected_text[1:])
    put_editions(editions)

if __name__ == "__main__":
    main()
