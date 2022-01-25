import tkinter as tk
from tkinter import ttk
#from PIL import Image, ImageTk

root = tk.Tk()                                     #start a tk interpreter
root.geometry("640x1280")                          
root.title(" Madlibs Game ")
root.configure(bg='#adebad')

#Formatting The Form Display
frm = ttk.Frame(root, padding=10)                  #Ordering and placement of UI elements in columns 
frm.place(relx=.5, rely=.45, anchor="center")

render = tk.PhotoImage(file="./madlib2.png")
img_label = ttk.Label(image = render)
img_label.image = render
img_label.place(relx=.5, rely=0.02, anchor="n")

#Declaring Variables, Labels & Inputs
junk = tk.Label(frm, text="").grid(column=0, row=1, pady=40)

des = tk.Label(frm, text="Descriptive word:").grid(column=0, row=4)
desInput = tk.Entry(frm)
desInput.grid(column=1, row=4, sticky="")

cliche = tk.Label(frm, text="Adjective: ").grid(column=0, row=5, pady=10)
clicheInput = tk.Entry(frm)
clicheInput.grid(column=1, row=5)

guru = tk.Label(frm, text="Profession: ").grid(column=0, row=6)
guruInput = tk.Entry(frm)
guruInput.grid(column=1, row=6)

cool = tk.Label(frm, text="Admiration word: ").grid(column=0, row=7, pady=10)
coolInput = tk.Entry(frm)
coolInput.grid(column=1, row=7)

hobby = tk.Label(frm, text="Hobby: ").grid(column=0, row=8)
hobbyInput = tk.Entry(frm)
hobbyInput.grid(column=1, row=8)

crush = tk.Label(frm, text="Describe your crush: ").grid(column=0, row=9, pady=10)
crushInput = tk.Entry(frm)
crushInput.grid(column=1, row=9)

verb = tk.Label(frm, text="Verb in -ing form: ").grid(column=0, row=10)
verbInput = tk.Entry(frm)
verbInput.grid(column=1, row=10)

place = tk.Label(frm, text="Name of a place: ").grid(column=0, row=11, pady=10)
placeInput = tk.Entry(frm)
placeInput.grid(column=1, row=11)

food = tk.Label(frm, text = "Favorite food: ").grid(column=0, row=12)
foodInput = tk.Entry(frm)
foodInput.grid(column=1, row=12)

habit = tk.Label(frm, text = "Annoying habit: ").grid(column=0, row=13, pady=10)
habitInput = tk.Entry(frm)
habitInput.grid(column=1, row=13)

name = tk.Label(frm, text = "Name of best friend: ").grid(column=0, row=14)
nameInput = tk.Entry(frm)
nameInput.grid(column=1, row=14)

apologize = tk.Label(frm, text = "Single word of apology: ").grid(column=0, row=15, pady=10)
apologizeInput = tk.Entry(frm)
apologizeInput.grid(column=1, row=15)

unreal = tk.Label(frm, text = "Descriptive word: ").grid(column=0, row=16)
unrealInput = tk.Entry(frm)
unrealInput.grid(column=1, row=16)

feelings = tk.Label(frm, text = "Single word of comment: ").grid(column=0, row=17, pady=10)
feelingsInput = tk.Entry(frm)
feelingsInput.grid(column=1, row=17)

#Function Definition For Getting the Inputs and Displaying Them
def callback():
    story = f"Team Proton is a group of 8 {desInput.get()} people.\nThe various members are {clicheInput.get()} in unique ways. \nWe have our teachop, Lawrence the {guruInput.get()} of the group. He is a/an {coolInput.get()}, dad-joke-telling kind of person. He likes to {hobbyInput.get()}. \nOur female team member Dami is very {crushInput.get()}. She secretly likes to {verbInput.get()} at {placeInput.get()}. \nCharles favorite food is {foodInput.get()}. He actually can't stand {habitInput.get()}. \nWe don't think {nameInput.get()} is in our group but if he/she is, then we are {apologizeInput.get()}. WoW! You cooked this {unrealInput.get()} story, you are really {feelingsInput.get()}."
    top = tk.Toplevel()
    textArea = tk.Text(top, height=30, width=100)
    textArea.grid(column=0, row=21, columnspan = 6)
    textArea.tag_config('justified', justify='left')
    textArea.insert(tk.END, story, 'justified')

#Button Creation
btn = tk.Button(frm, text="Generate", command=callback)  #Calling the callback function
btn.grid(column=0, row=20, pady=10)
btn.configure(bg="#00ff00")
btn1 = tk.Button(frm, text="Quit", command=root.destroy)
btn1.grid(column=1, row=20)
btn1.configure(bg="#ff0000", fg="#fff")
root.mainloop()  #tkinter event loop. This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until the window it's called on is closed
