pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

is_pin1 = input.pin_is_pressed(TouchPin.P1)
is_pin2 = input.pin_is_pressed(TouchPin.P2)

hrac1 = False
hrac2 = False
zahajeni = False
lze_ukazovat = False
podvod1 = False
podvod2 = False

def on_pin_pressed_p1():

    global hrac1

    hrac1 = True
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_pin_pressed_p2():

    global hrac2

    hrac2 = True
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def cast_hry():

    global zahajeni, hrac1, hrac2, lze_ukazovat

    basic.clear_screen()
    basic.pause(randint(3000, 10000))
    lze_ukazovat = True
    zahajeni = True
    music.play_melody("C", 120)

    while zahajeni == True and hrac1 == False and hrac2 == False:
        basic.show_icon(IconNames.YES)
    pause(3000)

forever(cast_hry)

def vyhodnocovani():

    global zahajeni, hrac1, hrac2, podvod1, podvod2
    
    if zahajeni == False and hrac1 == True:
        podvod1 = True
    
    elif zahajeni == False and hrac2 ==  True:
            podvod2 = True


    elif zahajeni == True and podvod1 == True and podvod2 == True:
        basic.show_string("C")
        restart()

    elif zahajeni == True and podvod1 == True:
        basic.show_string("B")
        restart()

    elif zahajeni == True and podvod2 == True:
        basic.show_string("A")
        restart()

    elif zahajeni == True and hrac1 == True:
        basic.show_string("1")
        restart()

    elif zahajeni == True and hrac2 == True:
        basic.show_string("2")
        restart()

    elif zahajeni == True and hrac1 == True and hrac2 == True:
        basic.show_string("R")
        restart()

forever(vyhodnocovani)

def restart():

    global hrac1, hrac2, zahajeni, podvod1, podvod2

    zahajeni = False
    hrac1 = False
    hrac2 = False
    podvod1 = False
    podvod2 = False
    basic.clear_screen()