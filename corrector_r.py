#!/usr/bin/env python3
''' Recursive corrector '''
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
    ''' Saves the number of editions in a file '''

    if len(sys.argv) > 1:
        file_d = open(sys.argv[4], "w")
        file_d.write(str(editions))
        file_d.close()
    else:
        print(editions)

def lev_distance(word_1, word_2, min_dist, editions=0):
    ''' Levenshtein distance algorithm '''

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
    ''' Iterates recursively through the words to correct '''

    if not original:
        return corrected, editions
    correct_word, distance = compare_with_dict(original[0], dictionary, "", sys.maxsize)
    return check_distances(original[1:], corrected + " " + correct_word,
                           dictionary, editions + distance)

def compare_with_dict(tocheck_word, dictionary, checked_word, minimum_distance):
    ''' Iterates recursively through the words of the dictionary '''

    if not dictionary or minimum_distance == 0:
        return checked_word, minimum_distance

    checking = dictionary[0]
    if ((len(checking) - len(tocheck_word)) > minimum_distance or
            len(checking) - len(tocheck_word) < -minimum_distance):
        return compare_with_dict(tocheck_word, dictionary[1:], checked_word, minimum_distance)

    dist = lev_distance(tocheck_word, checking, minimum_distance)

    if dist < minimum_distance:
        return compare_with_dict(tocheck_word, dictionary[1:], checking, dist)

    return compare_with_dict(tocheck_word, dictionary[1:], checked_word, minimum_distance)

def main():
    ''' Main function '''

    dictionary = save_dictionary()
    original = save_original_text()

    corrected_text, editions = check_distances(original, "", dictionary, 0)
    put_correct_text(corrected_text[1:])
    put_editions(editions)

if __name__ == "__main__":
    main()
