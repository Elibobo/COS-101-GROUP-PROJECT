import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x400")

        self.result_var = tk.StringVar()

        self.create_widgets()


    def create_widgets(self):
        # Entry to display the result
        entry = tk.Entry()




if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
