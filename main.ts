pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let is_pin1 = input.pinIsPressed(TouchPin.P1)
let is_pin2 = input.pinIsPressed(TouchPin.P2)
let hrac1 = false
let hrac2 = false
let zahajeni = false
let lze_ukazovat = false
let podvod1 = false
let podvod2 = false
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    hrac1 = true
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    hrac2 = true
})
forever(function cast_hry() {
    
    basic.clearScreen()
    basic.pause(randint(3000, 10000))
    lze_ukazovat = true
    zahajeni = true
    music.playMelody("C", 120)
    while (zahajeni == true && hrac1 == false && hrac2 == false) {
        basic.showIcon(IconNames.Yes)
    }
    pause(3000)
})
forever(function vyhodnocovani() {
    
    if (zahajeni == false && hrac1 == true) {
        podvod1 = true
    } else if (zahajeni == false && hrac2 == true) {
        podvod2 = true
    } else if (zahajeni == true && podvod1 == true && podvod2 == true) {
        basic.showString("C")
        restart()
    } else if (zahajeni == true && podvod1 == true) {
        basic.showString("B")
        restart()
    } else if (zahajeni == true && podvod2 == true) {
        basic.showString("A")
        restart()
    } else if (zahajeni == true && hrac1 == true) {
        basic.showString("1")
        restart()
    } else if (zahajeni == true && hrac2 == true) {
        basic.showString("2")
        restart()
    } else if (zahajeni == true && hrac1 == true && hrac2 == true) {
        basic.showString("R")
        restart()
    }
    
})
function restart() {
    
    zahajeni = false
    hrac1 = false
    hrac2 = false
    podvod1 = false
    podvod2 = false
    basic.clearScreen()
}

