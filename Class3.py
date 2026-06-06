#Desktop Digital Clock(GUI)

#IMPORT TKINTER 
from tkinter import Tk, Label
from time import strftime

root = Tk()
root.title('Python Clock')
 
def update_time():
    #Format: Hour;Minute;second AM/PM
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, update_time)

#styling the cklock
lbl = Label(root, font=('calibri', 40 ,'bold'),background='purple', foreground='white')
lbl.pack(anchor='center')

update_time()
root.mainloop()
