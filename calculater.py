from tkinter import *

class gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("calculater")
        self.list = [[1,2,3],[4,5,6],[7,8,9]]
        self.var = StringVar()

    def click(self,write,val):
        if not write:
            if val== "=" and self.entry.get():
                try:
                    res = str(eval(self.entry.get()))
                    self.entry.delete(0,END)
                    self.entry.insert(END,res)
                except Exception as e:
                    import tkinter.messagebox as msgbox
                    msgbox.showerror("Wrong Input","Couldn't calculate the answer, Please check your input")

            elif val=="C":
                self.entry.delete(0,END)
            else:
                self.entry.delete(len(self.entry.get())-1,len(self.entry.get()))

        else:
            self.insert_val(val)



    def draw_wid(self):
        self.entry = Entry(self,textvariable= self.var,relief=SUNKEN,borderwidth=2,width=25)
        self.entry.grid(row=0,column=0,columnspan=5)
        b9 =  self.make_btn("9")
        b8 =  self.make_btn("8")
        b7 =  self.make_btn("7")
        b6 =  self.make_btn("6")
        b5 =  self.make_btn("5")
        b4 =  self.make_btn("4")
        b3 =  self.make_btn("3")
        b2 =  self.make_btn("2")
        b1 =  self.make_btn("1")
        b0 =  self.make_btn("0")
        bp =  self.make_btn("+")
        bs =  self.make_btn("-")
        bd =  self.make_btn("/")
        bm =  self.make_btn("*")
        bcl =  self.make_btn("C",False)
        bdot =  self.make_btn(".")
        beq =  self.make_btn("=",False,17)
        bback =  self.make_btn("<-",False)

        # btn_list = [b{i} for i in range(1,10)]
        btn_list = [b1,b2,b3,bcl,b4,b5,b6,bback,b7,b8,b9,bd,bdot,b0,bs,bm,beq,bp]
        count = 0
        for row in range(1,5):
            for col in range(4):
                btn_list[count].grid(row=row,column=col)
                count+=1
        btn_list[-2].grid(row=5,column=0,columnspan=3)
        btn_list[-1].grid(row=5,column=3)



    def make_btn(self,val,write=True,width=2):
        return Button(self,text=val,command=lambda:self.click(write,val),width=width,relief=SUNKEN,borderwidth=3)

    def insert_val(self,val):
        text = self.entry.get()
        self.entry.insert(END,val)
        text+= val




            
if __name__ == '__main__':
    win = gui()
    win.draw_wid()



    win.mainloop()