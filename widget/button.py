import customtkinter

def button_event():
        print("button pressed")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.button = customtkinter.CTkButton(master=self, text="CTkButton", command=button_event)
        self.button.pack(padx=20, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()