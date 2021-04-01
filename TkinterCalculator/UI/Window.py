import tkinter as tk


class Window:
    def __init__(self, root):
        self.root = root

        self.result = 0
        self.mem = 0
        self.operation = None

        self.root.title("Calculator")
        self.root.geometry("305x460")

        self.entry = tk.Entry(root, justify=tk.RIGHT, width=45, borderwidth=7)
        self.entry.insert(0, 0)
        self.entry.config(state=tk.DISABLED)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

        self.seven = tk.Button(self.root, text="7", padx=40, pady=20, command=self.press_7)
        self.seven.grid(row=1, column=0)

        self.eight = tk.Button(self.root, text="8", padx=40, pady=20, command=self.press_8)
        self.eight.grid(row=1, column=1)

        self.nine = tk.Button(self.root, text="9", padx=40, pady=20, command=self.press_9)
        self.nine.grid(row=1, column=2)

        self.four = tk.Button(self.root, text="4", padx=40, pady=20, command=self.press_4)
        self.four.grid(row=2, column=0)

        self.five = tk.Button(self.root, text="5", padx=40, pady=20, command=self.press_5)
        self.five.grid(row=2, column=1)

        self.six = tk.Button(self.root, text="6", padx=40, pady=20, command=self.press_6)
        self.six.grid(row=2, column=2)

        self.one = tk.Button(self.root, text="1", padx=40, pady=20, command=self.press_1)
        self.one.grid(row=3, column=0)

        self.two = tk.Button(self.root, text="2", padx=40, pady=20, command=self.press_2)
        self.two.grid(row=3, column=1)

        self.tree = tk.Button(self.root, text="3", padx=40, pady=20, command=self.press_3)
        self.tree.grid(row=3, column=2)

        self.zero = tk.Button(self.root, text="0", padx=40, pady=20, command=self.press_0)
        self.zero.grid(row=4, column=0)

        self.dot = tk.Button(self.root, text=".", padx=40, pady=20, command=self.press_dot)
        self.dot.grid(row=6, column=0)

        self.equal = tk.Button(self.root, text="=", padx=40, pady=20, command=self.press_equal)
        self.equal.grid(row=6, column=2)

        self.plus = tk.Button(self.root, text="+", padx=40, pady=20, command=self.press_plus)
        self.plus.grid(row=5, column=0)

        self.minus = tk.Button(self.root, text="-", padx=40, pady=20, command=self.press_minus)
        self.minus.grid(row=5, column=1)

        self.square = tk.Button(self.root, text="^", padx=40, pady=20)
        self.square.grid(row=6, column=1)

        self.multiply = tk.Button(self.root, text="x", padx=40, pady=20, command=self.press_multiply)
        self.multiply.grid(row=4, column=1)

        self.divide = tk.Button(self.root, text="/", padx=40, pady=20)
        self.divide.grid(row=4, column=2)

        self.back = tk.Button(self.root, text="<", padx=40, pady=20, command=self.press_back)
        self.back.grid(row=5, column=2)

    def press_plus(self):
        self.entry.config(state=tk.NORMAL)
        self.mem = self.result
        self.result = 0
        self.operation = "+"
        self.entry.config(state=tk.DISABLED)

    def press_minus(self):
        self.entry.config(state=tk.NORMAL)
        self.mem = self.result
        self.result = 0
        self.operation = "-"
        self.entry.config(state=tk.DISABLED)

    def press_multiply(self):
        self.entry.config(state=tk.NORMAL)
        self.mem = self.result
        self.result = 0
        self.operation = "*"
        self.entry.config(state=tk.DISABLED)

    def press_dot(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = str(self.result) + ".0"
        self.result = float(self.result)
        self.entry.insert(0, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_equal(self):
        self.entry.config(state=tk.NORMAL)
        if self.operation == "+":
            self.entry.delete(0, tk.END)
            self.result += self.mem
            self.operation = None
            self.entry.insert(0, self.result)
        elif self.operation == "-":
            self.entry.delete(0, tk.END)
            self.result = self.mem - self.result
            self.operation = None
            self.entry.insert(0, self.result)
        elif self.operation == "*":
            self.entry.delete(0, tk.END)
            self.result = self.mem * self.result
            self.operation = None
            self.entry.insert(0, self.result)
        elif self.operation == "/":
            self.entry.delete(0, tk.END)
            self.result /= self.mem
            self.operation = None
            self.entry.insert(0, self.result)
            self.mem = 0
        self.entry.config(state=tk.DISABLED)

    def press_back(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result // 10
        self.entry.insert(0, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_0(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_1(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 1
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_2(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 2
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_3(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 3
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_4(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 4
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_5(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 5
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_6(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 6
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_7(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 7
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_8(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 8
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)

    def press_9(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.result = self.result * 10 + 9
        self.entry.insert(tk.END, self.result)
        self.entry.config(state=tk.DISABLED)
