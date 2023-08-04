from tkinter import ttk
import tkinter as tk
from tkinter import *
from time import sleep
from tkinter import messagebox
def result():
    msg = messagebox.showinfo('Result','IDK, Just Look Outside')
    
def analysing():
   def close_loading():
        m3.destroy()
        result()
   def donothing():
       pass

   m3 = tk.Tk()
   m3.geometry('200x100')
   m3.resizable(0,0)
   m3.protocol('WM_DELETE_WINDOW',donothing)
   m3.title('Loading...')
   Label(m3).pack()
   Label(m3, text='Analysing...').pack()
   progress_bar = ttk.Progressbar(m3, length=130, mode='indeterminate')
   progress_bar.pack()
   root.after(5000, close_loading)

    # Start the progress bar animation
   progress_bar.start(10)
   m3.mainloop()

root = tk.Tk()
root.geometry('300x120')
root.title('Crazy AI Weather Reporter')

Label(root).pack()
a = Label(root,text='Choose Location').pack()
b = Entry(root,width='30').pack()
Label(root).pack()
c = Button(root,text="See Result", command=analysing).pack()


root.mainloop()
