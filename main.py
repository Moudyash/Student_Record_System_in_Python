import tkinter as tk
from tkinter import *
from tkinter import ttk
from csv import DictWriter
import os
from tkinter import messagebox

root = Tk()
root.title('Student Record System')
root.geometry("300x300")

#creating  labels

label_head = tk.Label(root,text='Student Record System')
label_head.grid(row=0,column=0)

label1 = ttk.Label(root,text="Enter Your Name :")
label1.grid(row=1,column=0,sticky=tk.W)

label2 = tk.Label(root,text="Enter Your Email :")
label2.grid(row=2,column=0,sticky=tk.W)

label3 = tk.Label(root,text="Enter Your Age :")
label3.grid(row=3,column=0,sticky=tk.W)

label4 = tk.Label(root,text="Select Your gender :")
label4.grid(row=4,column=0,sticky=tk.W)


#  Creating Entry box 

entrybox_1_var = tk.StringVar()
entrybox_1 = ttk.Entry(root, width = 16, textvariable = entrybox_1_var)
entrybox_1.grid(row=1,column=1,sticky=tk.W)
entrybox_1.focus()

entrybox_2_var = tk.StringVar()
entrybox_2 = tk.Entry(root, width = 16, textvariable = entrybox_2_var)
entrybox_2.grid(row=2,column=1,sticky=tk.W)

entrybox_3_var = tk.StringVar()
entrybox_3 = tk.Entry(root, width = 16, textvariable = entrybox_3_var)
entrybox_3.grid(row=3,column=1,sticky=tk.W)

#creating combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root,width=13, textvariable = gender_var, state='readonly')
gender_combobox['values']= ('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=4,column=1)

# creating radio button 

usertype = StringVar() 
radio_btn1 = ttk.Radiobutton(root,text='Student',value='Student',variable=usertype)
radio_btn1.grid(row=5,column=0)

radio_btn2 = ttk.Radiobutton(root,text='Teacher',value='Teacher',variable=usertype)
radio_btn2.grid(row=5,column=1)

#creating check button
checkvar = IntVar()
check_btn = ttk.Checkbutton(root,text='check if you want to Subscribe to our newsletter',variable=checkvar)
check_btn.grid(row=6, columnspan=3)

def action():
    user_name = entrybox_1_var.get() 
    user_email = entrybox_2_var.get()
    user_age = entrybox_3_var.get()
    gender_vari = gender_var.get()
    user_type = usertype.get()
    if checkvar.get()==0:
        Subscribed = 'No'
    else:
        Subscribed = 'yes'
    
 
# writing to csv file

    with open("st_records.csv",'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName','User email address','User age','User gender','User type','subscribed'])

        if os.stat("st_records.csv").st_size==0: #checks if file contains the header or not
            DictWriter.writeheader(dict_writer)

        dict_writer.writerow({'UserName': user_name,'User email address': user_email, 'User age': user_age,'User gender': gender_vari,'User type': user_type,'subscribed':Subscribed })

        messagebox.showinfo('Message','Record added Sucessfully')  #creating message box



    name =  entrybox_1.delete(0,tk.END)
    age = entrybox_2.delete(0,tk.END)
    email = entrybox_3.delete(0,tk.END)
    label1.configure(foreground='Blue')



#creating buttons
submit_btn = tk.Button(root,text='Submit', command= action)
submit_btn.grid(row=8,columnspan=3)


root.mainloop()    