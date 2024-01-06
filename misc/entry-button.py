import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Entry
        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.entry.pack(padx=20, pady=10)

        # Button
        self.button = customtkinter.CTkButton(master=self, text="Print Entry", command=self.print_entry)
        self.button.pack(padx=20, pady=10)

    def print_entry(self):
        user_entry = self.entry.get()
        print(user_entry)
        print(type(user_entry))




if __name__ == "__main__":
    app = App()
    app.mainloop()