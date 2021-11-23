import tkinter as tk
from tkinter import filedialog
import os
import cv2.cv2
from PIL import Image, ImageTk
import tkinter.messagebox
import items
from PIL.Image import composite
import csv
import numpy as np
import pandas as pd
import time
import re

import matplotlib.pyplot as plt
from pylab import mpl

from people_flow import people_flow




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

    def check_storage(self):
        a = [self.water, self.coco, self.milk, self.sugar, self.cheese]
        for i in a:
            if i < 50:
                return False
        return True


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


# 加密
def enctry(s):
    k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
    encry_str = ""
    for i, j in zip(s, k):
        # i为字符，j为秘钥字符
        temp = str(ord(i) + ord(j)) + '_'  # 加密字符 = 字符的Unicode码 + 秘钥的Unicode码
        encry_str = encry_str + temp
    return encry_str


# 解密
def dectry(p):
    k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
    dec_str = ""
    for i, j in zip(p.split("_")[:-1], k):
        # i 为加密字符，j为秘钥字符
        temp = chr(int(i) - ord(j))  # 解密字符 = (加密Unicode码字符 - 秘钥字符的Unicode码)的单字节字符
        dec_str = dec_str + temp
    return dec_str


def info_command(userlevel):
    if userlevel != 0:
        tk.messagebox.showerror(title='Error', message='Permission denied')
        return
    global root
    global frame_home
    frame_home.place_forget()
    item_data, item_menu, storage = check_info()

    def return_command():
        return_b.grid_forget()
        frame_info.place_forget()
        frame_home.place(x=20, y=5)
        items_choices.destroy()
        storage_frame.place_forget()

    def change_item(item):

        def confirm_change():
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

            items_choices.destroy()
            top.destroy()
            return_command()
            info_command(0)

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

    return_b = tk.Button(root, text="Home", command=return_command, width=3, height=2, padx=10, pady=10)
    return_b.grid(row=0, column=0)
    frame_info = tk.Frame(root)
    items_choices = tk.Frame(root)
    ButtonList = [0 for i in range(len(item_menu))]
    for i in range(len(item_menu)):
        ButtonList[i] = tk.Button(items_choices, width=30, height=3, text=item_menu[i].name + "   $"
                                                                          + str(
            item_menu[i].price) + "\n" + "water: " + str(item_menu[i].water) + " coco: " + str(item_menu[i].coco)
                                                                          + " milk: " + str(
            item_menu[i].milk) + " sugar: " + str(item_menu[i].sugar) + " cheese: " + str(item_menu[i].cheese),
                                  command=lambda f=item_menu[i]: change_item(f))
        ButtonList[i].grid(pady=5)

    items_choices.place(x=150, y=10)
    frame_info.place(x=20, y=5)

    def confirm_storage_change():
        data = np.array([[int(e11.get()), int(e22.get()), int(e33.get()), int(e44.get()), int(e55.get())]])
        data_new = pd.DataFrame(data)
        data_new.columns = ["water", "coco", "milk", "sugar", "cheese"]
        data_new.to_csv("material_storage.csv", index=0)

    storage_water_info = storage.water
    storage_coco_info = storage.coco
    storage_milk_info = storage.milk
    storage_sugar_info = storage.sugar
    storage_cheese_info = storage.cheese

    storage_frame = tk.Frame(root)
    storage_default_water = tk.StringVar(value=storage_water_info)
    storage_water_label = tk.Label(storage_frame, text="water ")
    storage_water_label.grid(row=3, column=2)

    storage_default_coco = tk.StringVar(value=storage_coco_info)
    storage_coco_label = tk.Label(storage_frame, text="coco ")
    storage_coco_label.grid(row=4, column=2)

    storage_default_milk = tk.StringVar(value=storage_milk_info)
    storage_milk_label = tk.Label(storage_frame, text="milk ")
    storage_milk_label.grid(row=5, column=2)

    storage_default_sugar = tk.StringVar(value=storage_sugar_info)
    storage_sugar_label = tk.Label(storage_frame, text="sugar ")
    storage_sugar_label.grid(row=6, column=2)

    storage_default_cheese = tk.StringVar(value=storage_cheese_info)
    storage_cheese_label = tk.Label(storage_frame, text="cheese ")
    storage_cheese_label.grid(row=7, column=2)

    e11 = tk.Entry(storage_frame, textvariable=storage_default_water)
    e11.grid(row=3, column=3)
    e22 = tk.Entry(storage_frame, textvariable=storage_default_coco)
    e22.grid(row=4, column=3)
    e33 = tk.Entry(storage_frame, textvariable=storage_default_milk)
    e33.grid(row=5, column=3)
    e44 = tk.Entry(storage_frame, textvariable=storage_default_sugar)
    e44.grid(row=6, column=3)
    e55 = tk.Entry(storage_frame, textvariable=storage_default_cheese)
    e55.grid(row=7, column=3)

    storage_change_button = tk.Button(storage_frame, text="Confirm", width=8, height=5, command=confirm_storage_change)
    storage_change_button.grid(row=8, column=3)
    storage_frame.place(x=800, y=50)


def rank_command():
    global root
    global frame_home
    frame_home.place_forget()

    def return_command():
        return_b.grid_forget()
        rank_frame.destroy()
        frame_record.destroy()
        button_frame.destroy()
        frame_home.place(x=20, y=5)

    def place_fig1():
        rank_img = ImageTk.PhotoImage(Image.open("rank_img_weekly.jpg"))
        rank_label = tk.Label(rank_frame, image=rank_img, width=500, height=500, padx=10, pady=10)
        rank_label.grid(row=0, column=0)
        rank_frame.place(x=80, y=0)
        rank_frame.mainloop()  # Or the image will be blank

    def place_fig2():
        rank_img = ImageTk.PhotoImage(Image.open("rank_img_allthetime.jpg"))
        rank_label = tk.Label(rank_frame, image=rank_img, width=500, height=500, padx=10, pady=10)
        rank_label.grid(row=0, column=0)
        rank_frame.place(x=80, y=0)
        rank_frame.mainloop()  # Or the image will be blank

    def weekly_rank():
        record = pd.read_csv("order_record.csv")
        record = record[time.time()-record["id"]  < 604800]
        data = np.array2string(np.array(record["items"]))
        item_data, item_menu, storage = check_info()
        rank_info = {}
        for i in item_menu:
            ret = re.findall(i.name, data)
            rank_info.update({i.name: len(ret)})
        rank_info_ordered = sorted(rank_info.items(), key=lambda x: x[1], reverse=False)
        # matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        # matplotlib.rcParams['axes.unicode_minus'] = False
        count = []
        tick = []
        for i in rank_info_ordered:
            count.append(i[1])
            tick.append(i[0])

        plt.figure(figsize=(5, 5))
        plt.barh(range(len(count)), count, height=0.7, color='steelblue', alpha=0.8)  # 从下往上画
        plt.yticks(range(len(count)), tick)
        plt.xlim(0, int(rank_info_ordered[-1][1]) * 1.1)
        plt.xlabel("count")
        plt.title("Ranking")
        for x, y in enumerate(count):
            plt.text(y + 0.2, x - 0.1, '%s' % y)
        plt.savefig("rank_img_weekly.jpg")

        # rank_img = ImageTk.PhotoImage(Image.open("rank_img.jpg"))
        # rank_label = tk.Label(rank_frame, image=rank_img, width=800, height=800, padx=10, pady=10)
        # rank_label.grid(row=0, column=0)
        # rank_frame.place(x=80, y=0)
        # rank_frame.mainloop()  # Or the image will be blank

    def allthetime_rank():
        record = pd.read_csv("order_record.csv")
        data = np.array2string(np.array(record["items"]))
        item_data, item_menu, storage = check_info()
        rank_info = {}
        for i in item_menu:
            ret = re.findall(i.name, data)
            rank_info.update({i.name: len(ret)})
        rank_info_ordered = sorted(rank_info.items(), key=lambda x: x[1], reverse=False)
        # matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        # matplotlib.rcParams['axes.unicode_minus'] = False
        count = []
        tick = []
        for i in rank_info_ordered:
            count.append(i[1])
            tick.append(i[0])

        plt.figure(figsize=(5, 5))
        plt.barh(range(len(count)), count, height=0.7, color='steelblue', alpha=0.8)  # 从下往上画
        plt.yticks(range(len(count)), tick)
        plt.xlim(0, int(rank_info_ordered[-1][1]) * 1.1)
        plt.xlabel("count")
        plt.title("Ranking")
        for x, y in enumerate(count):
            plt.text(y + 0.2, x - 0.1, '%s' % y)
        plt.savefig("rank_img_allthetime.jpg")

        # rank_img = ImageTk.PhotoImage(Image.open("rank_img.jpg"))
        # rank_label = tk.Label(rank_frame, image=rank_img, width=800, height=800, padx=10)
        # rank_label.grid(row=0, column=0)
        # rank_frame.place(x=80, y=0)
        # rank_frame.mainloop()  # Or the image will be blank

    return_b = tk.Button(root, text="Home", command=return_command, width=3, height=2, padx=10, pady=10)
    return_b.grid(row=0, column=0)
    rank_frame = tk.Frame(root)
    weekly_rank()

    allthetime_rank()
    # 两个button
    button_frame = tk.Frame(root)
    weekly_rank = tk.Button(button_frame, text="Weekly ranking", command=place_fig1, width=15, height=2)
    allthetime_rank = tk.Button(button_frame, text="All the time ranking", command=place_fig2, width=15, height=2)
    weekly_rank.grid(row=1, column=0)
    allthetime_rank.grid(row=2, column=0)
    button_frame.place(x=120, y=600)
    rank_frame.place(x=10, y=0)

    frame_record = tk.Frame(root)
    sb = tk.Scrollbar(frame_record)
    # sb.grid(row=0, column=0)
    sb.pack(side="right", fill="y")
    lb = tk.Listbox(frame_record, yscrollcommand=sb.set, width=60, height=40)

    def standardize(a, b, c):
        res = 55 - len(a) - len(b) - len(str(c))
        if res < 0:
            return a + "   " + b[:(55 - len(a) - len(str(c)))] + "     " + str(c)
        else:
            for m in range(2 * res):
                b += " "
            return a + "   " + b + str(c)

    record = pd.read_csv('order_record.csv')
    data = np.array(record)
    for i in range(len(data)):
        # lb.insert("end", data[i][1] + "   " + data[i][2][:30]+ "   " + str(data[i][3]))
        lb.insert("end", standardize(data[i][1], data[i][2], data[i][3]))
    # lb.grid(row=0, column=1)
    lb.pack(side="left", fill="both")
    sb.config(command=lb.yview)

    frame_record.place(x=600, y=50)
    place_fig1()  # show weekly_rank by default


def buy_command():
    global root
    global frame_home
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
        if not storage.check_storage():
            tk.messagebox.showerror(title='Error', message='Low storage')
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
    bill = tk.Label(payment_frame, text="   $  0", font=('Arial', 14), width=15)
    bill.grid(row=0, column=12)

    clear_button = tk.Button(payment_frame, text="clear", command=clear_ordering_list, width=3, height=2, padx=10,
                             pady=10)
    clear_button.grid(row=2, column=12)

    done_button = tk.Button(payment_frame, text="Done", command=order_the_list, width=3, height=2, padx=10, pady=10)
    done_button.grid(row=4, column=12)

    payment_frame.place(x=800, y=320)


def people_command():
    # def cancel_command():
    #     loading_window.destroy()
    #     exit(0)
    # loading_window = tk.Toplevel()
    # loading_window.title("Please wait")
    # loading_window.geometry("300x200")
    # loading_label = tk.Label(loading_window, text="LOADING")
    # loading_label.place(x=100, y=50)
    #
    # cancel_button = tk.Button(loading_window, text="Cancel", command=cancel_command)
    # cancel_button.place(x=100, y=100)

    # file_win = tk.Toplevel()
    # file_win.withdraw()
    #
    # filepath = filedialog.askopenfilename(initialdir = os.getcwd(), filetypes = [("video files","*.flv")])
    # print(filepath)

    total_num, area_num = people_flow()




    plt.figure(figsize=(9, 6))
    # y = [0, 0, 15, 15, 15, 17, 16, 16, 15, 17, 17, 15, 15, 15, 15, 15, 15, 14, 14, 14, 14, 14, 14, 14, 13, 14, 13, 13,
    #      12, 12, 12, 11, 11, 11, 11, 12, 13, 13, 13, 13, 13, 13, 13, 12, 12, 12, 13, 14, 14, 13, 10, 11, 12, 11, 12, 13,
    #      11, 11, 10, 10, 12, 12, 13, 12, 10, 11, 11, 10, 12, 12, 11, 11, 10, 11, 12, 11, 11, 11, 12, 12, 12, 11, 11, 12,
    #      11, 10, 10, 11, 11, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 10, 10, 11,
    #      12, 12, 11, 12, 12, 11, 10, 12, 11, 10, 10, 11, 12, 12, 11, 12, 13, 13, 13, 12, 12, 13, 13, 13, 13, 14, 14, 13,
    #      14, 13, 15, 14, 12, 11, 14, 14, 12, 13, 15, 15, 15, 15, 16, 17, 17, 16, 16, 17, 18, 18, 18, 19, 19, 17, 17, 17,
    #      19, 19, 17, 17, 18, 18, 18, 16, 17, 17, 17, 17, 17, 17, 17, 16, 16, 17, 18, 18, 18, 17, 17, 16, 17, 17, 17, 18,
    #      18, 17, 16, 16, 16, 17, 18, 17, 16, 17, 17, 16, 15, 15, 16, 16, 16, 16, 17, 17, 16, 16, 16, 17, 17, 17, 17, 16,
    #      17, 17, 18, 18, 17, 17, 20, 22, 19, 20, 21, 18, 18, 19, 18, 18, 19, 19, 19, 18, 18, 20, 19, 19, 18, 16, 19, 19,
    #      20, 21, 21, 20, 19, 18, 18, 17, 18, 18, 18, 18, 21, 22, 19, 19, 18, 18, 17, 19, 19, 18, 18, 20, 20, 20, 20, 19,
    #      20, 20, 20, 21, 21, 22, 20, 20, 22, 20, 20, 22, 21, 19, 21, 22, 22, 22, 21, 22, 21, 20, 19, 20, 19, 18, 18, 18,
    #      19, 17, 17, 15, 15, 15, 17, 15, 14, 15, 16, 16, 17, 17, 18, 18, 20, 17, 16, 19, 17, 16, 15, 15, 15, 15, 18, 16,
    #      17, 19, 17, 17, 16, 16, 16, 17, 16, 17, 18, 19, 19, 19, 18, 17, 16, 16, 17, 19, 20, 19, 19, 18, 19, 19, 17, 15,
    #      15, 17, 18, 17, 17, 18, 18, 17, 18, 17, 18, 18, 18, 16, 14, 15, 16, 17, 17, 17, 16, 16, 16, 17, 18, 20, 19, 18,
    #      20, 19, 19, 20, 20, 19, 18, 18, 18, 19, 19, 18, 17, 17, 18, 16, 16, 17, 16, 15, 14, 16, 15, 13, 14, 14, 14, 14,
    #      13, 13, 13, 13, 14, 14, 14, 15, 16, 16, 16, 15, 16, 15, 12, 12, 12, 13, 14, 14, 13, 12, 13, 14, 12, 13, 12, 13,
    #      13, 11, 12, 11, 12, 11, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 9, 10, 12, 12, 10, 13, 14, 12, 12, 12, 12, 13,
    #      13, 11, 13, 13, 13, 13, 12, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 10, 10, 10, 11, 11, 11, 12,
    #      12, 12, 12, 11, 11, 11, 11, 11, 10, 10, 11, 11, 11, 10, 11, 9, 9, 9, 9, 9, 9, 8, 8, 9, 10, 10, 10, 10, 10, 9,
    #      9, 9, 11, 11, 9, 9, 9, 9, 10, 9, 9, 9, 10, 12, 11, 11, 11, 11, 12, 12, 11, 11, 11, 12, 13, 14, 14, 13, 12, 12,
    #      13, 13, 12, 12, 13, 13, 16, 16, 14, 14, 15, 16, 15, 15, 15, 14, 14, 14, 14, 14, 15, 16, 16, 16, 16, 16, 16, 15,
    #      16, 16, 16, 16, 16, 17, 17, 18, 16, 17, 16, 17, 16, 15, 15, 16, 16, 15, 16, 15, 15, 14, 14, 15, 15, 17, 17, 17,
    #      17, 18, 18, 18, 17, 17, 17, 18, 18, 18, 17, 17, 16, 18, 18, 17, 18, 18, 19, 20, 18, 18, 20, 20, 21, 19, 19, 18,
    #      20, 19, 18, 18, 19, 19, 21, 22, 19, 20, 22, 21, 21, 22, 22, 22, 24, 22, 22, 21, 20, 20, 22, 21, 19, 18, 20, 20,
    #      23, 21, 20, 24, 23, 22, 23, 22, 20, 20, 22, 23, 23, 23, 23, 20, 21, 19, 17, 17, 20, 20, 21, 21, 20, 22, 24, 24,
    #      24, 24, 24, 24, 25, 26, 26, 27, 28, 28, 24, 22, 22, 23, 27, 25, 28, 26, 23, 24, 24, 24, 26, 25, 26, 25, 25, 25,
    #      25, 25, 26, 28, 25, 27, 27, 26, 27, 29, 29, 29, 28, 28, 26, 26, 24, 24, 24, 24, 23, 24, 24, 24, 25, 25, 24, 24,
    #      25, 23, 23, 22, 24, 25, 27, 25, 24, 21, 25, 24, 23, 24, 24, 21, 24, 22, 22]
    # y1 = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    #       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    #       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    #       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    #       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    #       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    #       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
    #       6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
    #       6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
    #       6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
    #       6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    #       7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    #       7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    #       7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
    #       8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
    #       8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
    #       8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
    #       8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
    #       8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
    #       9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
    #       9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
    #       10, 10, 10, 10]
    y = total_num
    y1 = area_num
    x = np.linspace(8, 18, len(y))
    plt.stackplot(x, y, y1)

    plt.xlabel('time')
    plt.ylabel('number')
    plt.title('People flow', fontsize=18)
    plt.legend(['area number', 'total number'], fontsize=10, loc='best')  # 显示图例
    plt.savefig("flow.png")
    # loading_window.destroy()
    im = Image.open('flow.png')
    im.show()

def home_command(username, user_level):
    global root
    root = tk.Tk()
    root.title("Wuhu tech")
    root.geometry("1500x800")
    global frame_home
    frame_home = tk.Frame(root)

    login_button = tk.Button(frame_home, text="username: %s\n userlevel: %s" % (username, user_level),
                             width=12, height=5, font=('Arial', 14))
    login_button.grid(row=0, column=0)

    buy_image = imagemaker("food.png", 250, 200)
    buy_button = tk.Button(frame_home, image=buy_image, command=buy_command, width=250, height=200, padx=10, pady=10)
    buy_button.grid(row=5, column=1, padx=10, pady=10)

    info_image = imagemaker("info.jpg", 250, 200)
    info_button = tk.Button(frame_home, image=info_image, command=lambda: info_command(user_level), width=250,
                            height=200, padx=10, pady=10)
    info_button.grid(row=5, column=2, padx=10, pady=10)

    rank_image = imagemaker("rank.jpg", 250, 200)
    rank_button = tk.Button(frame_home, image=rank_image, command=rank_command, width=250, height=200, padx=10,
                            pady=10)
    rank_button.grid(row=5, column=3, padx=10, pady=10)

    people_image = imagemaker("people.jpg", 250, 200)
    people_button = tk.Button(frame_home, image=people_image, command=people_command, width=250, height=200, padx=10,
                              pady=10)
    people_button.grid(row=5, column=4, padx=10, pady=10)

    frame_home.place(x=0, y=0)
    frame_home.mainloop()
    root.mainloop()


def login_command():
    def login_confirm():
        id_get = e1.get()
        password_get = e2.get()
        if len(password_get)==0 or len(id_get)==0:
            tk.messagebox.showerror(title='Error', message='Fill your id or password!')
        else:
            user_info = pd.read_csv('user_information.csv')
            res = user_info[user_info['id'].isin([enctry(id_get)])]
            if len(res) == 0:
                tk.messagebox.showerror(title='Error', message='Wrong id or password!')
            else:
                real_password = res["password"]
                if np.array(real_password)[0] == enctry(password_get):
                    tk.messagebox.showinfo(title='Hi', message='Login successfully')
                    username = dectry(np.array(res["username"])[0])

                    user_level = int(dectry(np.array(res["level"])[0]))
                    login_root.destroy()
                    home_command(username, user_level)
                else:
                    tk.messagebox.showerror(title='Error', message='Wrong id or password!')

    def register_command():
        def register_confirm():
            register_name_get = register_e1.get()
            register_password_get = register_e2.get()
            register_name = enctry(register_name_get)
            register_password = enctry(register_password_get)

            user_info = pd.read_csv('user_information.csv')
            user_id = str(len(user_info["id"]))
            register_id = enctry(user_id)
            df = pd.DataFrame([register_id, register_name, register_password, enctry(str(2))]).T
            df.columns = user_info.columns
            df_new = pd.concat([user_info, df], ignore_index=True)

            df_new.to_csv("user_information.csv", index=0)
            register_top.destroy()
            tk.messagebox.showinfo(title='Registry successfully', message='Your user id is %s' % user_id)

        register_top = tk.Toplevel()
        register_top.title("Login")
        register_top.geometry("300x200")
        register_name_label = tk.Label(register_top, text="Name", font=('Arial', 14))
        register_password_label = tk.Label(register_top, text="Password", font=('Arial', 14))
        register_e1 = tk.Entry(register_top, show=None, font=('Arial', 14))
        register_e2 = tk.Entry(register_top, show='*', font=('Arial', 14))
        register_blank = tk.Label(register_top, text=" ")
        register_blank.grid(row=2, column=2)
        register_name_label.grid(row=5, column=2)
        register_password_label.grid(row=6, column=2)
        register_e1.grid(row=5, column=3)
        register_e2.grid(row=6, column=3)

        b = tk.Button(register_top, text="Register", command=register_confirm)
        b.place(x=100, y=150)

    login_root = tk.Tk()
    login_root.title("Login")
    login_root.geometry("300x200")
    id_label = tk.Label(login_root, text="ID", font=('Arial', 14))
    password_label = tk.Label(login_root, text="Password", font=('Arial', 14))
    e1 = tk.Entry(login_root, show=None, font=('Arial', 14))
    e2 = tk.Entry(login_root, show='*', font=('Arial', 14))
    blank = tk.Label(login_root, text=" ")
    blank.grid(row=2, column=2)
    id_label.grid(row=5, column=2)
    password_label.grid(row=6, column=2)
    e1.grid(row=5, column=3)
    e2.grid(row=6, column=3)

    b = tk.Button(login_root, text="Login", command=login_confirm)
    b.place(x=50, y=150)

    register = tk.Button(login_root, text="Register", command=register_command)
    register.place(x=150, y=150)

    login_root.mainloop()


# login_command()
home_command(0, 0)