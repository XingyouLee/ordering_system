import tkinter as tk

from PIL import Image, ImageTk

import numpy as np
import pandas as pd
import time
import re
import matplotlib.pyplot as plt

def rank_command():
    global root
    global frame_home
    frame_home.place_forget()

    def return_command():
        return_b.grid_forget()
        rank_frame.destroy()
        frame_record.destroy()
        frame_home.place(x=20, y=5)

    def place_fig():
        rank_img = ImageTk.PhotoImage(Image.open("rank_img.jpg"))
        rank_label = tk.Label(rank_frame, image=rank_img, width=800, height=800, padx=10, pady=10)
        rank_label.grid(row=0, column=0)
        rank_frame.place(x=80, y=0)
        rank_frame.mainloop()  # Or the image will be blank

    def weekly_rank():
        record = pd.read_csv("order_record.csv")
        record = record[record["id"] - time.time() < 604800]
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

        plt.figure(figsize=(7, 7))
        plt.barh(range(len(count)), count, height=0.7, color='steelblue', alpha=0.8)  # 从下往上画
        plt.yticks(range(len(count)), tick)
        plt.xlim(0, int(rank_info_ordered[-1][1]) * 1.1)
        plt.xlabel("count")
        plt.title("Ranking")
        for x, y in enumerate(count):
            plt.text(y + 0.2, x - 0.1, '%s' % y)
        plt.savefig("rank_img.jpg")

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

        plt.figure(figsize=(7, 7))
        plt.barh(range(len(count)), count, height=0.7, color='steelblue', alpha=0.8)  # 从下往上画
        plt.yticks(range(len(count)), tick)
        plt.xlim(0, int(rank_info_ordered[-1][1]) * 1.1)
        plt.xlabel("count")
        plt.title("Ranking")
        for x, y in enumerate(count):
            plt.text(y + 0.2, x - 0.1, '%s' % y)
        plt.savefig("rank_img.jpg")

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
    weekly_rank = tk.Button(button_frame, text="Weekly ranking", command=place_fig, width=15, height=2)
    allthetime_rank = tk.Button(button_frame, text="All the time ranking", command=place_fig, width=15, height=2)
    weekly_rank.grid(row=1, column=0)
    allthetime_rank.grid(row=2, column=0)
    button_frame.place(x=120, y=800)
    rank_frame.place(x=80, y=0)

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

    frame_record.place(x=1000, y=50)
    place_fig()  # show weekly_rank by default
