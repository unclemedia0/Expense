#GUIExpense.py

from tkinter import *
from tkinter import ttk
#########CSV##########
import csv
#Comma-separated values: CSV

###########WritetoCSV - for Expense #############
def WritetoCSV(ep):
	with open('allexpense.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) 
		fw.writerow(ep)
	print('Done!')


def ReadCSV():
	with open('allexpense.csv',newline='',encoding='utf-8') as file:
		#fr = file reader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data


###########WritetoCSV2 - for Income #############
def WritetoCSV2(ep):
	with open('allincome.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) 
		fw.writerow(ep)
	print('Done!')


def ReadCSV2():
	with open('allincome.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		data = list(fr)
	return data


########MAIN GUI########
GUI = Tk() 
GUI.title('ໂປຣເເກຣມບັນທຶກຄ່າໃຊ້ຈ່າຍ')

w = 1000
h = 900

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}') #ปรับขนาด
GUI.iconbitmap('wallet.ico')


########FONT#########
s = ttk.Style()
s.configure('my.TButton',font=('Phetsarath OT',20,'bold'))


menubar = Menu(GUI)
GUI.config(menu=menubar)
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Exit - (F4)',command=GUI.quit)
#command= lambda: GUI.destroy()
GUI.bind('<F4>',lambda x: GUI.destroy())
## helpmenu

import webbrowser

def About():
	url = 'https://www.facebook.com/Unclemedia0'
	webbrowser.open(url)
from tkinter import messagebox as msb
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)
helpmenu.add_command(label='Donate',command=lambda: msb.showinfo('Donate','ເລກບັນຊີ: 109 0 77222 7\nธนาคารกรุงเทพ'))



from tkinter.ttk import Notebook
Tab = Notebook(GUI)
Tab.pack(fill=BOTH, expand=1)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

icon_expense = PhotoImage(file='cart.png')
icon_income = PhotoImage(file='money.png')
icon_dashboard = PhotoImage(file='dashboard.png')

Tab.add(T1,text='ລາຍຈ່າຍ',image=icon_expense,compound='top')
Tab.add(T2,text='ລາຍຮັບ',image=icon_income,compound='top')
Tab.add(T3,text='ສະຫຼຸບຜົນ',image=icon_dashboard,compound='top')


#################################################

G = Canvas(T3,width=400,height=300)
G.place(x=200,y=230)
def UpdateGraph(expense=100,income=200):
	if income >= expense:
		ep = int((expense / income) * 300)
		ic = 298
	else:
		ic = int((income / expense) * 300)
		ep = 298
	start_y = 300
	total = 300
	print('income', ic)
	print('expense', ep)
	hb1 = ep
	hb2 = ic
	hb3 = hb2 - hb1
	G.delete(ALL)
	b1 = G.create_rectangle(50,total - hb1,100,start_y,fill='orange')
	b2 = G.create_rectangle(150,total - hb2,200,start_y,fill='green')
	b3 = G.create_rectangle(250,total - hb3,300,start_y,fill='blue')

L = Label(T3,text='ລາຍຈ່າຍ').place(x=250,y=540)
L = Label(T3,text='ລາຍຮັບ').place(x=350,y=540)
L = Label(T3,text='ຄົງເລືອກ').place(x=450,y=540)

####################Expense######################

FONT1 = ('Phetsarath OT',20)
FONT2 = ('Phetsarath OT',20,'bold')
FONT3 = ('Phetsarath OT',30,'bold')
v_expense = StringVar()

L = Label(T1,text='ກະລຸນາກອຂໍ້ມູນລາຍການຈ່າຍ',font=FONT1).pack() 
E1 = Entry(T1,textvariable=v_expense, font=FONT1, width=30)
E1.pack(pady=10)

v_price = StringVar()

L = Label(T1,text='ຄ່າໃຊ້ຈ່າຍ (ບາທ)',font=FONT1).pack() 
E2 = Entry(T1,textvariable=v_price, font=FONT1, width=30)
E2.pack(pady=10)

from datetime import datetime #เวลา
def SaveExpense(event=None):
	exp = v_expense.get()
	pc = float(v_price.get()) 
	print('ລາຍການ: ',exp) 
	v_result.set(f'ກຳລັງບັນທືກລາຍກັນ: {exp} ລາຄາ: {pc:,.2f} ບາທ')
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	data = [dt,exp,pc] 
	WritetoCSV(data)
	#reset ตัวแปร
	v_expense.set('')
	v_price.set('')
	E1.focus()
	update_table() 
E2.bind('<Return>',SaveExpense) 

B1 = ttk.Button(T1,text='ບັນທືກ',command=SaveExpense, style='my.TButton')
B1.pack(ipadx=20,ipady=10)

#######LABEL########
v_result = StringVar()
R1 = ttk.Label(T1, textvariable= v_result, font=FONT2, foreground='green') 
R1.pack(pady=20)

########Expense Button##########

expenselist = {'breakfast':{'name':'ຄ່າອາຫານເຊົ້າ','price':20},
			   'afternoon':{'name':'ຄ່າອາຫານບ່າຍ','price':25},
			   'dinner':{'name':'ຄ່າອາຫານຄໍ່າ','price':35}}


###########FUNCTION########
def Expense(keyword):
	price = expenselist[keyword]['price']
	print('ຄ່າໃຊ້ຈ່າຍ: ' + expenselist[keyword]['name'])
	print('ລາຄາ: ',price)
	ep = expenselist[keyword]['name']
	v_expense.set(ep)
	v_price.set(price)

###########ROW1############

F1 = Frame(T1)
F1.pack()
B1 = ttk.Button(F1,text='ຄ່າອາຫານເຊົ້າ',command=lambda x='breakfast': Expense(x), style='my.TButton')
B1.grid(row=0,column=0,ipadx=20,ipady=10,padx=5)
B2 = ttk.Button(F1,text='ຄ່າອາຫານບ່າຍ',command=lambda x='afternoon': Expense(x), style='my.TButton')
B2.grid(row=0,column=1,ipadx=20,ipady=10,padx=5)
B3 = ttk.Button(F1,text='ຄ່າອາຫານຄໍ່າ',command=lambda x='dinner': Expense(x), style='my.TButton')
B3.grid(row=0,column=2,ipadx=20,ipady=10,padx=5)


#########TABLE###########

header = ['ວັນ-ເວລາ','ລາຍການ','ຈຳນວນເງີນ']
table_expense = ttk.Treeview(T1,column=header,show='headings',height=20)
table_expense.pack(pady=20)
table_expense.heading('ວັນ-ເວລາ',text='ວັນ-ເວລາ')
table_expense.heading('ລາຍການ',text='ລາຍການ')
table_expense.heading('ຈຳນວນເງີນ',text='ຈຳນວນເງີນ')
sum_expense = 0
sum_income = 0
sum_remaining = 0


def remaining():
	global sum_remaining
	cal = sum_income - sum_expense
	sum_remaining = float(cal)
	v_remaining.set('{:,.2f} ບາທ'.format(sum_remaining))
	UpdateGraph(sum_expense,sum_income)


def sum_table():
	global sum_expense
	allsum = []
	data = ReadCSV()
	for dt in data:
		allsum.append(float(dt[2]))
	v_allexpense.set('{:,.2f} ບາທ'.format(sum(allsum)))
	sum_expense = sum(allsum)


def sum_table2():
	global sum_income
	allsum = []
	data = ReadCSV2()
	for dt in data:
		allsum.append(float(dt[2]))
	v_allincome.set('{:,.2f} ບາທ'.format(sum(allsum)))
	sum_income = sum(allsum)


def update_table():
	data = ReadCSV()
	print(data)
	table_expense.delete(*table_expense.get_children()) 
	for dt in data:
		table_expense.insert('','end',value=dt)
	sum_table()
	remaining()


def update_table2():
	data = ReadCSV2()
	print(data)
	table_income.delete(*table_income.get_children()) 

	for dt in data:
		table_income.insert('','end',value=dt)
	sum_table2()
	remaining()

############TAB2##############
v_income = StringVar()
L = Label(T2,text='ກະລຸນາກອກລາຍຮັບ',font=FONT1).pack()
E21 = Entry(T2,textvariable=v_income, font=FONT1, width=30)
E21.pack(pady=10)
v_incomequan = StringVar() 
L = Label(T2,text='ລາຍຮັບ (ບາທ)',font=FONT1).pack()
E22 = Entry(T2,textvariable=v_incomequan, font=FONT1, width=30)
E22.pack(pady=10)


def SaveIncome(event=None):
	print('ບັນທືກລາຍຮັບ')
	incm = v_income.get()
	incmq = float(v_incomequan.get())
	print('ລາຍການ:', incm)
	print('ຈຳນວນເງີນ', incmq)
	print('---------')
	v_result2.set(f'ກຳລັງບັນທືກລາຍການ: {incm} ຈຳນວນເງີນ: {incmq:,.2f} ບາທ')
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	data = [dt,incm,incmq] 
	WritetoCSV2(data) 
	v_income.set('')
	v_incomequan.set('')
	E21.focus()
	update_table2()
E22.bind('<Return>',SaveIncome) 
B21 = ttk.Button(T2,text='ບັນທືກ',command=SaveIncome, style='my.TButton')
B21.pack(ipadx=20,ipady=10)
v_result2 = StringVar()
R2 = ttk.Label(T2, textvariable= v_result2, font=FONT2, foreground='green') 
R2.pack(pady=20)
header = ['ວັນ-ເວລາ','ລາຍການ','ຈຳນວນເງີນ']
table_income = ttk.Treeview(T2,column=header,show='headings',height=6)
table_income.pack(pady=20)

table_income.heading('ວັນ-ເວລາ',text='ວັນ-ເວລາ')
table_income.heading('ລາຍການ',text='ລາຍການ')
table_income.heading('ຈຳນວນເງີນ',text='ຈຳນວນເງີນ')

############TAB3##############

v_allexpense = StringVar()
L = Label(T3,text='ຢອດຄ່າໃຊ້ຈ່າຍທັ້ງໝົດ ==>',font=FONT3,foreground='orange').place(x=50,y=50)
LR1 = Label(T3,textvariable=v_allexpense,font=FONT3,foreground='orange')
LR1.place(x=400,y=50)
v_allincome = StringVar()
L = Label(T3,text='ຢອດລາຍຮັບທັ້ງໝົດ ==>',font=FONT3,foreground='green').place(x=50,y=100)
LR2 = Label(T3,textvariable=v_allincome,font=FONT3,foreground='green')
LR2.place(x=400,y=100)
v_remaining = StringVar()
L = Label(T3,text='ຄົງເລືອກທັ້ງໝົດ ==>',font=FONT3,foreground='blue').place(x=50,y=150)
LR2 = Label(T3,textvariable=v_remaining,font=FONT3,foreground='blue')
LR2.place(x=400,y=150)
try:
	update_table()
	update_table2()
except:
	print('ERROR')
GUI.mainloop()

