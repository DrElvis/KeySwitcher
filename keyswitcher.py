import os
from time import sleep
import pyautogui
import pyperclip

selected = os.popen('xsel -p -o').read()
buffer = os.popen('xsel -b -o').read()
key_en = '`qwertyuiop[]asdfghjkl;\'zxcvbnm,./~QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?@#$%^&ёйцукенгшщзхъфывапролджэячсмитьбю.ЁЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"№;%:?'
key_ru = 'ёйцукенгшщзхъфывапролджэячсмитьбю.ЁЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"№;%:?`qwertyuiop[]asdfghjkl;\'zxcvbnm,./~QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?@#$%^&'
convert = ''.join([key_ru[key_en.index(x)] if key_en.find(x)>=0 else x for x in selected])
pyperclip.copy(convert)
sleep(0.1)
pyautogui.hotkey('ctrl', 'v')
pyperclip.copy(buffer)
pyautogui.hotkey('win', 'space')