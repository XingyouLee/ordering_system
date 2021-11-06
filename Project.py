import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import tkinter.messagebox
import items
from PIL.Image import composite
import csv
import numpy as np
import pandas as pd
import time


class Item(object):

    def __init__(self, name, price, water, coco, milk, sugar, cheese):
        self.name = name
        self.price = price
        self.water = water
        self.coco = coco
        self.milk = milk
        self.sugar = sugar
        self.cheese = cheese


class Storage(object):

    def __init__(self, water, coco, milk, sugar, cheese):
        self.water = water
        self.coco = coco
        self.milk = milk
        self.sugar = sugar
        self.cheese = cheese


def check_info():
    item_data = pd.read_csv('items_category.csv')
    item_menu = []
    item_data = np.array(item_data)

    # for row in f_csv:
    #     print(np.size(row))
    for i in item_data:
        # item_menu.append(Item(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5]), int(i[6])))
        item_menu.append(Item(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    storage_data = pd.read_csv('material_storage.csv')

    data = np.array(storage_data)

    storage = Storage(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4])

    return item_data, item_menu, storage


# Americano = Item("Americano", 10, 3, 1, 0, 0, 0)  # name, price, water, coco, milk, sugar, cheese
# 
# Cappuccino = Item("Cappuccino", 15, 3, 1, 1, 1, 1)
# 
# item_menu = [Americano, Cappuccino]
def update_storage(storage):
    headers = ["water", "coco", "milk", "sugar", "cheese"]

    rows = [[storage.water, storage.coco, storage.milk, storage.sugar, storage.cheese]]

    with open('material_storage.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def imagemaker(path, sizex, sizey):
    im = Image.open(path)
    im = im.resize((sizex, sizey))
    return ImageTk.PhotoImage(im)


login_status = 0


def login_info():
    def login_confirm():
        tkinter.messagebox.showinfo(title='Hi', message='Login successfully')
        login_status = 1

        top.destroy()
        login_button.grid_forget()
        login2_button = tk.Button(frame_home, text="User", command=login_info, width=5, height=2)
        login2_button.grid(row=0, column=0)

    top = tk.Toplevel()
    top.title("Login")
    top.geometry("300x200")
    e1 = tk.Entry(top, show=None, font=('Arial', 14))
    e2 = tk.Entry(top, show='*', font=('Arial', 14))
    e1.place(x=30, y=20)
    e2.place(x=30, y=50)

    b = tk.Button(top, text="Login", command=login_confirm)
    b.place(x=100, y=100)


def info_command():
    frame_home.place_forget()
    item_data, item_menu, storage = check_info()


    def return_command():
        frame_info.place_forget()
        frame_home.place(x=20, y=5)
        items_choices.destroy()
        

    def change_item(item):

        def confirm_change():
            # item.price = e1.get()
            # item.water = e2.get()
            # item.coco = e3.get()
            # item.milk = e4.get()
            # item.sugar = e5.get()
            # item.cheese = e6.get()
            # print(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get())
            # for i in range(len(item_data["name"])):
            #     if item_data["name"][i] == item.name:
            #         item_data["price"][i] = int(e1.get())
            #         item_data["water"][i] = int(e2.get())
            #         item_data["coco"][i] = int(e3.get())
            #         item_data["milk"][i] = int(e4.get())
            #         item_data["sugar"][i] = int(e5.get())
            #         item_data["cheese"][i] = int(e6.get())
            #         # df = pd.DataFrame(item_data)
            #         item_data.to_csv("item_category.csv", index=0)
            #         break
            for i in item_data:
                if i[0] == item.name:
                    i[1] = int(e1.get())
                    i[2] = int(e2.get())
                    i[3] = int(e3.get())
                    i[4] = int(e4.get())
                    i[5] = int(e5.get())
                    i[6] = int(e6.get())
                    data_new = pd.DataFrame(item_data)
                    data_new.columns = ["name", "price", "water", "coco", "milk", "sugar", "cheese"]
                    data_new.to_csv("items_category.csv", index=0)
                    break

        price_info = item.price
        water_info = item.water
        coco_info = item.coco
        milk_info = item.milk
        sugar_info = item.sugar
        cheese_info = item.cheese

        top = tk.Toplevel()
        top.title("Change the info")
        top.geometry("800x400")
        label_frame = tk.Frame(top, pady=5)
        price_label = tk.Label(label_frame, text="price ")
        price_label.grid(row=2, column=2)

        default_water = tk.StringVar(value=water_info)
        water_label = tk.Label(label_frame, text="water ")
        water_label.grid(row=3, column=2)

        default_coco = tk.StringVar(value=coco_info)
        coco_label = tk.Label(label_frame, text="coco ")
        coco_label.grid(row=4, column=2)

        default_milk = tk.StringVar(value=milk_info)
        milk_label = tk.Label(label_frame, text="milk ")
        milk_label.grid(row=5, column=2)

        default_sugar = tk.StringVar(value=sugar_info)
        sugar_label = tk.Label(label_frame, text="sugar ")
        sugar_label.grid(row=6, column=2)

        default_cheese = tk.StringVar(value=cheese_info)
        cheese_label = tk.Label(label_frame, text="cheese ")
        cheese_label.grid(row=7, column=2)

        default_price = tk.StringVar(value=price_info)
        e1 = tk.Entry(label_frame, textvariable=default_price)
        e1.grid(row=2, column=3)
        e2 = tk.Entry(label_frame, textvariable=default_water)
        e2.grid(row=3, column=3)
        e3 = tk.Entry(label_frame, textvariable=default_coco)
        e3.grid(row=4, column=3)
        e4 = tk.Entry(label_frame, textvariable=default_milk)
        e4.grid(row=5, column=3)
        e5 = tk.Entry(label_frame, textvariable=default_sugar)
        e5.grid(row=6, column=3)
        e6 = tk.Entry(label_frame, textvariable=default_cheese)
        e6.grid(row=7, column=3)

        check_button = tk.Button(top, text="Confirm", width=6, height=3, command=confirm_change)

        check_button.place(x=350, y=300)
        label_frame.place(x=50, y=50)

    frame_info = tk.Frame(root)
    return_b = tk.Button(frame_info, text="Home", command=return_command, width=3, height=2, padx=10, pady=10)
    return_b.grid(row=0, column=0)
    items_choices = tk.Frame(root)
    ButtonList = [0 for i in range(len(item_menu))]
    for i in range(len(item_menu)):
        ButtonList[i] = tk.Button(items_choices, width=30, height=3, text=item_menu[i].name + "   $"
                                                                          + str(
            item_menu[i].price) + "\n" + "water: " + str(item_menu[i].water) + " coco: " + str(item_menu[i].coco)
                                                                          + " milk: " + str(
            item_menu[i].milk) + " sugar: " + str(item_menu[i].sugar) + " cheese: " + str(item_menu[i].cheese),
                                  command=lambda f=item_menu[i]: change_item(f))
        ButtonList[i].grid()

    items_choices.place(x=150, y=10)

    frame_info.place(x=20, y=5)


def contact_command():
    frame_home.place_forget()

    def return_command():
        return_b.grid_forget()

        frame_home.place(x=20, y=5)

    return_b = tk.Button(root, text="Home", command=return_command, width=3, height=2, padx=10, pady=10)
    return_b.grid(row=0, column=0)


def buy_command():
    frame_home.place_forget()
    item_data, item_menu, storage = check_info()
    global ItemOrderList
    ItemOrderList = []

    def return_command():
        return_b.grid_forget()
        items_choices.destroy()
        payment_frame.destroy()
        order_list_frame.destroy()
        frame_home.place(x=20, y=5)

    def add_to_list(item):
        ItemOrderList.append(item)
        order_list.insert("end", item.name)
        count_total_price()

    def count_total_price():
        total_price = 0
        for i in ItemOrderList:
            total_price += i.price
        payment_frame.place_forget()
        payment_bill = tk.Label(payment_frame, text="total: $   " + str(total_price), font=('Arial', 14))
        payment_bill.grid(row=0, column=12)
        payment_frame.place(x=800, y=320)

    return_b = tk.Button(root, text="Home", command=return_command, width=3, height=2, padx=10, pady=10)
    return_b.grid(row=0, column=0)

    items_choices = tk.Frame(root)
    ButtonList = [0 for i in range(len(item_menu))]
    for i in range(len(item_menu)):
        ButtonList[i] = tk.Button(items_choices, width=12, height=2, text=item_menu[i].name + "   $" +
                                                                          str(item_menu[i].price),
                                  command=lambda f=item_menu[i]: add_to_list(f))
        ButtonList[i].grid()

    items_choices.place(x=100, y=50)

    def delete_item():
        delete_item_name = order_list.get("active")
        for i in range(len(ItemOrderList)):
            if ItemOrderList[i].name == delete_item_name:
                ItemOrderList.pop(i)
                break
        order_list.delete("active")
        count_total_price()

    def update_order():
        total_price = 0
        items = []
        for i in ItemOrderList:
            total_price += i.price
            items.append(i.name)
        payment_id = round(time.time())
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        storage_data = pd.read_csv('order_record.csv')
        df = pd.DataFrame([payment_id, date, items, total_price]).T
        df.columns = storage_data.columns
        df_new = pd.concat([storage_data, df], ignore_index=True)

        df_new.to_csv("order_record.csv", index=0)

    def clear_ordering_list():
        global ItemOrderList
        order_list.delete(0, "end")
        ItemOrderList = []
        count_total_price()

    def order_the_list():
        total_price = 0
        for i in ItemOrderList:
            storage.water -= i.water
            storage.coco -= i.coco
            storage.milk -= i.milk
            storage.sugar -= i.sugar
            storage.cheese -= i.cheese
            total_price += i.price

        # update
        update_storage(storage)
        update_order()

        clear_ordering_list()

    order_list_frame = tk.Frame(root)
    order_list = tk.Listbox(order_list_frame, height=11)
    order_list.pack()
    delete_button = tk.Button(order_list_frame, text='Delete', command=lambda: [delete_item()])
    delete_button.pack()
    order_list_frame.place(x=300, y=100)

    payment_frame = tk.Frame(root)
    payment_bill = tk.Label(payment_frame, text="$  0", font=('Arial', 14))
    payment_bill.grid(row=0, column=12)

    clear_button = tk.Button(payment_frame, text="clear", command=clear_ordering_list, width=3, height=2, padx=10,
                             pady=10)
    clear_button.grid(row=2, column=12)

    done_button = tk.Button(payment_frame, text="Done", command=order_the_list, width=3, height=2, padx=10, pady=10)
    done_button.grid(row=4, column=12)

    payment_frame.place(x=800, y=320)


def play_command():
    pass


root = tk.Tk()
root.title("Wuhu tech")
root.geometry("1600x900")

frame_home = tk.Frame(root)

login_image = imagemaker("login.jpg", 50, 50)
login_button = tk.Button(frame_home, image=login_image, command=login_info)
login_button.grid(row=0, column=0)

buy_image = imagemaker("food.png", 250, 200)
buy_button = tk.Button(frame_home, image=buy_image, command=buy_command, width=250, height=200, padx=10, pady=10)
buy_button.grid(row=5, column=5, padx=10, pady=10)

info_image = imagemaker("info.jpg", 250, 200)
info_button = tk.Button(frame_home, image=info_image, command=info_command, width=250, height=200, padx=10, pady=10)
info_button.grid(row=5, column=10, padx=10, pady=10)

contact_image = imagemaker("contact.jpg", 250, 200)
contact_button = tk.Button(frame_home, image=contact_image, command=contact_command, width=250, height=200, padx=10,
                           pady=10)
contact_button.grid(row=5, column=12, padx=10, pady=10)

play_button = tk.Button(frame_home, text="PLAY", command=play_command, width=20, height=4, pady=10)
play_button.grid(row=7, column=10)

frame_home.place(x=20, y=5)

root.mainloop()
