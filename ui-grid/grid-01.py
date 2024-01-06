import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        # Grid Geometry
        self.button.grid(row=0, column=0, padx=20, pady=20)
        self.grid_columnconfigure(0, weight=1)

    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()