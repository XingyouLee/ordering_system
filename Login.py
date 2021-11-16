import tkinter as tk
import numpy as np
import pandas as pd
from Decode import dectry, enctry
from Home import home_command
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