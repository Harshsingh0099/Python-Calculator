import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display
        self.display = tk.Entry(master, width=30, justify='right', font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Add the buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)

        self.create_button('=', 5, 0, columnspan=4)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, padx=10, pady=5, font=('Arial', 14), command=lambda: self.click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
        elif key == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()