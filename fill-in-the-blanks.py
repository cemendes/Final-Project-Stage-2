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
dic_sample = {'___1___' : 'function', '___2___' : 'variables', '___3___' : 'None', '___4___' : 'list'}
sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


def game_level_guess():
    exit_loop = 0
    while exit_loop == 0:
        level = raw_input("Please, select a game difficulty by typing it in! Possible choices include easy, medium, and hard. ")
        if level.lower() == "easy" or level.lower() == "medium" or level.lower() == "hard":
            print "You've chosen",level,"!"
            return level
        else:
            print level,"is not a valid level!"

    number_of_guesses = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    while number_of_guesses.isdigit() == False:
        print "This is not an integer"
        print("\n")
        number_of_guesses = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
    number_of_guesses = int(number_of_guesses)
    return level, number_of_guesses

def check_answer(choice,choice_pos,sampleA):
    if choice == dic_sample[choice_pos]:
        sample_changed = sampleA.replace(choice_pos,choice)
        return sample_changed

def fill_in_the_blank():
    sample_changed_again = sample
    guess_count = 0
    exit_loop = 0
    level_and_guess = game_level_guess()
    print "This paragraph reads as such: ", sample

    while level_and_guess[1] > guess_count:
        first_choice = raw_input("What should be substituded in for ___1___? ")
        if not check_answer(first_choice,'___1___',sample):
            guess_count += 1
            print "This isn't the correct answer! You only have",level_and_guess[1] - guess_count, "try left. Make it count!"
        else:
            sample_changed_again = check_answer(first_choice,'___1___',sample)
            print sample_changed_again
            break

    while level_and_guess[1] > guess_count:
        second_choice = raw_input("What should be substituded in for ___2___? ")
        if not check_answer(second_choice, '___2___',sample_changed_again):
            guess_count += 1
            print "This isn't the correct answer! You only have",level_and_guess[1] - guess_count, "try left. Make it count!"
        else:
            sample_changed_again = check_answer(second_choice,'___2___',sample_changed_again)
            print sample_changed_again
            break

    while level_and_guess[1] > guess_count:
        third_choice = raw_input("What should be substituded in for ___3___? ")
        if not check_answer(third_choice, '___3___',sample_changed_again):
            guess_count += 1
            print "This isn't the correct answer! You only have",level_and_guess[1] - guess_count, "try left. Make it count!"
        else:
            sample_changed_again = check_answer(third_choice,'___3___',sample_changed_again)
            print sample_changed_again
            break

    while level_and_guess[1] > guess_count:
        fourth_choice = raw_input("What should be substituded in for ___4___? ")
        if not check_answer(fourth_choice, '___4___',sample_changed_again):
            guess_count += 1
            print "This isn't the correct answer! You only have",level_and_guess[1] - guess_count, "try left. Make it count!"
        else:
            sample_changed_again = check_answer(fourth_choice,'___4___',sample_changed_again)
            print sample_changed_again
            break


fill_in_the_blank()