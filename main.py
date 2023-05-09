import tkinter as tk
from tkinter import ttk


class myApp:
    def __init__(self):
        self.expression = ""
        self.root = tk.Tk()
        self.root.geometry("350x550")
        self.root.title("Calculator-Let's Compute!")
        self.root.resizable(False, False)
        self.root.config(background='#06010a')

        self.input_Frame = tk.Frame(self.root, width=400, height=50)
        self.input_Frame.pack(padx=10, pady=40)

        self.input_state = tk.StringVar()
        self.input = tk.Entry(self.input_Frame, textvariable=self.input_state, width=50, font=('Arial', 20),
                              justify=tk.RIGHT)
        self.input.grid(row=0, column=0)
        self.input.pack(ipady=20)
        self.input.focus()

        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.columnconfigure(2, weight=1)
        self.buttonFrame.columnconfigure(3, weight=1)
        self.buttonFrame.columnconfigure(4, weight=1)
        self.buttonFrame.rowconfigure(0, weight=1)
        self.buttonFrame.rowconfigure(1, weight=1)
        self.buttonFrame.rowconfigure(2, weight=1)
        self.buttonFrame.rowconfigure(3, weight=1)
        self.buttonFrame.rowconfigure(4, weight=1)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('custom.TButton', background='#c4c4c4',relief='flat',font=('Arial',18))
        # ROW - 0
        self.C = ttk.Button(self.buttonFrame, text="C", command=lambda: self.onclick("C"), style='custom.TButton')
        self.C.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.mod = ttk.Button(self.buttonFrame, text="%", command=lambda: self.onclick("%"), style='custom.TButton')
        self.mod.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.delete = ttk.Button(self.buttonFrame, text="Del", command=lambda: self.onclick("Del"), style='custom'
                                                                                                          '.TButton')
        self.delete.grid(row=0, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
        self.div = ttk.Button(self.buttonFrame, text="/", command=lambda: self.onclick("/"), style='custom.TButton')
        self.div.grid(row=0, column=3, sticky=tk.W + tk.E + tk.N + tk.S)

        # ROW - 1
        self.seven = ttk.Button(self.buttonFrame, text="7", command=lambda: self.onclick("7"), style='custom.TButton')
        self.seven.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.eight = ttk.Button(self.buttonFrame, text="8", command=lambda: self.onclick("8"), style='custom.TButton')
        self.eight.grid(row=1, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.nine = ttk.Button(self.buttonFrame, text="9", command=lambda: self.onclick("9"), style='custom.TButton')
        self.nine.grid(row=1, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
        self.mul = ttk.Button(self.buttonFrame, text="x", command=lambda: self.onclick("*"), style='custom.TButton')
        self.mul.grid(row=1, column=3, sticky=tk.W + tk.E + tk.N + tk.S)

        # ROW - 2
        self.four = ttk.Button(self.buttonFrame, text="4", command=lambda: self.onclick("4"), style='custom.TButton')
        self.four.grid(row=2, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.five = ttk.Button(self.buttonFrame, text="5", command=lambda: self.onclick("5"), style='custom.TButton')
        self.five.grid(row=2, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.six = ttk.Button(self.buttonFrame, text="6", command=lambda: self.onclick("6"), style='custom.TButton')
        self.six.grid(row=2, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
        self.minus = ttk.Button(self.buttonFrame, text="-", command=lambda: self.onclick("-"), style='custom.TButton')
        self.minus.grid(row=2, column=3, sticky=tk.W + tk.E + tk.N + tk.S)

        # ROW - 3
        self.one = ttk.Button(self.buttonFrame, text="1", command=lambda: self.onclick("1"), style='custom.TButton')
        self.one.grid(row=3, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.two = ttk.Button(self.buttonFrame, text="2", command=lambda: self.onclick("2"), style='custom.TButton')
        self.two.grid(row=3, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.three = ttk.Button(self.buttonFrame, text="3", command=lambda: self.onclick("3"), style='custom.TButton')
        self.three.grid(row=3, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
        self.plus = ttk.Button(self.buttonFrame, text="+", command=lambda: self.onclick("+"), style='custom.TButton')
        self.plus.grid(row=3, column=3, sticky=tk.W + tk.E + tk.N + tk.S)

        # ROW - 4
        self.Dzero = ttk.Button(self.buttonFrame, text="00", command=lambda: self.onclick("00"), style='custom.TButton')
        self.Dzero.grid(row=4, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.zero = ttk.Button(self.buttonFrame, text="0", command=lambda: self.onclick("0"), style='custom.TButton')
        self.zero.grid(row=4, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.dot = ttk.Button(self.buttonFrame, text=".", command=lambda: self.onclick("."), style='custom.TButton')
        self.dot.grid(row=4, column=2, sticky=tk.W + tk.E + tk.N + tk.S)
        self.equal = ttk.Button(self.buttonFrame, text="=", command=lambda: self.onclick("="), style='custom.TButton')
        self.equal.grid(row=4, column=3, sticky=tk.W + tk.E + tk.N + tk.S)

        self.root.mainloop()

    def onclick(self, text):
        if text == "=":
            try:
                self.expression = str(eval(self.expression))
                self.input_state.set(self.expression)
                self.expression = ""
            except:
                self.input_state.set("Error")
        elif text == "C":
            self.expression = ""
            self.input_state.set("")
        elif text == "Del":
            self.expression = self.expression[:-1]
            self.input_state.set(self.expression)
        else:
            self.expression += text
            self.input_state.set(self.expression)


if __name__ == "__main__":
    myApp()
