import tkinter as tk
from fpdf import FPDF

pdf=FPDF(format='A4')
pdf.add_page()
pdf.set_font("Arial",size=10)
master=tk.Tk()
master.title('Electricity consumption')
tk.Label(master,text='ELECTRICITY CONSUMPTION',height=4).grid(row=1)
tk.Label(master,text='Lecture hall/Room no:',height=2).grid(row=2)
e1=tk.Entry(master,width=10)
e1.grid(row=2,column=1)
tk.Label(master,text='No.of fans:',height=2).grid(row=3)
e2=tk.Entry(master,width=10)
e2.grid(row=3,column=1)
tk.Label(master,text='Hours used per day:',height=2).grid(row=4)
sb1=tk.Spinbox(master,from_=0,to=24,width=10)
sb1.grid(row=4,column=1)
tk.Label(master,text='No.of lights:',height=2).grid(row=5)
e3=tk.Entry(master,width=10)
e3.grid(row=5,column=1)
tk.Label(master,text='Hours used per day:',height=2).grid(row=6)
sb2=tk.Spinbox(master,from_=0,to=24,width=10)
sb2.grid(row=6,column=1)
tk.Label(master,text='No.of projector:',height=2).grid(row=7)
e4=tk.Entry(master,width=10)
e4.grid(row=7,column=1)
tk.Label(master,text='Hours used per day:',height=2).grid(row=8)
sb3=tk.Spinbox(master,from_=0,to=24,width=10)
sb3.grid(row=8,column=1)

def calculate():
    watt=[75,25,300]
    app=[]
    hour=[]
    unit=0
    lec_no=0
    tot=0
    lec_no=e1.get()
    app.append(int(e2.get()))
    app.append(int(e3.get()))
    app.append(int(e4.get()))
    hour.append(int(sb1.get()))
    hour.append(int(sb2.get()))
    hour.append(int(sb3.get()))
    i=0
    while i < len(app) :
        tot=tot+(app[i]*hour[i]*watt[i])
        unit=int(tot)/1000
        i=i+1
    pdf.multi_cell(0,4,('ELECTRICITY CONSUMPTION'))
    pdf.ln()
    pdf.multi_cell(100,8,('Lecture hall/Room no : %s'%lec_no))
    pdf.multi_cell(100,6,('%s watt per day'%tot))
    pdf.multi_cell(100,6,('%s unit per day'%unit))
    pdf.multi_cell(100,6,('%s watt per month'%(tot*30)))
    pdf.multi_cell(100,6,('%s unit per month'%(unit*30)))
    pdf.output("Electricity consumption.pdf")
    master.destroy()
    top=tk.Tk()
    top.title('Message')
    top.geometry('300x100')
    message='OUTPUT IS GENERATED AS PDF'
    m=tk.Message(top,text=message,width=100,bg='lightgreen')
    m.pack()
    top.mainloop()
    

b=tk.Button(master,text='CALCULATE',command=calculate,height=2).grid(row=9,column=1)

master.mainloop()
