from tkinter import *
from tkinter.ttk import *

class Application(Frame):
    def __init__(self, root, functions, platform, master=None):
        super().__init__(master)
        self.root = root
        self.functions = functions
        self.platform = platform
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Nature Desktop")
        #create label frame
        label_frame = Frame(self.root)
        label_frame.grid(row=0, pady=(10,10), padx=10)

        #create label
        self.mainLabel = Label(label_frame, text='This application will change your desktop background. Continue?')
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

        #create settings button to open settings window
        self.second_button = Button(buttons_frame, text='Settings')
        self.second_button.grid(row=0, column=2)

    def yes_hit(self):
        self.root.destroy()
        image_url = self.functions.get_image_url(self.platform)

        #test that a url was retrieved
        if image_url != 1:
            #download and set the background image
            self.platform.download_image(image_url)
            self.platform.set_background()