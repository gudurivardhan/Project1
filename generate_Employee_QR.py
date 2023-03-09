import pandas as pd
import qrcode


def generate_qr_code(employee_id, name):
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


def read_employee_details(file_path):
    employee_details = pd.read_csv(file_path)
    return employee_details


def initiateGeneration():
    employee_details = read_employee_details("employee_details.csv")
    employee_details["QR code image"] = ""
    for index, row in employee_details.iterrows():
        img_path = generate_qr_code(row["ID"], row["Name"])
        employee_details.at[index, "QR code image"] = img_path

    # Write the updated data to the same CSV file
    employee_details.to_csv("employee_details.csv", index=False)
