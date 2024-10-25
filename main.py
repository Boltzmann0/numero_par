def Convert(num: number):
    return num * 1.8 + 32
def kelvin(K: number):
    return K + 273

def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(kelvin(input.temperature()))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(Convert(input.temperature()))
input.on_button_pressed(Button.B, on_button_pressed_b)
