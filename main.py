import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

    def create_widgets(self):
        # Entry to display the result
        entry = tk.Entry()




if __name__ == "__main__":
    app = Calculator()
    app.mainloop()