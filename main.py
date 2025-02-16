import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()
        
        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=30, borderwidth=4)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]
        
        row = 0
        col = 0
        
        for button in buttons:
            if button == '=':
                btn = tk.Button(self.buttons_frame, text=button, fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self.evaluate())
            elif button == 'C':
                btn = tk.Button(self.buttons_frame, text=button, fg='black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self.clear())
            else:
                btn = tk.Button(self.buttons_frame, text=button, fg='black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda x=button: self.click(x))
            
            btn.grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)
    
    def clear(self):
        self.expression = ""
        self.input_text.set("")
    
    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()