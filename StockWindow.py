import AdidasStock
from Tkinter import *
import tkMessageBox

class StockWindow:

    def __init__(self):
        self.master = Tk()
        self.master.wm_title("pslifeisgood - Adidas Stock Checker")
        self.master.minsize(width=500, height=275)
        self.master.maxsize(width=500, height=275)
        self.v = StringVar()
        Label(self.master, textvariable=self.v).pack()
        self.e = Entry(self.master)
        self.e.pack()
        self.e.focus_set()
        self.b = Button(self.master, text="Pull Adidas Stock", width=15, command=self.callback)
        self.b.pack()
        self.result = Listbox(self.master)
        self.result.config(width=40)
        self.result.pack()
        mainloop()
        
        
    def callback(self):
        self.result.delete(0, END)
        _input = str(self.e.get())
        self.v.set("Working...")
        sku = _input
        stock = AdidasStock.AdidasStock('', sku)
        result = stock.getVarientStock(sku)
        self.formatStock(result)

    def formatStock(self, stock):
        toSet = ''
        if not 'error' in stock.keys():
            for size in stock.keys():
                if not size == 'total':
                    temp = 'Size ' + str(size) + ' : ' + str(int(stock[size])) + ' Available\n'
                    self.result.insert(END, temp)
            total = 'TOTAL STOCK : ' + str(stock['total'])
            self.result.insert(END, total)
        else:
            self.result.insert(END, 'Error: %s' % stock['error'])
        self.v.set('Finished')
        

StockWindow = StockWindow()
