from blinkt import set_pixel, set_brightness, show, clear


set_brightness(0.1)

i = 0

def back():
    global i
    while i >= 0 :

        set_pixel(i, 255, 255, 255)
        show()
        i -= 1
        clear()
        show()
        if i == 0:
            forward()
def forward():
    global i
    while i < 7:

        set_pixel(i, 255, 255, 255)
        show()
        i += 1
        clear()
        show()
        if i == 7:
            back()

forward()
