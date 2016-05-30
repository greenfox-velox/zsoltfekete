#Task_1
def only_alpha(string):
    for letter in string:
        if not letter in "abcdefghjklmnopqrstuvwxyzöüóőúéáű":
            return False
    return True

def anagramm (string_1, string_2):
    letter_1=[]
    letter_2=[]

    for letter in range(len(string_1)):
            letter_1 +=(string_1[letter])
    for letter in range(len(string_2)):
            letter_2 += (string_2[letter])

    if len(string_1) == 0 and len(string_2) == 0:
        return False

    elif only_alpha(string_1) == False or only_alpha(string_2) == False :
            return False

    elif (len(letter_1)==len(letter_2)):
        for letter in letter_1:
            if letter in letter_2:
                letter_2.remove(letter)
                if len(letter_2)==0:
                    return True
            else:
                return False
    else:
        return False

#Task_2
def count_letters(string):
    if len(string) != 0 and only_alpha(string) == True:
        letter_number={}
        for letter in string:
            letter_number[letter] = string.count(letter)
        return letter_number
    else :
        return False
