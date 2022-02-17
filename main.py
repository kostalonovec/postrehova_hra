pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

is_pin1 = input.pin_is_pressed(TouchPin.P1)
is_pin2 = input.pin_is_pressed(TouchPin.P2)

hrac1 = False
hrac2 = False
zahajeni = False
lze_ukazovat = False

def on_pin_pressed_p1():

    global hrac1

    hrac1 = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_pin_pressed_p2():

    global hrac2

    hrac2 = True
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def cast_hry():

    global zahajeni, hrac1, hrac2

    console.log_value("x", zahajeni)
    basic.clear_screen()
    basic.pause(randint(3000, 10000))
    lze_ukazovat = True
    zahajeni = True
    music.play_melody("C", 120)
    while zahajeni == True:
        basic.show_icon(IconNames.YES)

forever(cast_hry)

def vyhodnocovani():

    global zahajeni, hrac1, hrac2, lze_ukazovat

    if zahajeni == True and hrac1 == True:
        basic.show_string("1")
        restart()

    elif zahajeni == True and hrac2 == True:
        basic.show_string("2")
        restart()

    elif zahajeni == True and hrac1 == True and hrac2 == True:
        basic.show_string("R")
        restart()

    elif zahajeni == False and hrac1 == True and lze_ukazovat == True:
        basic.show_string("B")
        restart()

    elif zahajeni == False and hrac2 ==  True and lze_ukazovat == True:
        basic.show_string("A")
        restart()

    elif zahajeni == False and hrac1 == True and hrac2 == True and lze_ukazovat == True:
        basic.show_string("C")
        restart()

forever(vyhodnocovani)

def restart():

    global hrac1, hrac2, zahajeni, lze_ukazovat

    zahajeni = False
    hrac1 = False
    hrac2 = False
    lze_ukazovat = False
    basic.clear_screen()