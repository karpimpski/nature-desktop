from tkinter import *
from tkinter.ttk import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.startup = IntVar()

        self.winfo_toplevel().title("Nature Desktop")

        #create label frame
        label_frame = Frame(self.root)
        label_frame.grid(row=0, columnspan=2, pady=(10))

        #create label
        self.mainLabel = Label(label_frame, text='Settings')
        self.mainLabel.grid()

        #create frames for columns
        left_frame = Frame(self.root)
        left_frame.grid(row=1, column=0, padx=(10,90))
        right_frame = Frame(self.root)
        right_frame.grid(row=1, column=1, padx=(90,10))

        #create first setting
        self.startup_label = Label(left_frame, text="Run on startup?")
        self.startup_label.grid(row=0)

        self.startup_check = Checkbutton(right_frame, variable=self.startup)
        self.startup_check.grid(row=0)

        #create buttons frame
        buttons_frame = Frame(self.root)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=(10))

        #create save button
        self.save_button = Button(
            buttons_frame, text="Save", command=self.save
        )
        self.save_button.grid(column=0, row=0)

        #create back button that goes to first screen
        self.back_button = Button(
            buttons_frame, text="Back", command=self.root.destroy
        )
        self.back_button.grid(column=1, row=0)

    def save(self):
        print(self.startup)