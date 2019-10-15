# MrNetTek
# eddiejackson.net/blog
# 10/14/2019
# free for public use 
# free to claim as your own

import tkinter as tk
import webbrowser
 
# FUNCTION
def openURL(x):
    new = 2   
    webbrowser.open(x,new=new)
 
# FORM SETUP
root = tk.Tk()
root.geometry("350x300")# X Y
root.resizable(0,0)
root.title("")
 
# button
button = tk.Button(root, 
                    text='Google Search', 
                    width=25,                    
                    command= lambda: openURL("http://google.com"))
button.pack()
 
root.mainloop()