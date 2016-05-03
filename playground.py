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

level = 21
exit_loop = 2

while level > 20 or exit_loop == 3:
    print "I'm in the loop"
    exit_loop += 1
    level -= 1
