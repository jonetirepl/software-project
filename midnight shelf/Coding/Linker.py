from customtkinter import *
from PIL import Image
from login_page import Login

state_linker = Login.state


if(state_linker == '#1'):
    Login.login_window()
elif(state_linker == '#2'):
     print('reg')

