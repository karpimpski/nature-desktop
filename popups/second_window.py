from tkinter import *
from tkinter.ttk import *

class Application(Frame):
    def __init__(self, root, platform, master=None):
        super().__init__(master)
        self.root = root
        self.platform = platform
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Nature Desktop")
        #create label frame
        label_frame = Frame(self.root)
        label_frame.grid(row=0, pady=(10,10), padx=10)

        #create label
        self.mainLabel = Label(label_frame, text='Would you like to save the image to your disk?')
        self.mainLabel.grid(row=0)

        #create buttons frame
        buttons_frame = Frame(self.root)
        buttons_frame.grid(row=1, pady=(0,10), padx=10)

        #create yes button
        self.mainButton = Button(buttons_frame, text='Yes', command=self.yes_hit)
        self.mainButton.grid(row=0, column=0)

        #create no button that exits application
        self.quit_button = Button(
            buttons_frame, text="No", command=self.root.destroy
        )
        self.quit_button.grid(row=0, column=1)

    def yes_hit(self):
        self.root.destroy()
        self.platform.save_background()