from PIL import Image
import pyzbar.pyzbar as pyzbar
import pandas as pd


# Read QR code from an image file
def read_qr_code_image(image_file):
    decoded_objs = pyzbar.decode(Image.open(image_file))
    return decoded_objs[0].data.decode()


def read_employee_details(file_path):
    employee_details = pd.read_csv(file_path)
    return employee_details


def mark_attendance(qr_code_data):
    data_items = qr_code_data.split(',')
    employee_id = int(data_items[0])
    employee_details = read_employee_details("employee_details.csv")
    employee_attendance = pd.read_csv("employee_attendance.csv")
    if employee_id in employee_details["ID"].values:
        if employee_id not in employee_attendance["ID"].values:
            employee_attendance = employee_attendance.append({"ID": employee_id, "Attendance": "Present"},
                                                             ignore_index=True)
            employee_attendance.to_csv("employee_attendance.csv", index=False)
            print(f"Attendance marked for employee ID: {employee_id}")
        else:
            print(f"Attendance already marked for employee ID: {employee_id}")
    else:
        print(f"Invalid employee ID: {employee_id}")


def scanIntiatiate():
    qr_code_data = read_qr_code_image("employee1.png")
    print("QR code data:", qr_code_data)
    mark_attendance(qr_code_data)
