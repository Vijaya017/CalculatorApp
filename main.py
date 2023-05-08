import tkinter as tk
from tkinter import ttk


class myApp:
    def __init__(self):
        self.expression=""
        self.root=tk.Tk()
        self.root.geometry("400x550")
        self.root.title("Calculator-Let's Compute!")
        self.root.resizable(False,False)

        self.input_Frame=tk.Frame(self.root,width=400,height=50)
        self.input_Frame.pack(padx=10,pady=40)

        self.input_state=tk.StringVar()
        self.input=tk.Entry(self.input_Frame,textvariable=self.input_state,width=50,font=('Arial',20),justify=tk.RIGHT)
        self.input.grid(row=0,column=0)
        self.input.pack(ipady=20)


        self.buttonFrame=tk.Frame(self.root,width=400,height=300)
        self.buttonFrame.pack()

        #ROW - 0
        self.C=ttk.Button(self.buttonFrame,text="C",command=lambda:self.onclick("C"))
        self.C.grid(row=0,column=0)
        self.mod = ttk.Button(self.buttonFrame, text="%", command=lambda: self.onclick("%"))
        self.mod.grid(row=0, column=1)
        self.delete = ttk.Button(self.buttonFrame, text="Del", command=lambda: self.onclick("Del"))
        self.delete.grid(row=0, column=2)
        self.div = ttk.Button(self.buttonFrame, text="/", command=lambda: self.onclick("/"))
        self.div.grid(row=0, column=3)

        # ROW - 1
        self.seven = ttk.Button(self.buttonFrame, text="7", command=lambda: self.onclick("7"))
        self.seven.grid(row=1, column=0)
        self.eight = ttk.Button(self.buttonFrame, text="8", command=lambda: self.onclick("8"))
        self.eight.grid(row=1, column=1)
        self.nine = ttk.Button(self.buttonFrame, text="9", command=lambda: self.onclick("9"))
        self.nine.grid(row=1, column=2)
        self.mul = ttk.Button(self.buttonFrame, text="x", command=lambda: self.onclick("*"))
        self.mul.grid(row=1, column=3)

        # ROW - 2
        self.four = ttk.Button(self.buttonFrame, text="4", command=lambda: self.onclick("4"))
        self.four.grid(row=2, column=0)
        self.five = ttk.Button(self.buttonFrame, text="5", command=lambda: self.onclick("5"))
        self.five.grid(row=2, column=1)
        self.six = ttk.Button(self.buttonFrame, text="6", command=lambda: self.onclick("6"))
        self.six.grid(row=2, column=2)
        self.minus = ttk.Button(self.buttonFrame, text="-", command=lambda: self.onclick("-"))
        self.minus.grid(row=2, column=3)

        # ROW - 3
        self.one = ttk.Button(self.buttonFrame, text="1", command=lambda: self.onclick("1"))
        self.one.grid(row=3, column=0)
        self.two = ttk.Button(self.buttonFrame, text="2", command=lambda: self.onclick("2"))
        self.two.grid(row=3, column=1)
        self.three = ttk.Button(self.buttonFrame, text="3", command=lambda: self.onclick("3"))
        self.three.grid(row=3, column=2)
        self.plus = ttk.Button(self.buttonFrame, text="+", command=lambda: self.onclick("+"))
        self.plus.grid(row=3, column=3)

        # ROW - 4
        self.Dzero = ttk.Button(self.buttonFrame, text="00", command=lambda: self.onclick("00"))
        self.Dzero.grid(row=4, column=0)
        self.zero = ttk.Button(self.buttonFrame, text="0", command=lambda: self.onclick("0"))
        self.zero.grid(row=4, column=1)
        self.dot = ttk.Button(self.buttonFrame, text=".", command=lambda: self.onclick("."))
        self.dot.grid(row=4, column=2)
        self.equal = ttk.Button(self.buttonFrame, text="=", command=lambda: self.onclick("="))
        self.equal.grid(row=4, column=3)






        self.root.mainloop()


    def onclick(self,text):
        if text == "=":
            try:
                self.expression = str(eval(self.expression))
                self.input_state.set(self.expression)
                self.expression = ""
            except:
                self.input_state.set("Error")
        elif text == "C":
            self.expression=""
            self.input_state.set("")
        elif text == "Del":
            self.expression=self.expression[:-1]
            self.input_state.set(self.expression)
        else:
            self.expression+=text
            self.input_state.set(self.expression)




if __name__=="__main__":
    myApp()