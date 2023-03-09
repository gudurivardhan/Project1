from PIL import Image
import pyzbar.pyzbar as pyzbar
import pandas as pd
import qrcode
import cv2
class WriteEmpDetails:
    # Create a data sheet with Employee details
    def __init__(self):
        employee_details = pd.DataFrame(
        {"ID": [1, 2, 3, 4], "Name":["Vardhan", "Praveen", "Bhanu", "Raju"]}
        )
        # Write the data to a CSV file
        employee_details.to_csv("employee_details.csv", index=False)
        print("Employee details written to employee_details.csv")

class CrateAttendanceDetails:
    def __init__(self):
        data = {"ID": [],"Name": [],"Attendance": []}
        employee_attendance = pd.DataFrame(data)
        employee_attendance.to_csv("employee_attendance.csv", index=False)

class Read_CSV_file:
    def read_file(self,file_path):
        employee_details = pd.read_csv(file_path)
        return employee_details

class Generate_QR:
    def generate_qr_code(self,employee_id,name):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(f"{employee_id},{name}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = f"employee{employee_id}.png"
        with open(img_path, "wb") as f:
            img.save(f)
        print(f"QR code generated for employee ID: {employee_id}")
        return img_path

class QRScanner:      
    def read_qr_code_data(self):
        cap = cv2.VideoCapture(0)
        while True:
            # read frame from camera
            ret, frame = cap.read()

            # detect QR codes
            decoded_objs = pyzbar.decode(frame)
            print("Got it...")

            # display video stream
            cv2.imshow('frame', frame)

            # check for quit key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # release camera and close window
        
        cap.release()
        cv2.destroyAllWindows()
        return decoded_objs[0].data.decode()


class Mark_Emp_Attendance:    
    def mark_attendance(self, qr_code_data):
        data_items = qr_code_data.split(',')
        employee_id = int(data_items[0])
        emp_name=data_items[1]
        employee_details = Read_CSV_file().read_file("employee_details.csv")
        emp_attendance_details=Read_CSV_file().read_file("employee_attendance.csv")
        if employee_id in employee_details["ID"].values:
            if employee_id not in emp_attendance_details["ID"].values:
                emp_attendance_details = pd.concat([emp_attendance_details, pd.DataFrame({"ID": [employee_id], "Name": [emp_name], "Attendance": ["Present"]})], ignore_index=True)
                emp_attendance_details.to_csv("employee_attendance.csv", index=False)
                print(f"Attendance marked for employee ID: {employee_id}")
            else:
                print(f"Attendance already marked for employee ID: {employee_id}")
        else:
            print(f"Invalid employee ID: {employee_id}")

writeDetails= WriteEmpDetails()
createAttendanceSheet=CrateAttendanceDetails()
employee_details =Read_CSV_file().read_file("employee_details.csv")

qr_genarate=Generate_QR()
employee_details["QR code image"] = ""
for index, row in employee_details.iterrows():
    img_path =qr_genarate.generate_qr_code(row["ID"],row["Name"])
    employee_details.at[index, "QR code image"] = img_path

# Write the updated data to the same CSV file
employee_details.to_csv("employee_details.csv", index=False)

qr_scanner = QRScanner()
qr_code_data = qr_scanner.read_qr_code_data()
print("QR code data:", qr_code_data)

employee_attendance = Mark_Emp_Attendance()
employee_attendance.mark_attendance(qr_code_data)







