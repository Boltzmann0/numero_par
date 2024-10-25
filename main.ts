function Convert(num: number): number {
    return num * 1.8 + 32
}

function kelvin(K: number): number {
    return K + 273
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(input.temperature())
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showNumber(kelvin(input.temperature()))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(Convert(input.temperature()))
})
