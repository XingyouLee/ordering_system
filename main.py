from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox

Order_Sys = Tk()
Order_Sys.geometry("1550x700")
Order_Sys.resizable(0, 0)
Order_Sys.title("Online Ordering Systems")
Order_Sys.configure(background='sky blue')

def Exit():
    qExit = messagebox.askyesno("Billing System", "Do you want to exit the system")
    if qExit > 0:
        Order_Sys.destroy()

def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofWhiteWine.set(0)
    CostofRedWine.set(0)
    CostofOtherWine.set(0)
    CostofDeliver.set(0)
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    TimeofOrder.set("")
    DateofOrder.set("")
    Discount.set(0)
    UnitPriceOtherWine.set(0)
    UnitPriceRedWine.set(0)
    UnitPriceWhiteWine.set(0)
    QtyOtherWine.set(0)
    QtyRedWine.set(0)
    QtyWhiteWine.set(0)
    CustomerRef.set("")

def OrderReference():
    x = random.randint(10000, 700000)
    randomRef = str(x)
    CustomerRef.set("PR" + randomRef)

def Total():
    Qty1 = float(QtyWhiteWine.get())
    Qty2 = float(QtyRedWine.get())
    Qty3 = float(QtyOtherWine.get())

    discount = float(Discount.get()) / 100
    if float(Discount.get()) > 100:
        messagebox.showinfo("Error", "you gave too much rebate!")
        discount = 0

    UnitPrice1 = float(UnitPriceWhiteWine.get())
    UnitPrice2 = float(UnitPriceRedWine.get())
    UnitPrice3 = float(UnitPriceOtherWine.get())

    CostofWine1 = str(format(Qty1 * UnitPrice1, '.2f'))
    CostofWine2 = str(format(Qty2 * UnitPrice2, '.2f'))
    CostofWine3 = str(format(Qty3 * UnitPrice3, '.2f'))

    CostofWhiteWine.set(CostofWine1)
    CostofRedWine.set(CostofWine2)
    CostofOtherWine.set(CostofWine3)

    AllCost = (float(CostofWine1) + float(CostofWine2) + float(CostofWine3)) - (float(CostofWine1) + float(CostofWine2) + float(CostofWine3)) * discount
    num = format(((AllCost)*0.02), '.2f')
    TaxAll = "pln", str(num)
    Tax.set(TaxAll)

    SubTotalp = "pln", str(format(((AllCost)), '.2f'))
    SubTotal.set(SubTotalp)

    TotalCostp = "pln", str(format(AllCost + (AllCost)*0.02, '.2f'))
    TotalCost.set(TotalCostp)
    return

CustomerRef = StringVar()
Tax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofWhiteWine = StringVar()
CostofRedWine = StringVar()
CostofOtherWine = StringVar()
CostofDeliver = StringVar()
CustomerName = StringVar()
CustomerPhone = StringVar()
CustomerEmail = StringVar()
TimeofOrder = StringVar()
DateofOrder = StringVar()
Discount = StringVar()
UnitPriceOtherWine = StringVar()
UnitPriceRedWine = StringVar()
UnitPriceWhiteWine = StringVar()
QtyOtherWine = StringVar()
QtyRedWine = StringVar()
QtyWhiteWine = StringVar()
CustomerRef = StringVar()

CostofWhiteWine.set(0)
CostofRedWine.set(0)
CostofOtherWine.set(0)
CostofDeliver.set(0)
Discount.set(0)
UnitPriceOtherWine.set(0)
UnitPriceRedWine.set(0)
UnitPriceWhiteWine.set(0)
QtyOtherWine.set(0)
QtyRedWine.set(0)
QtyWhiteWine.set(0)
TimeofOrder.set(time.strftime("%H:%M:%S"))
DateofOrder.set(time.strftime("%d-%m-%Y"))




Tops = Frame(Order_Sys, width=1550, height=50, bd=16, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(Order_Sys, width=700, height=650, bd=16, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(Order_Sys, width=440, height=650, bd=16, relief="raise")
f2.pack(side=RIGHT)

Tops.configure(background='powder blue')
f1.configure(background='powder blue')
f2.configure(background='powder blue')

#---f1
f1a = Frame(f1, width=700, height=100, bd=8, relief="raise")
f1a.pack(side=TOP)

f1b = Frame(f1, width=700, height=400, bd=8, relief="raise")
f1b.pack(side=BOTTOM)

#---f2
f2a = Frame(f2, width=600, height=200, bd=8, relief="raise")
f2a.pack(side=TOP)

f2b = Frame(f2, width=300, height=400, bd=8, relief="raise")
f2b.pack(side=LEFT)

f2c = Frame(f2, width=300, height=400, bd=8, relief="raise")
f2c.pack(side=RIGHT)

#---Tops

lblInfo = Label(Tops, font=('arial', 52, 'bold'), text="                Online Ordering Systems                  ",
                bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

#---f1a

lblCustomerName = Label(f1a, font=('arial', 16, 'bold'), text="Customer Name",
                fg='black', bd=10, anchor='w')
lblCustomerName.grid(row=0, column=0)

txtCustomerName = Entry(f1a, font=('arial', 12, 'bold'), textvariable=CustomerName,
               bd=20, width=50, bg='white', justify='left')
txtCustomerName.grid(row=0, column=1)

lblCustomerPhone = Label(f1a, font=('arial', 16, 'bold'), text="Customer Phone",
                fg='black', bd=10, anchor='w')
lblCustomerPhone.grid(row=1, column=0)

txtCustomerPhone = Entry(f1a, font=('arial', 12, 'bold'), textvariable=CustomerPhone,
               bd=20, width=50, bg='white', justify='left')
txtCustomerPhone.grid(row=1, column=1)

lblCustomerEmail = Label(f1a, font=('arial', 16, 'bold'), text="Customer Email",
                fg='black', bd=10, anchor='w')
lblCustomerEmail.grid(row=2, column=0)

txtCustomerEmail = Entry(f1a, font=('arial', 12, 'bold'), textvariable=CustomerEmail,
               bd=20, width=50, bg='white', justify='left')
txtCustomerEmail.grid(row=2, column=1)

#---f1b

lblItemOrder = Label(f1b, font=('arial', 16, 'bold'), text="Item Order",
                fg='black', bd=20)
lblItemOrder.grid(row=0, column=0)
lblQty = Label(f1b, font=('arial', 16, 'bold'), text="Qty",
                fg='black', bd=20)
lblQty.grid(row=0, column=1)
lblUnitPrice = Label(f1b, font=('arial', 16, 'bold'), text="Unit Price",
                fg='black', bd=20)
lblUnitPrice.grid(row=0, column=2)
lblCostofItem = Label(f1b, font=('arial', 16, 'bold'), text="Cost of Item",
                fg='black', bd=20)
lblCostofItem.grid(row=0, column=3)
#---
lblWhiteWine = Label(f1b, font=('arial', 16, 'bold'), text="White Wine",
                fg='black', bd=20)
lblWhiteWine.grid(row=1, column=0)

txtWhiteWine = Entry(f1b, font=('arial', 12, 'bold'), textvariable=QtyWhiteWine,
               bd=20, width=16, bg='white', justify='left')
txtWhiteWine.grid(row=1, column=1)

lblRedWine = Label(f1b, font=('arial', 16, 'bold'), text="Red Wine",
                fg='black', bd=20)
lblRedWine.grid(row=2, column=0)

txtRedWine = Entry(f1b, font=('arial', 12, 'bold'), textvariable=QtyRedWine,
               bd=20, width=16, bg='white', justify='left')
txtRedWine.grid(row=2, column=1)

lblOtherWine = Label(f1b, font=('arial', 16, 'bold'), text="Other Wine",
                fg='black', bd=20)
lblOtherWine.grid(row=3, column=0)

txtOtherWin = Entry(f1b, font=('arial', 12, 'bold'), textvariable=QtyOtherWine,
               bd=20, width=16, bg='white', justify='left')
txtOtherWin.grid(row=3, column=1)
#---
txtUnitPriceWhiteWine = Entry(f1b, font=('arial', 12, 'bold'), textvariable=UnitPriceWhiteWine,
               bd=20, width=16, bg='white', justify='left')
txtUnitPriceWhiteWine.grid(row=1, column=2)

txtUnitPriceRedWine = Entry(f1b, font=('arial', 12, 'bold'), textvariable=UnitPriceRedWine,
               bd=20, width=16, bg='white', justify='left')
txtUnitPriceRedWine.grid(row=2, column=2)

txtUnitPriceOtherWin = Entry(f1b, font=('arial', 12, 'bold'), textvariable=UnitPriceOtherWine,
               bd=20, width=16, bg='white', justify='left')
txtUnitPriceOtherWin.grid(row=3, column=2)
#---
txtCostofWhiteWine = Entry(f1b, font=('arial', 12, 'bold'), textvariable=CostofWhiteWine,
               bd=20, width=16, bg='white', justify='left')
txtCostofWhiteWine.grid(row=1, column=3)

txtCostofRedWine = Entry(f1b, font=('arial', 12, 'bold'), textvariable=CostofRedWine,
               bd=20, width=16, bg='white', justify='left')
txtCostofRedWine.grid(row=2, column=3)

txtCostofOtherWine = Entry(f1b, font=('arial', 12, 'bold'), textvariable=CostofOtherWine,
               bd=20, width=16, bg='white', justify='left')
txtCostofOtherWine.grid(row=3, column=3)

#---f2c buttons

btnTotal = Button(f2c, padx=8, pady=13, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                        text="Total Cost", bg='white', command=Total).grid(row=0, column=0)

btnOrderRef = Button(f2c, padx=8, pady=13, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                        text="Order Reference", bg='white', command=OrderReference).grid(row=1, column=0)

btnReset = Button(f2c, padx =8, pady=13, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                        text="Reset", bg='white', command=Reset).grid(row=2, column=0)

btnExit = Button(f2c, padx =8, pady=13, bd=8, fg="black", font=('arial', 16, 'bold'), width=16,
                        text="Exit", bg='white', command=Exit).grid(row=3, column=0)
#---f2a

lblDateofOrder = Label(f2a, font=('arial', 16, 'bold'), text="Date of Order",
                fg='black', bd=10, anchor='w')
lblDateofOrder.grid(row=0, column=0)

txtDateofOrder = Entry(f2a, font=('arial', 12, 'bold'), textvariable=DateofOrder,
               bd=20, width=53, bg='white', justify='left')
txtDateofOrder.grid(row=0, column=1)

lblTimeofOrder = Label(f2a, font=('arial', 16, 'bold'), text="Time of Order",
                fg='black', bd=10, anchor='w')
lblTimeofOrder.grid(row=1, column=0)

txtTimeofOrder = Entry(f2a, font=('arial', 12, 'bold'), textvariable=TimeofOrder,
               bd=20, width=53, bg='white', justify='left')
txtTimeofOrder.grid(row=1, column=1)

lblCustomerRef = Label(f2a, font=('arial', 16, 'bold'), text="Customer Reference",
                fg='black', bd=10, anchor='w')
lblCustomerRef.grid(row=2, column=0)

txtCustomerRef = Entry(f2a, font=('arial', 12, 'bold'), textvariable=CustomerRef,
               bd=20, width=53, bg='white', justify='left')
txtCustomerRef.grid(row=2, column=1)


#---f2b

lblMethodOfPayment = Label(f2b, font=('arial', 16, 'bold'), text="Method of Payment",
                fg='black', bd=16, anchor='w')
lblMethodOfPayment.grid(row=0, column=0)

cmdMethodOfPayment = ttk.Combobox(f2b, font=('arial', 16, 'bold'))
cmdMethodOfPayment['value'] = (' ', 'Cash', 'Debit Card', 'Visa Card', 'Mater Card')
cmdMethodOfPayment.grid(row=0, column=1)

lblDiscount = Label(f2b, font=('arial', 16, 'bold'), text="Discount",
                 fg = 'black', bd=16, anchor='w')
lblDiscount.grid(row=1, column=0)

txtDiscount = Entry(f2b, font=('arial', 16, 'bold'), textvariable=Discount,
                 bd=16, width=18, bg='white', justify='left')
txtDiscount.grid(row=1, column=1)

lblTax = Label(f2b, font=('arial', 16, 'bold'), text="Tax",
               fg='black', bd=16, anchor='w')
lblTax.grid(row=2, column=0)

txtTax = Entry(f2b, font=('arial', 16, 'bold'), textvariable=Tax,
               bd=16, width=18, bg='white', justify='left')
txtTax.grid(row=2, column=1)

lblSubTotal = Label(f2b, font=('arial', 16, 'bold'), text="Sub Total",
                    fg='black', bd=16, anchor='w')
lblSubTotal.grid(row=3, column=0)

txtSubTotal = Entry(f2b, font=('arial', 16, 'bold'), textvariable=SubTotal,
                    bd=16, width=18, bg='white', justify='left')
txtSubTotal.grid(row=3, column=1)

lblTotalCost = Label(f2b, font=('arial', 16, 'bold'), text="Total Cost",
                    fg='black', bd=16, anchor='w')
lblTotalCost.grid(row=4, column=0)

txtTotalCost = Entry(f2b, font=('arial', 16, 'bold'), textvariable=TotalCost,
                    bd=16, width=18, bg='white', justify='left')
txtTotalCost.grid(row=4, column=1)

Order_Sys.mainloop()