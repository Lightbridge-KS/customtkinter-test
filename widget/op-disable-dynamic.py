import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        # Option Menu
        ## Label
        self.optionmenu_label = customtkinter.CTkLabel(self, text="Options:", font=customtkinter.CTkFont(size=15, weight="bold"), anchor="w")
        self.optionmenu_label.grid(row=0, column=0, padx=10, pady=(20, 0))
        ## Drop down 1
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self, state="normal",  values=["normal", "disabled"], command=self.optionmenu_1_event)
        self.optionmenu_1.set("normal")
        self.optionmenu_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        ## Drop down 2
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self, state="normal",  values=["option 1", "option 2"])
        self.optionmenu_2.set("option 2")
        self.optionmenu_2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        # Button
        self.button = customtkinter.CTkButton(master=self, text="CTkButton", command=self.button_event)
        self.button.grid(row=3, column=0, padx=10, pady=20, sticky="ew")

    def optionmenu_1_event(self, choice):
        print("Option 1: ", choice)
        self.optionmenu_2.configure(state = choice)
    def button_event(self):
        print("Button clicked with option 1: {}, option 2: {}".format(self.optionmenu_1.get(), self.optionmenu_2.get()))

app = App()
app.mainloop()



