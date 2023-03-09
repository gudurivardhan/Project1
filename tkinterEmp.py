from tkinter import *

import generate_Employee_QR
import scanning_qrcode
import writeEmployeeDetails

root=Tk()
root.geometry("655x544")
root.title("Employee Attendance System")
f1 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f1.pack(side=TOP, fill="x")
l1 = Label(f1, text="Employee Attendance System", font="Helvetica 16 bold", fg="red", pady=22)
l1.pack()
register=Button(root,text="Register",command=writeEmployeeDetails.writeEmpDetails)
generateQR=Button(root,text="Generate QR code",command=generate_Employee_QR.initiateGeneration)
scan=Button(root,text="Scan QR",command=scanning_qrcode.scanIntiatiate)
register.pack()
generateQR.pack()
scan.pack()
root.mainloop()












































































































































































































































