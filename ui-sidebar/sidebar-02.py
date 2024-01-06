import customtkinter

class MySidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Logo Label
        self.logo_label = customtkinter.CTkLabel(self, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Check boxes
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        # Button
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

    def get(self):
        checked_checkboxes = []
        if self.checkbox_1.get() == 1:
            checked_checkboxes.append(self.checkbox_1.cget("text"))

        return checked_checkboxes
    
    def button_callback(self):
        print("button pressed", self.get())
    
class MyMainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(4, weight=1)
        # Sidebar
        self.sidebar_frame = MySidebarFrame(self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # Main
        self.main_frame = MyMainFrame(self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsw")
        self.main_frame.configure(fg_color="transparent")


app = App()
app.mainloop()