import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        # Entry
        ## Label
        self.entry_label = customtkinter.CTkLabel(self, text="Entry:", font=customtkinter.CTkFont(size=15, weight="bold"), anchor="w")
        self.entry_label.grid(row=0, column=0, padx=10, pady=(20, 0))
        ## Text box
        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.entry.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        # Button
        self.button = customtkinter.CTkButton(master=self, text="CTkButton", command=self.button_event)
        self.button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")


    def button_event(self):
        print("entry:", self.entry.get())

app = App()
app.mainloop()



