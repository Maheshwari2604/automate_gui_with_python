#!/usr/bin/python3.4


#library to import file to automate gui
import pyautogui as pyy

#to press keys
pyy.hotkey('alt','tab')

#to click on thses x and y coardinats
pyy.click(250,117)

pyy.hotkey('ctrl', 'a')

#writee somthing on that coardinates
#xample to write somthing on browser url
pyy.typewrite("192.168.43.13:8000")

#to press enter
pyy.press('enter')

