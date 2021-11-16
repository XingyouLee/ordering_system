import tkinter as tk

import tkinter.messagebox

import pandas as pd
import time


def update_storage(storage):
    headers = ["water", "coco", "milk", "sugar", "cheese"]

    rows = [[storage.water, storage.coco, storage.milk, storage.sugar, storage.cheese]]

    with open('material_storage.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

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
    payment_bill = tk.Label(payment_frame, text="$  0", font=('Arial', 14))
    payment_bill.grid(row=0, column=12)

    clear_button = tk.Button(payment_frame, text="clear", command=clear_ordering_list, width=3, height=2, padx=10,
                             pady=10)
    clear_button.grid(row=2, column=12)

    done_button = tk.Button(payment_frame, text="Done", command=order_the_list, width=3, height=2, padx=10, pady=10)
    done_button.grid(row=4, column=12)

    payment_frame.place(x=800, y=320)
