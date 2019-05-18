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

''' Levenshtein distance algorithm '''
def lev_distance(word_1, word_2, min_dist, editions = 0):
    len1 = len(word_1)
    len2 = len(word_2)
    cost = 0
   
    if len1 == 0:
        return len2 + editions
    if len2 == 0:
        return len1 + editions
    if editions >= min_dist:
        return min_dist

    cost = 0 if word_1[-1] == word_2[-1] else 1
    
    case_1 = lev_distance(word_1[:-1], word_2, min_dist, editions + 1)
    case_2 = lev_distance(word_1, word_2[:-1], min_dist, editions + 1)
    case_3 = lev_distance(word_1[:-1], word_2[:-1], min_dist, editions + cost)
    return min(case_1, case_2, case_3)




def check_distances(original, corrected, dictionary, editions): 
    if not original:
        return corrected, editions
    correct_word, distance = compare_with_dict(original[0], dictionary, "", sys.maxsize)#TODO Canviar per màxim
    return check_distances(original[1:], corrected + " " + correct_word, dictionary, editions + distance)

def compare_with_dict(tocheck_word, dictionary, checked_word, minimum_distance):
    if not dictionary or minimum_distance == 0:
        return checked_word, minimum_distance
    
    #print("Checking " + tocheck_word + " with " + dictionary[0])
    
    checking = dictionary[0]
    dist = lev_distance(tocheck_word, checking, minimum_distance)
    
    #print("Distance: " + str(dist))
    
    if dist < minimum_distance:
        return compare_with_dict(tocheck_word, dictionary[1:], checking, dist)
    else:
        return compare_with_dict(tocheck_word, dictionary[1:], checked_word, minimum_distance)

def main():
    dictionary = save_dictionary()
    original = save_original_text() 

    corrected_text, editions = check_distances(original, "", dictionary, 0)
    
    put_correct_text(corrected_text)
    put_editions(editions)

if __name__=="__main__":
    main()













