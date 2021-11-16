import tkinter as tk

import tkinter.messagebox

import numpy as np
import pandas as pd





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
        storage_frame.destroy()

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
            info_command()

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
