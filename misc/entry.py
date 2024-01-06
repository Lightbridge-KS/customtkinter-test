import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Entry
        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="CTkEntry")
        self.entry.pack(padx=20, pady=10)
        # Button
        self.button = customtkinter.CTkButton(master=self, text="CTkButton", command=self.show_text)
        self.button.pack(padx=20, pady=10)

        # Output TextBox
        self.output_textbox = customtkinter.CTkTextbox(self, height = 150, width = 250) 
        self.output_textbox.pack(padx=20, pady=20)

    def show_text(self):
        self.output_textbox.insert("0.0", f"Some example text!: {self.entry.get()}\n")



if __name__ == "__main__":
    app = App()
    app.mainloop()