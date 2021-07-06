import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
from gpiozero import Button
from time import sleep

button1 = Button(17)
button2 = Button(27)
button3 = Button(22)
button4 = Button(23)

# Configuration for CS and DC pins
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# 2.2", 2.4", 2.8", 3.2" ILI9341
disp = ili9341.ILI9341(spi, rotation=90, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE)

if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height




image = Image.new("RGB", (320, 240))
draw = ImageDraw.Draw(image)

# Pressing different buttons will successfully draw on the screen without clearing it first    

while True:
    if button1.is_pressed:
        print("button 1 pressed")
        draw.rectangle((0, 0, 20, 20), fill="blue")
        disp.image(image)
    if button2.is_pressed:
        print("button 2 pressed")
        draw.rectangle((20, 20, 40, 40), fill="red")
        disp.image(image)
    if button3.is_pressed:
        print("button 3 pressed")
    if button4.is_pressed:
        print("button 4 pressed")
    sleep(.5)


