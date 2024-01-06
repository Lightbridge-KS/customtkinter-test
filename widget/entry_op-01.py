import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Option Menu
        ## Label
        self.optionmenu_label = customtkinter.CTkLabel(self, text="Options:", font=customtkinter.CTkFont(size=15, weight="bold"), anchor="w")
        self.optionmenu_label.grid(row=0, column=0, padx=10, pady=(20, 0), sticky = "w")
        ## Drop down
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["option 1", "option 2"])
        self.optionmenu.set("option 2")
        self.optionmenu.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        # Entry
        ## Label
        self.entry_label = customtkinter.CTkLabel(self, text="Entry:", font=customtkinter.CTkFont(size=15, weight="bold"), anchor="w")
        self.entry_label.grid(row=2, column=0, padx=10, pady=(20, 0), sticky = "w")
        ## Text box
        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        # Button
        self.button = customtkinter.CTkButton(master=self, text="CTkButton", command=self.button_event)
        self.button.grid(row=4, column=0, padx=10, pady=20, sticky="ew")


    def button_event(self):
        print("optionmenu dropdown clicked:", self.optionmenu.get())
        print("Entry:", self.entry.get())

app = App()
app.mainloop()



