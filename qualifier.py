"""
A GUI application for a rocketship launch control panel.
This application is built on tkinter. See the official
documentation and linked resources here:
    https://docs.python.org/3/library/tkinter.html

Requirements:
    Python 3.
"""
import tkinter as tk

class RocketShipControlPanel(tk.Frame):

    count = 0
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.pilot = None
        self.pilot_label = None
        self.launch_button = None

    def create_form(self):
        """
        Create the input fields, labels,
        and buttons when called.
        """

        self.pilot_label = tk.Label(
            self,
            text="Pilot: "
        )
        self.pilot = tk.Entry(
            self,
            width=30,
            textvariable=name
        )
        self.pilot_label.pack(side=tk.TOP)
        self.pilot.pack(side=tk.TOP)

        self.password_label = tk.Label(
            self,
            text="Password"
        )
        self.password_entry = tk.Entry(
            self,
            width=30,
            show="*",
            textvariable=password
        )
        self.password_label.pack()
        self.password_entry.pack()

        self.launch_button = tk.Button(
            self,
            text="Launch",
            bg="teal",
            fg="white",
            command=self.do_countdown
        )
        self.launch_button.pack(side=tk.BOTTOM)

    def do_countdown(self):
        """
        When the user clicks the login button, this callback
        is invoked. Make it do a countdown. The first time
        it is clicked, the button text should change to "3".
        The next time to "2", then to "1", and then to "LIFTOFF!".

        If the username or the password are blank, this
        callback should not do anything.
        """
        if self.pilot.get() and self.password_entry.get() and self.count == 0:
            self.launch_button["text"]="3"
            self.count += 1
        elif self.count == 1:
            self.launch_button["text"]="2"
            self.count += 1
        elif self.count == 2:
            self.launch_button["text"]="1"
            self.count += 1
        elif self.count == 3:
            self.launch_button["text"]="LIFTOFF!"
            self.count += 1

root = tk.Tk()
app = RocketShipControlPanel(master=root)
name = tk.StringVar()
password = tk.StringVar()
app.create_form()
app.mainloop()
