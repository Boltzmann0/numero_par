from microbit import *
import random

# An error could appear if you press button B without pressing button A first.
# If the variable 'number' has not been assigned.
# To work around this, the value of 101 is assigned to the variable 'number'
# at the start of the program. When you press button B the program tests
# first to see if the value of 'number' is 101 - if it is, it shows a helpful message.

number = 101

while True:
    if button_a.was_pressed():
        number = random.randint(1, 100)
        display.scroll(number)
    if button_b.was_pressed():
        if number == 101:
            display.scroll('no number chosen yet')
        elif number%2 == 0:
            display.scroll('even')
        else:
            display.scroll('odd')
