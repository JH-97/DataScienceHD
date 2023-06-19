# A program that reads a string and makes each alternate character an UPPERCASE
# character and the others lower e.g Hello World -> HeLlO WoRlD
# and then makes each alternate word change case 
# e.g Hello World World Hello -> HELLO world WORLD hello

input_phrase = input('Enter a phase to be manipulated: ')
case_letter = ""

# for loop to change the case of alternating characters
for i in range(len(input_phrase)):
    if i % 2 == 0: 
        case_letter += input_phrase[i].lower() 
    else:
        case_letter += input_phrase[i].upper()
print(case_letter)


# Splits the input phrase at every space into a indexed list.
# Loops through list making evenly indexed words uppercase and odd lowercase.
# Then joins each element of list with a space (' ')
phrase_list = input_phrase.split(" ")
for i in range(len(phrase_list)):
    if i % 2 == 0:
        phrase_list[i] = phrase_list[i].upper()
    else:
        phrase_list[i] = phrase_list[i].lower()
case_word = " ".join(phrase_list)
print(case_word)