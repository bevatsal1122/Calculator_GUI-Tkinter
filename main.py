# Code by bevatsal1122 (GitHub)
# Trust God, Your Code will Work

from tkinter import *

# Window divided in 2 Frames
# 1st Frame --> Display Frame
# 2nd Frame --> Buttons Frame

# 1st Frame (Display Frame) is divided in 2 Labels
# 1st Label --> Total Expression
# 2nd Label --> Current Expression


class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("370x640")
        self.window.resizable(False, False)

        self.t_expression = ""
        self.c_expression = ""
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }
        self.operations = {
            '/': "\u00F7",
            '*': "\u00D7",
            '+': '+',
            '-': '-'
        }

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_label, self.current_label = self.create_display_labels()
        self.create_digits_buttons()
        self.create_operations_buttons()
        self.create_special_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

    def create_display_frame(self):
        frame = Frame(self.window, height=240)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = Frame(self.window, bg="black")
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.t_expression, anchor=E, bg="black", fg="white", padx=24,
                            font=("Arial", 18))
        total_label.pack(expand=True, fill="both")
        current_label = Label(self.display_frame, text=self.c_expression, anchor=E, bg="black", fg="white", padx=24,
                              font=("Arial", 40, "bold"))
        current_label.pack(expand=True, fill="both")
        return total_label, current_label

    def add_to_current_label(self, value):
        self.c_expression += str(value)
        self.update_current_label()

    def add_operators(self, op):
        self.c_expression += str(op)
        self.t_expression = self.c_expression
        self.c_expression = ""
        self.update_current_label()
        self.update_total_label()

    def print_result(self):
        self.t_expression += self.c_expression
        self.update_total_label()
        self.c_expression = str(eval(self.t_expression))
        self.update_current_label()

    def clear_everything(self):
        self.c_expression = ""
        self.t_expression = ""
        self.update_current_label()
        self.update_total_label()

    def create_digits_buttons(self):
        for digit, grid_values in self.digits.items():
            button = Button(self.buttons_frame, text=str(digit), bg="#292929", fg="white",
                            font=("Arial", 26, "bold"), border=0.5,
                            command=lambda x=digit: self.add_to_current_label(x))
            button.grid(row=grid_values[0], column=grid_values[1], sticky=NSEW)

    def create_operations_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = Button(self.buttons_frame, text=symbol, bg="#292929", fg="white",
                            font=("Arial", 28, "bold"), border=0.5,
                            command=lambda x=operator: self.add_operators(x))
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def create_special_buttons(self):
        clear_button = Button(self.buttons_frame, text='C', bg="#292929", fg="white",
                              font=("Arial", 24, "bold"), border=0.5,
                              command=self.clear_everything)
        clear_button.grid(row=0, column=1, columnspan=3, sticky=NSEW)
        equal_button = Button(self.buttons_frame, text='=', bg="#292929", fg="white",
                              font=("Arial", 24, "bold"), border=0.5,
                              command=self.print_result)
        equal_button.grid(row=4, column=3, columnspan=2, sticky=NSEW)
        return clear_button, equal_button

    def update_total_label(self):
        self.total_label.config(text=self.t_expression)

    def update_current_label(self):
        self.current_label.config(text=self.c_expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    play = Calculator()
    play.run()
