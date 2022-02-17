pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let is_pin1 = input.pinIsPressed(TouchPin.P1)
let is_pin2 = input.pinIsPressed(TouchPin.P2)
let hrac1 = false
let hrac2 = false
let zahajeni = false
let lze_ukazovat = false
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    hrac1 = true
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    hrac2 = true
})
forever(function cast_hry() {
    
    console.logValue("x", zahajeni)
    basic.clearScreen()
    basic.pause(randint(3000, 10000))
    let lze_ukazovat = true
    zahajeni = true
    music.playMelody("C", 120)
    basic.showIcon(IconNames.Heart)
    while (zahajeni == true) {
        basic.showIcon(IconNames.Heart)
    }
})
forever(function vyhodnocovani() {
    
    if (zahajeni == true && hrac1 == true) {
        restart()
        basic.showString("1")
    } else if (zahajeni == true && hrac2 == true) {
        restart()
        basic.showString("2")
    } else if (zahajeni == true && hrac1 == true && hrac2 == true) {
        restart()
        basic.showString("R")
    } else if (zahajeni == false && hrac1 == true && lze_ukazovat == true) {
        restart()
        basic.showString("B")
    } else if (zahajeni == false && hrac2 == true && lze_ukazovat == true) {
        restart()
        basic.showString("A")
    } else if (zahajeni == false && hrac1 == true && hrac2 == true && lze_ukazovat == true) {
        restart()
        basic.showString("C")
    }
    
})
function restart() {
    
    basic.clearScreen()
    hrac1 = false
    hrac2 = false
    zahajeni = false
}

