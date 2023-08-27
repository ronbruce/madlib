
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

adjective = input("Hi there! Enter a discriptive word here: ")
noun = input("Great! Now enter a name of a person: ")
place = input("You're doing great! Let's get specific. Enter a place: ")
verb = input("Let's turn up the heat. Enter an action word: ")
adjective_2 = input("Enter another discriptive word: ")
noun_2 = input("Enter another name of a person: ")
number = input("Cool! Now enter a number: ")
adjective_3 = input("You're almost there. Enter another discriptive word: ")
adjective_4 = input("Enter one more discriptive word: ")
verb_2 = input("Last one. Enter a another verb: ")

def print_story(adjective, noun, place, verb, adjective_2, noun_2, number, adjective_3, adjective_4, verb_2):
    line_1 = f"Once upon a time, there was a {adjective} hero named {noun}. \n"
    line_2 = f"{noun} lived in the magical world of {place}. \n"
    line_3 = f"One day, {noun} met a {adjective_2} princess named {noun_2}. \n"
    line_4 = f"{noun} and {noun_2} set out on an adventure to {verb} the {adjective_3} Heartless that was terrorizing {place}.\n"
    line_5 = f"Along the way, they met {number} {adjective_4} Disney characters and faced many dangerous challenges. \n"
    line_6 = f"In the end, {noun} and {noun_2} were victorious and {verb_2} the day. \n"
    whole_story = line_1 + line_2 + line_3 + line_4 + line_5 + line_6
    print(whole_story)

print_story(adjective, noun, place, verb, adjective_2, noun_2, number, adjective_3, adjective_4, verb_2)    









































# --------------------------------------------------
# Partial solution
























# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")