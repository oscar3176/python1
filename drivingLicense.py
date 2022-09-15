# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:20:08 2022

@author: Admin
"""
from tkinter import*
root = Tk()
root.title("Driving License")
root.geometry("600x600")

label_title = Label(root)
label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle_type = Label(root)
    
drivingId = 6654809182
name = "Sahil Prashant Chogle"
dob = "2nd Feb 2012"
pin = 554329
address = "Qatar, Doha, Barwa Village, B-15, Flat-9"
vehicle_type = "Four-wheeler"
def showLicense():
    print(drivingId)
    print(name)
    print(dob)
    print(pin)
    print(address)
    print(vehicle_type)
    label_title["text"] = "Driving License"
    label_id["text"] = "Driving Id - " + str(drivingId)
    label_name["text"] = "Name - " + str(name)
    label_dob["text"] = "DOB - " + str(dob)
    label_pin["text"] = "Pin - " + str(pin)
    label_address["text"] = "Address - " + str(address)
    label_vehicle_type["text"] = "Vehicle Type - " + str(vehicle_type)

btn = Button(root, text="Show License", command = showLicense)
btn.pack()
label_title.pack()
label_id.pack()
label_name.pack()
label_dob.pack()
label_pin.pack()
label_address.pack()
label_vehicle_type.pack()

root.mainloop()