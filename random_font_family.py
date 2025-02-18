import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import string
import random



class WindowClass:
    def __init__(self, master):
        self.master = master

        helv36 = tkFont.Font(family="Helvetica", size=18, weight="bold")

        self.btn = tk.Button(
            master,
            text="Start",
            command=self.command,
            bg="#000000",
            fg="#b7f731",
            relief="flat",
            width=30,
            font=helv36
        )
        self.btn.pack(padx=50, pady=200)

    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("800x600")
        Demo2(toplevel)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(
            self.master,
            highlightbackground="green",
            highlightcolor="green",
            highlightthickness=2,
            width=700,
            height=500,
            bd=0
        )

       

        helv36 = tkFont.Font(family="Helvetica", size=18, weight="bold")
        self.label = tk.Label(self.frame, text="Font Family is Helvetica", font=helv36)
        self.label.grid(row=0, column=1,pady=20)

        self.randomFontButton = tk.Button(
            self.frame, text="See Next Random Font Family and Color",
            command=self.randomGen
        )
        self.randomFontButton.grid(row=1, column=1, padx=220, pady=50)

        

        self.frame.grid(padx=50, pady=50)
        self.frame.grid_propagate(0)

    def randomGen(self):

        fonts_list = list(tkFont.families())
        random_font = random.choice(fonts_list)
        random_font_setting = tkFont.Font(family=str(random_font), size=16)

        random_backgroundcolor = random.randrange(0, 2**24)
        hex_value = hex(random_backgroundcolor)
        random_color = "#"+hex_value[2:]
        self.frame.configure(bg = str(random_color))

        self.label.configure(text = "The Font Family is "+random_font+"\n\n And Background value is : #"+hex_value,
                             font = random_font_setting)




root = tk.Tk()
root.title("Random Font Family and Color Generator")
root.geometry("800x600")

cls = WindowClass(root)
root.mainloop()
