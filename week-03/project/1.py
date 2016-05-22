def palindrome_generator (word):
    if word == word[::-1]:
        print ("This is palindrome.")
    else:
         print (word + word[::-1])

palindrome_generator("apa")
palindrome_generator("anya")
