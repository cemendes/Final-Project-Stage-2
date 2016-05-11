# def game_level_guess():
#     level = 'easy'
#     # if level.lower() == "easy":
#     #     print "You have chosen",level,"!"
#     # elif level.lower() == "medium":
#     #     print "You have chosen",level,"!"
#     # elif level.lower() == "hard":
#     #     print "You have chosen",level,"!"
#     number_of_guesses = 2
#     return level, number_of_guesses
# level_and_guess = game_level_guess()
# var1 = 1
# print level_and_guess[1]
# print type(level_and_guess)
# print level_and_guess[1] > var1

# level = 21
# exit_loop = 2

# while level > 20 or exit_loop == 3:
#     print "I'm in the loop"
#     exit_loop += 1
#     level -= 1

# number_of_guesses = "10a"
# print number_of_guesses
# print number_of_guesses.isdigit()
# while number_of_guesses.isdigit() == False:
#         number_of_guesses = raw_input("How many guesses would you like per problem? Please enter a positive integer number: ")
# #number_of_guesses = int(number_of_guesses)
level == 'easy'

if level.lower() == "easy" or level.lower() == "medium" or level.lower() == "hard":
    print "YAY"


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
