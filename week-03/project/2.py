def palindrome_checker(text):
    palindromes = []
    for start_1 in range(len(text)):
        letter_1 = text[start_1]
        for start_2 in range(start_1,len(text)):
            letter_2 = text[start_2]
            distance = start_2 - start_1
            if (letter_1 == letter_2) and distance > 1:
                if text[start_1 :start_2 +1] == text[start_2 : start_1 -1: -1]:
                    palindromes += [text[start_1: start_2 + 1]]
    return(palindromes)

def palindrome_checker_2(text):
    palindromes = []
    for x in range((len(text))-2):
        for y in range( 3,len(text)):
            if text[x : x+y] == text[x : x+y][::-1]:
                palindromes.append(text[x : x+y])

    return(palindromes)

print(palindrome_checker('dog goat dad duck doodle never'))
print(palindrome_checker_2('dog goat dad duck doodle never'))
