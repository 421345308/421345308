from tkinter import *
from tkinter import ttk
import math

class Calculator:
    def __init__(self, master):
        # 创建主窗口
        self.master = master
        self.master.title("科学计算器")
        self.master.resizable(0, 0)
        self.master.geometry('400x440')  # 增加高度以容纳更多按钮

        # 创建样式
        self.style = ttk.Style()
        self.style.configure('TButton', padding=(10, 10), font=('Arial', 16))  # 调整按钮样式

        # 定义按钮样式
        self.style.configure('Digit.TButton', background='lightgray')  # 数字按钮的样式
        self.style.configure('Operator.TButton', background='orange')  # 运算符按钮的样式
        self.style.configure('Control.TButton', background='lightblue')  # 控制按钮的样式

        # 创建显示结果的文本框
        self.result = StringVar()
        self.equation = StringVar()
        self.result.set('')
        self.equation.set('0')

        self.show_result_eq = Label(self.master, bg='white', fg='black',
                                    font=('Arial', '20'), bd='0',
                                    textvariable=self.equation, anchor='se')
        self.show_result = Label(self.master, bg='white', fg='black',
                                 font=('Arial', '30'), bd='0',
                                 textvariable=self.result, anchor='se')

        # 定义按钮文本、回调函数和样式
        button_texts = [
            ('MC', self.clear, 'Control.TButton'),
            ('(', lambda: self.getNum('('), 'Operator.TButton'),
            (')', lambda: self.getNum(')'), 'Operator.TButton'),
            ('<-', self.back, 'Control.TButton'),  # 合并两个'<-'按钮
            ('π', lambda: self.insert_constant('π'), 'Operator.TButton'),
            ('e', lambda: self.insert_constant('e'), 'Operator.TButton'),
            ('log', lambda: self.insert_function('log('), 'Operator.TButton'),
            ('+', lambda: self.getNum('+'), 'Operator.TButton'),
            ('sin', lambda: self.insert_function('sin('), 'Operator.TButton'),
            ('7', lambda: self.getNum('7'), 'Digit.TButton'),
            ('8', lambda: self.getNum('8'), 'Digit.TButton'),
            ('9', lambda: self.getNum('9'), 'Digit.TButton'),
            ('-', lambda: self.getNum('-'), 'Operator.TButton'),
            ('cos', lambda: self.insert_function('cos('), 'Operator.TButton'),
            ('4', lambda: self.getNum('4'), 'Digit.TButton'),
            ('5', lambda: self.getNum('5'), 'Digit.TButton'),
            ('6', lambda: self.getNum('6'), 'Digit.TButton'),
            ('*', lambda: self.getNum('*'), 'Operator.TButton'),
            ('tan', lambda: self.insert_function('tan('), 'Operator.TButton'),
            ('1', lambda: self.getNum('1'), 'Digit.TButton'),
            ('2', lambda: self.getNum('2'), 'Digit.TButton'),
            ('3', lambda: self.getNum('3'), 'Digit.TButton'),
            ('÷', lambda: self.getNum('÷'), 'Operator.TButton'),
            ('=', self.run, 'Operator.TButton'),  # 合并两个'='按钮
            ('sqrt', lambda: self.insert_function('sqrt('), 'Operator.TButton'),
            ('0', lambda: self.getNum('0'), 'Digit.TButton'),
            ('.', lambda: self.getNum('.'), 'Operator.TButton'),
            ('^', lambda: self.getNum('^'), 'Operator.TButton'),
        ]

        # 布局按钮
        row, col = 2, 0
        for text, command, style in button_texts:
            if text == '=':
                button = ttk.Button(self.master, text=text, style=style, command=command)
                button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2, rowspan=2)
            elif text == '<-':
                button = ttk.Button(self.master, text=text, style=style, command=command)
                button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2, columnspan=2)
            else:
                button = ttk.Button(self.master, text=text, style=style, command=command)
                button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            if row == 2 and col ==3:
                col +=2
            else :
                col += 1
            if col > 4:
                col = 0
                row += 1

        # 设置网格权重，以便按钮可以根据窗口大小均匀分布
        for i in range(7):  # 增加一行以容纳更多按钮
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        # 放置结果显示文本框
        self.show_result_eq.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.show_result.grid(row=1, column=0, columnspan=5, sticky='nsew')

    def back(self):
        temp_equ = self.equation.get()
        self.equation.set(temp_equ[:-1])  # 删除最后一个字符

    def getNum(self, arg):
        temp_equ = self.equation.get()
        temp_result = self.result.get()

        # 判断基本语法错误
        if temp_result != ' ':  # 如果计算器之前没有结果，结果区域应该设置为空。
            self.result.set(' ')
        if temp_equ == '0' and (arg not in ['.', '+', '-', '*', '÷']):  # 如果首次输入为0，则后面不能是数字，只能是小数点或运算符
            temp_equ = ''
        if len(temp_equ) > 2 and temp_equ[-1] == '0':  # 运算符后面也不能出现0+数字的情况，如03，09，x
            if (temp_equ[-2] in ['+', '-', '*', '÷', '^']) and (
                    arg in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', 'π', 'e']):
                temp_equ = temp_equ[:-1]
        if arg in ['sin', 'cos', 'tan', 'sqrt', 'log']:
            temp_equ += arg + '('

        temp_equ += arg
        self.equation.set(temp_equ)

    def clear(self):
        self.equation.set('0')
        self.result.set(' ')

    def insert_constant(self, constant):
        if constant == 'π':
            constant_value = str(math.pi)
        elif constant == 'e':
            constant_value = str(math.e)
        else:
            constant_value = ''

        temp_equ = self.equation.get()
        if temp_equ == '0':
            temp_equ = ''
        temp_equ += constant
        self.equation.set(temp_equ)

    def insert_function(self, func):
        temp_equ = self.equation.get()
        if temp_equ == '0':
            temp_equ = ''
        temp_equ += func
        self.equation.set(temp_equ)

    def run(self):
        temp_equ = self.equation.get()
        temp_equ = temp_equ.replace('÷', '/')  # 将÷替换为/
        temp_equ = temp_equ.replace('^', '**')
        temp_equ = temp_equ.replace('π', str(math.pi))  # 将π替换为math.pi
        temp_equ = temp_equ.replace('e', str(math.e))  # 将e替换为math.e
        if temp_equ[0] in ['+', '-', '*', '÷', '^']:
            temp_equ = '0' + temp_equ

        # 检查表达式是否包含特殊函数
        special_functions = ['sin(', 'cos(', 'tan(', 'sqrt(', 'log(']
        if any(func in temp_equ for func in special_functions):
            try:
                # 使用 eval() 计算表达式，但先将特殊函数替换为 math 模块的计算函数
                for func in special_functions:
                    temp_equ = temp_equ.replace(func, 'math.' + func[:-1])  # 去掉函数名后的括号
                answer = '%.4f' % eval(temp_equ)
                self.result.set(str(answer))
            except (ZeroDivisionError, SyntaxError, ValueError):
                self.result.set(str('Error'))
        else:
            try:
                answer = '%.4f' % eval(temp_equ)
                self.result.set(str(answer))
            except (ZeroDivisionError, SyntaxError, ValueError):
                self.result.set(str('Error'))

if __name__ == "__main__":
    root = Tk()
    my_cal = Calculator(root)
    root.mainloop()
