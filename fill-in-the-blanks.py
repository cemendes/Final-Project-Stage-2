# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.


# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
easy_dic = {'___1___' : 'function', '___2___' : 'variables', '___3___' : 'None', '___4___' : 'list'}
easy_sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

medium_dic = {'___1___' : 'world', '___2___' : 'python', '___3___' : 'print', '___4___' : 'html',}
medium_sample = '''A common first thing to do in a language is display 'Hello ___1___!'  In ___2___ this is particularly easy;
all you have to do is type in: ___3___ "Hello ___1___!" Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and produces a program which does something, so it is useful
in that capacity.'It may seem a bit odd to do something in a Turing complete language that can be done even more easily
with an ___4___ file in a browser, but it's a step in learning ___2___ syntax, and that's really its purpose.'''

hard_dic = {'___1___' : 'class', '___2___' : 'semantics', '___3___' : 'methods', '___4___' : 'python',}
hard_sample = '''Compared with other programming languages, Python’s ___1___ mechanism adds ___1___s with a minimum of new syntax
and ___2___. It is a mixture of the ___1___ mechanisms found in C++ and Modula-3. Python ___1___es provide all the standard
features of Object Oriented Programming: the ___1___ inheritance mechanism allows multiple base ___1___es, a derived ___1___ can
override any ___3___ of its base ___1___ or ___1___es, and a method can call the __3__ of a base ___2___ with the same name.
Objects can contain arbitrary amounts and kinds of data. As is true for modules, ___1___es partake of the dynamic nature
of Python: they are created at runtime, and can be modified further after creation.'''

dictionaries = {'easy' : easy_dic, 'medium' : medium_dic, 'hard' : hard_dic}
samples = {'easy' : easy_sample, 'medium' : medium_sample, 'hard' : hard_sample}

def game_level_guess():
    '''Asks the user for the level and number of guesses. Level should be easy, medium or hard and number_of_guesses should be an integer.
       It will return level and number_of_guesses'''
    exit_loop = 0
    while exit_loop == 0:
        level = raw_input("Please, select a game difficulty by typing it in! Possible choices include easy, medium, and hard. ")
        if level.lower() in ['easy','medium','hard']:
            print "You've chosen",level,"!"
            exit_loop += 1
        else:
            print level,"is not a valid level!"
    number_of_guesses = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    while number_of_guesses.isdigit() == False:
        print "This is not an integer"
        print("\n")
        number_of_guesses = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    number_of_guesses = int(number_of_guesses)
    return level,number_of_guesses

def check_answer(choice,choice_pos,sampleA,dictionary):
    '''Check if the answer is correct. if true, it changes the variable using the dictionary. It will return sample_changed with the correct answered
    inputed by the user'''
    if choice == dictionary[choice_pos]:
        sample_changed = sampleA.replace(choice_pos,choice)
        return sample_changed

def fill_in_the_blank():
    '''This is the main function. It will call check_answer and number_of_guesses as use its inputs. The output will be either the sample with the right answer
       or it will ask for the user to try again.'''
    guess_count = 0
    exit_loop = 0
    level_and_guess = game_level_guess()
    dictionary_to_use = dictionaries[level_and_guess[0]]
    sample_changed_again = samples[level_and_guess[0]]

    print "This paragraph reads as such: ", sample_changed_again

    for n in sorted(dictionary_to_use.keys()):
        while level_and_guess[1] > guess_count:
            first_choice = raw_input("What should be substituded in for" + n + "?")
            if not check_answer(first_choice,n,sample_changed_again,dictionary_to_use):
                guess_count += 1
                print "This isn't the correct answer! You only have",level_and_guess[1] - guess_count,"try left. Make it count!"
            else:
                sample_changed_again = check_answer(first_choice,n,sample_changed_again,dictionary_to_use)
                print sample_changed_again
                break



fill_in_the_blank()