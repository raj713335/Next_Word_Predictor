from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText


from tkinter import Entry, Frame, Label, StringVar
from tkinter.constants import *
from tkinter.messagebox import showinfo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



import os
import time


from datetime import date
from datetime import timedelta

import Output




def user_add_kc():
    # CLASS FOR ADDING STATION

    class user_add_kc():

        def __init__(self, window):

            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            shop_floor_canvax = tk.Canvas(window, width=400, height=501, background='white')
            shop_floor_canvax.grid(row=0, column=0)
            shop_floor_canvax.create_line(-10, 200, 400, 200, fill='grey', width=3)
            shop_floor_canvax.create_line(-10, 274, 400, 274, fill='grey', width=3)






            def command(tkvar0):
                print(tkvar0.widget.get('1.0', 'end-1c'))
                suggestion(x=tkvar0.widget.get('1.0', 'end-1c'))



            def suggestion(x):




                value=Output.predict_and_return(x)

                print(value)

                try:
                    one=value[0]
                except:
                    one="i"

                try:
                    two=value[1]
                except:
                    two="love"

                try:
                    three=value[2]
                except:
                    three="my"
                try:
                    four=value[3]
                except:
                    four="capatalist"

                try:
                    five=value[4]
                except:
                    five="mentality"

                self.btn_one = ttk.Button(user_add, text=one, width=20)
                self.btn_one.place(x=0, y=230, width=80, height=45)

                self.btn_two = ttk.Button(user_add, text=two, width=20)
                self.btn_two.place(x=80, y=230, width=80, height=45)

                self.btn_three = ttk.Button(user_add, text=three, width=20)
                self.btn_three.place(x=160, y=230, width=80, height=45)

                self.btn_four = ttk.Button(user_add, text=four, width=20)
                self.btn_four.place(x=240, y=230, width=80, height=45)

                self.btn_five = ttk.Button(user_add, text=five, width=20)
                self.btn_five.place(x=320, y=230, width=80, height=45)










            self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
            self.tkvar0.place(x=0, y=0,width=400, height=200 )


            self.tkvar0.bind("<Key>", command)


            def write_command_1():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(1))



            def write_command_2():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(2))


            def write_command_3():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(3))

            def write_command_4():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(4))

            def write_command_5():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(5))


            def write_command_6():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(6))

            def write_command_7():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(7))

            def write_command_8():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(8))


            def write_command_9():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(9))


            def write_command_0():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(0))


            def write_command_a():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("a"))


            def write_command_b():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("b"))


            def write_command_c():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("c"))


            def write_command_d():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("d"))


            def write_command_e():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("e"))


            def write_command_f():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("f"))


            def write_command_g():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("g"))



            def write_command_h():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("h"))


            def write_command_i():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("i"))


            def write_command_j():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("j"))


            def write_command_k():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("k"))



            def write_command_l():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("l"))


            def write_command_m():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("m"))


            def write_command_n():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("n"))


            def write_command_o():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("o"))


            def write_command_p():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("p"))


            def write_command_q():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("q"))


            def write_command_r():
                temp=str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("r"))

            def write_command_s():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("s"))

            def write_command_t():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("t"))

            def write_command_u():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("u"))

            def write_command_v():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("v"))

            def write_command_w():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("w"))

            def write_command_x():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("x"))

            def write_command_y():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("y"))


            def write_command_z():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str("z"))



            def write_command_space():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(" "))


            def write_command_bsk():
                temp = str(self.tkvar0.get('1.0', 'end-1c'))
                # self.tkvar0.destroy()
                # self.tkvar0 = ScrolledText(window,font=("Ariel", 20), width=20)
                # self.tkvar0.place(x=0, y=0, width=400, height=200)
                self.tkvar0.insert("end-1c", str(" "))



            s = ttk.Style()
            s.configure('my.TButton', font=('Aerial', 12, 'bold'))

            # b = ttk.Button(mainframe, text='Press me', style='my.TButton',

            # self.btn0 = ttk.Button(user_add, text="DASHBOARD", style='my.TButton', width=20)
            # self.btn0.place(x=0, y=70, width=230, height=70)
            #
            # self.btn1 = ttk.Button(user_add, text="MASTER", style='my.TButton', width=20)
            # self.btn1.place(x=230, y=70, width=230, height=70)

            self.btn_submit = ttk.Button(user_add, text="SUBMIT", width=20)
            self.btn_submit.place(x=0, y=200, width=400, height=30)

            # The zero row of keyboard Layout



            self.btn_uk = ttk.Button(user_add, text="", width=20)
            self.btn_uk.place(x=0, y=275, width=400, height=226)

            self.btn_1 = ttk.Button(user_add, text="1", width=20,command=write_command_1)
            self.btn_1.place(x=0, y=275, width=40, height=45)

            self.btn_2 = ttk.Button(user_add, text="2", width=20,command=write_command_2)
            self.btn_2.place(x=40, y=275, width=40, height=45)

            self.btn_3 = ttk.Button(user_add, text="3", width=20,command=write_command_3)
            self.btn_3.place(x=80, y=275, width=40, height=45)

            self.btn_4 = ttk.Button(user_add, text="4", width=20,command=write_command_4)
            self.btn_4.place(x=120, y=275, width=40, height=45)

            self.btn_5 = ttk.Button(user_add, text="5", width=20,command=write_command_5)
            self.btn_5.place(x=160, y=275, width=40, height=45)

            self.btn_6 = ttk.Button(user_add, text="6", width=20,command=write_command_6)
            self.btn_6.place(x=200, y=275, width=40, height=45)

            self.btn_7 = ttk.Button(user_add, text="7", width=20,command=write_command_7)
            self.btn_7.place(x=240, y=275, width=40, height=45)

            self.btn_8 = ttk.Button(user_add, text="8", width=20,command=write_command_8)
            self.btn_8.place(x=280, y=275, width=40, height=45)

            self.btn_9 = ttk.Button(user_add, text="9", width=20,command=write_command_9)
            self.btn_9.place(x=320, y=275, width=40, height=45)

            self.btn_0 = ttk.Button(user_add, text="0", width=20,command=write_command_0)
            self.btn_0.place(x=360, y=275, width=40, height=45)

            #The first row of keyboard Layout

            self.btn_q = ttk.Button(user_add, text="q", width=20,command=write_command_q)
            self.btn_q.place(x=0, y=320, width=40, height=45)

            self.btn_w = ttk.Button(user_add, text="w", width=20,command=write_command_w)
            self.btn_w.place(x=40, y=320, width=40, height=45)

            self.btn_e = ttk.Button(user_add, text="e", width=20,command=write_command_e)
            self.btn_e.place(x=80, y=320, width=40, height=45)

            self.btn_r = ttk.Button(user_add, text="r", width=20,command=write_command_r)
            self.btn_r.place(x=120, y=320, width=40, height=45)

            self.btn_t = ttk.Button(user_add, text="t", width=20,command=write_command_t)
            self.btn_t.place(x=160, y=320, width=40, height=45)

            self.btn_y = ttk.Button(user_add, text="y", width=20,command=write_command_y)
            self.btn_y.place(x=200, y=320, width=40, height=45)

            self.btn_u = ttk.Button(user_add, text="u", width=20,command=write_command_u)
            self.btn_u.place(x=240, y=320, width=40, height=45)

            self.btn_i = ttk.Button(user_add, text="i", width=20,command=write_command_i)
            self.btn_i.place(x=280, y=320, width=40, height=45)

            self.btn_o = ttk.Button(user_add, text="o", width=20,command=write_command_o)
            self.btn_o.place(x=320, y=320, width=40, height=45)

            self.btn_p = ttk.Button(user_add, text="p", width=20,command=write_command_p)
            self.btn_p.place(x=360, y=320, width=40, height=45)





            #The Second row of Keyboard Layout

            self.btn_a = ttk.Button(user_add, text="a", width=20,command=write_command_a)
            self.btn_a.place(x=20, y=365, width=40, height=45)

            self.btn_s = ttk.Button(user_add, text="s", width=20,command=write_command_s)
            self.btn_s.place(x=60, y=365, width=40, height=45)

            self.btn_d = ttk.Button(user_add, text="d", width=20,command=write_command_d)
            self.btn_d.place(x=100, y=365, width=40, height=45)

            self.btn_f = ttk.Button(user_add, text="f", width=20,command=write_command_f)
            self.btn_f.place(x=140, y=365, width=40, height=45)

            self.btn_g = ttk.Button(user_add, text="g", width=20,command=write_command_g)
            self.btn_g.place(x=180, y=365, width=40, height=45)

            self.btn_h = ttk.Button(user_add, text="h", width=20,command=write_command_h)
            self.btn_h.place(x=220, y=365, width=40, height=45)

            self.btn_j = ttk.Button(user_add, text="j", width=20,command=write_command_j)
            self.btn_j.place(x=260, y=365, width=40, height=45)

            self.btn_k = ttk.Button(user_add, text="k", width=20,command=write_command_k)
            self.btn_k.place(x=300, y=365, width=40, height=45)

            self.btn_l = ttk.Button(user_add, text="l", width=20,command=write_command_l)
            self.btn_l.place(x=340, y=365, width=40, height=45)


            #The third row of keyboard Layout

            self.btn_z = ttk.Button(user_add, text="z", width=20,command=write_command_z)
            self.btn_z.place(x=60, y=410, width=40, height=45)

            self.btn_x = ttk.Button(user_add, text="x", width=20,command=write_command_x)
            self.btn_x.place(x=100, y=410, width=40, height=45)

            self.btn_c = ttk.Button(user_add, text="c", width=20,command=write_command_c)
            self.btn_c.place(x=140, y=410, width=40, height=45)

            self.btn_v = ttk.Button(user_add, text="v", width=20,command=write_command_v)
            self.btn_v.place(x=180, y=410, width=40, height=45)

            self.btn_b = ttk.Button(user_add, text="b", width=20,command=write_command_b)
            self.btn_b.place(x=220, y=410, width=40, height=45)

            self.btn_n = ttk.Button(user_add, text="n", width=20,command=write_command_n)
            self.btn_n.place(x=260, y=410, width=40, height=45)

            self.btn_m = ttk.Button(user_add, text="m", width=20,command=write_command_m)
            self.btn_m.place(x=300, y=410, width=40, height=45)

            self.btn_bsk = ttk.Button(user_add, text="bsk", width=20,command=write_command_bsk)
            self.btn_bsk.place(x=340, y=410, width=60, height=45)

            self.btn_space = ttk.Button(user_add, text="", width=20,command=write_command_space)
            self.btn_space.place(x=60, y=455, width=280, height=45)
















        def quit(self):
            user_add.destroy()

    user_add = tk.Tk()
    #user_add.iconbitmap(default='IMAGES/favicon.ico')
    # user_add.overrideredirect(True)
    # user_add.geometry("{0}x{1}+0+0".format(user_add.winfo_screenwidth(), user_add.winfo_screenheight()))
    user_login_window = user_add_kc(user_add)
    user_add.config(background='white')
    user_add.attributes('-alpha', 1)

    user_add.title('WORD PREDICTOR')
    user_add.geometry("400x501")
    user_add.mainloop()


if __name__ == "__main__":
    user_add_kc()