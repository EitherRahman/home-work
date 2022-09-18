numberofWords = 0
numberofDigits = 0
numberofLetters = 0
text = input("Enter a text :")
for x in text:
    if x >= 'a' and x <= 'z':
        numberofLetters = numberofLetters + 1
    elif x >= '0' and x <= '9':
        numberofDigits = numberofDigits + 1
    elif x == ' ':
        numberofWords = numberofWords + 1
print("Number of words : ", numberofWords + 1)
print("Number of letters : ", numberofLetters)
print("Number of digits : ", numberofDigits)
