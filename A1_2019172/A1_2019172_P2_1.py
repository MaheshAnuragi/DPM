# importing a english_words for checking a english_word_set
from english_words import english_words_set
# taking a input as String
a=input("Enter a password: ")

# function for checking a word_Set is or not
def word_Set(a):
    for i in range(len(a)):
        subString = ""
        for j in range(i,len(a)):
            subString += a[j]       # here i making a subString part
            if(subString in english_words_set):     # if it present
                if(len(subString)<3):               #if it smaller than 3 it will continue otherwise it returns True
                     continue
                #print(subString)
                return True
    return False                # if not return False

# checking a lower case is present or not
def isLower(a):
    for i in range(len(a)):     #runs a loop from 0 to len(a)-1
        if(a[i].islower()):     #if lower present return True
            return True
    return False        # after looping returns False

# checking a upper case is present or not
def isUpper(a):
    if(a[0].isupper() or a[len(a)-1].isupper()):    #for checking a begining and ending a case
        return False
    for i in range(1,len(a)-1): #runs a loop from 0 to len(a)-1
        if(a[i].isupper()): #if upper present return True
            return True
    return False    # after looping returns False

# checking a digit case is present or not
def isDigit(a):
    if(a[0].isdigit() or a[len(a)-1].isdigit()): #for checking a begining and ending a case
        return False
    for i in range(1,len(a)-1): #runs a loop from 0 to len(a)-1
        if(a[i].isdigit()):     #if digit present return True
            return True
    return False        # after looping returns False

# checking a special case is present or not
def specialChar(a):
    set_char = {'#', '$', '%', '&', '!'}
    if(a[0] in set_char or a[len(a)-1] in set_char):    #for checking a begining and ending a case
        return False
    for i in range(1,len(a)-1):     #runs a loop from 0 to len(a)-1
        if(a[i] in set_char):       #if specail case present return True
            return True
    return False        # after looping returns False


# for checking a cases
def solve(a):
    if(len(a)<8):
        return False
    elif(word_Set(a)):
        return False
    elif(isLower(a)==False):
        return False
    elif(isUpper(a)==False):
        return False
    elif(isDigit(a)==False):
        return False
    elif(specialChar(a)==False):
        return False
    return True

# print a result
print(solve(a))