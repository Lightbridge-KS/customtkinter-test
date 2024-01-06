
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        txt = """
        Some 
        Long 
        Text
        """
        self.label = customtkinter.CTkLabel(master=self, text= txt)
        self.label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)



if __name__ == "__main__":
    app = App()
    app.mainloop()

