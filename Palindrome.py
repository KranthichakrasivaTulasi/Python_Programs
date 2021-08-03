def is_palindrome(string):
    string = "".join(string.split())                         # joins the spaces
    return string[::-1].casefold() == string.casefold()      # checks the cases of the given input

word = input("please enter a sentence: ")
sentence = ""

for character in word:
    if character.isalnum() == True:
        sentence += character

if is_palindrome(sentence):
    print("{0} is a palindrome word".format(word))
else:
    print(word," is not a palindrome word")
