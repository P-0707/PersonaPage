
import tkinter
from tkinter import BOTH, StringVar, END
import random

#root window
root = tkinter.Tk()
root.title('Words')
root.iconbitmap(r'C:\Users\pavani\Desktop\projjjjj\Quotes\images\word.ico')
root.geometry('600x300')
root.resizable(0,0)

#functions
def quote():

   # name_label = tkinter.Label(output_frame, text="", bg=output_color)

   # style = case_style.get()
    random_quote = ""
    if style.get() == 'Normal':
        with open(r"C:\Users\pavani\Desktop\projjjjj\Quotes\normal_quotes.txt", "r") as f:
            quotes1 = f.readlines()
            random_quote = random.choice(quotes1)
    elif style.get() == 'Motivational':
        with open(r"C:\Users\pavani\Desktop\projjjjj\Quotes\motivational_quotes.txt", "r") as f:
            quotes1 = f.readlines()
            random_quote = random.choice(quotes1)
    elif style.get() == 'Any':
        chosen_files = random.choice([
            r"C:\Users\pavani\Desktop\projjjjj\Quotes\normal_quotes.txt",
            r"C:\Users\pavani\Desktop\projjjjj\Quotes\motivational_quotes.txt"
        ])
        with open(chosen_files, "r") as f:
            quotes1 = f.readlines()
            random_quote = random.choice(quotes1)
    

    hello = "**  Hello!!!!! "+ name.get()+", lets see a quote for you!!  **"
    name_label.config(text=hello)
    label2.config(text=random_quote)

    name.delete(0, END)


#fonts and colors
root_color = '#7dbff1'
output_color = '#a3f8fb'
input_color = '#71a7cd'
fonts_color = '#e66079'
root.config(bg=root_color)

#frames
input_frame = tkinter.LabelFrame(root, bg=input_color, borderwidth=5)
#choose_frame = tkinter.LabelFrame(root, bg=root_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(padx=10, pady=10, ipadx=10, ipady=10, fill=BOTH)
#choose_frame.pack(padx=10, pady=10)
output_frame.pack(padx=10, pady=10, fill=BOTH)

#widgets
name = tkinter.Entry(input_frame, text="what is your name?!", width=20)
submit_button = tkinter.Button(input_frame, text='Submit', command=quote)

name.grid(row=0, column=0, padx=10, pady=10, ipadx=10, columnspan=4, sticky='WE')
submit_button.grid(row=1, column=4, padx=10, pady=10)

#radio buttons
style = StringVar()
style.set('Normal')
motivational_button = tkinter.Radiobutton(input_frame, text='Motivational', bg=input_color, variable=style, value='Motivational')
normal_button = tkinter.Radiobutton(input_frame, text='Normal', bg=input_color, variable=style, value='Normal')
any_button = tkinter.Radiobutton(input_frame, text='Any', bg=input_color, variable=style, value='Any')

motivational_button.grid(row=1, column=0, padx=10, pady=10, ipadx=5)
normal_button.grid(row=1, column=1, ipadx=5)
any_button.grid(row=1, column=2, ipadx=5)

#image
img1 = tkinter.PhotoImage(file= r"C:\Users\pavani\Desktop\projjjjj\Quotes\images\letter.png") 
label1 = tkinter.Label(output_frame, image=img1, height=50, width=50, bg=output_color)
label1.pack()

name_label = tkinter.Label(output_frame, text="", bg=output_color)
name_label.pack()
label2 = tkinter.Label(output_frame, text="", bg=output_color)
label2.pack()
    

#loop
root.mainloop()