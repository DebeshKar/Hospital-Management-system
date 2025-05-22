import tkinter as tk
from tkinter import messagebox, simpledialog
import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet

def AppointmentIndexInDoctorsDataBase(patient_ID):
    for i in Doctors_DataBase:
        for j in Doctors_DataBase[i]:
            if str(patient_ID) == str(j[0]):
                Appointment_index = Doctors_DataBase[i].index(j)
                return Appointment_index, i
    return None, None

def read_databases():
    global Pateints_DataBase, Doctors_DataBase
    Pateints_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
    Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()

def write_databases():
    Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Pateints_DataBase)
    Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)

def admin_mode():
    password = simpledialog.askstring("Admin Login", "Please enter your password:", show='*')
    if password == "1234":
        admin_options()
    else:
        messagebox.showerror("Error", "Incorrect Password")

def admin_options():
    def manage_patients():
        patient_window = tk.Toplevel(root)
        patient_window.title("Manage Patients")

        def add_patient():
            try:
                patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
                if patient_ID in Pateints_DataBase:
                    messagebox.showerror("Error", "This ID is unavailable")
                    return
                Department = simpledialog.askstring("Input", "Enter patient department:")
                DoctorName = simpledialog.askstring("Input", "Enter doctor following the case:")
                Name = simpledialog.askstring("Input", "Enter patient name:")
                Age = simpledialog.askstring("Input", "Enter patient age:")
                Gender = simpledialog.askstring("Input", "Enter patient gender:")
                Address = simpledialog.askstring("Input", "Enter patient address:")
                RoomNumber = simpledialog.askstring("Input", "Enter patient room number:")
                Pateints_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address, RoomNumber]
                messagebox.showinfo("Success", "Patient added successfully")
            except ValueError:
                messagebox.showerror("Error", "Patient ID should be an integer")

        def display_patient():
            try:
                patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
                if patient_ID not in Pateints_DataBase:
                    messagebox.showerror("Error", "Incorrect ID")
                    return
                data = Pateints_DataBase[patient_ID]
                messagebox.showinfo("Patient Data", f"Name: {data[2]}\nAge: {data[3]}\nGender: {data[4]}\nAddress: {data[5]}\nRoom: {data[6]}\nDepartment: {data[0]}\nDoctor: {data[1]}")
            except ValueError:
                messagebox.showerror("Error", "Patient ID should be an integer")

        def delete_patient():
            try:
                patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
                if patient_ID not in Pateints_DataBase:
                    messagebox.showerror("Error", "Incorrect ID")
                    return
                del Pateints_DataBase[patient_ID]
                messagebox.showinfo("Success", "Patient data deleted successfully")
            except ValueError:
                messagebox.showerror("Error", "Patient ID should be an integer")

        def edit_patient():
            try:
                patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
                if patient_ID not in Pateints_DataBase:
                    messagebox.showerror("Error", "Incorrect ID")
                    return
                edit_window = tk.Toplevel(patient_window)
                edit_window.title("Edit Patient Data")

                def update_field(field_index, field_name):
                    new_value = simpledialog.askstring("Input", f"Enter new {field_name}:")
                    if new_value:
                        Pateints_DataBase[patient_ID][field_index] = new_value
                        messagebox.showinfo("Success", f"Patient {field_name} edited successfully")

                tk.Button(edit_window, text="Edit Department", command=lambda: update_field(0, "Department")).pack()
                tk.Button(edit_window, text="Edit Doctor", command=lambda: update_field(1, "Doctor")).pack()
                tk.Button(edit_window, text="Edit Name", command=lambda: update_field(2, "Name")).pack()
                tk.Button(edit_window, text="Edit Age", command=lambda: update_field(3, "Age")).pack()
                tk.Button(edit_window, text="Edit Gender", command=lambda: update_field(4, "Gender")).pack()
                tk.Button(edit_window, text="Edit Address", command=lambda: update_field(5, "Address")).pack()
                tk.Button(edit_window, text="Edit Room Number", command=lambda: update_field(6, "Room Number")).pack()
            except ValueError:
                messagebox.showerror("Error", "Patient ID should be an integer")

        tk.Button(patient_window, text="Add New Patient", command=add_patient).pack()
        tk.Button(patient_window, text="Display Patient", command=display_patient).pack()
        tk.Button(patient_window, text="Delete Patient", command=delete_patient).pack()
        tk.Button(patient_window, text="Edit Patient Data", command=edit_patient).pack()

    def manage_doctors():
        doctor_window = tk.Toplevel(root)
        doctor_window.title("Manage Doctors")

        def add_doctor():
            try:
                Doctor_ID = int(simpledialog.askstring("Input", "Enter doctor ID:"))
                if Doctor_ID in Doctors_DataBase:
                    messagebox.showerror("Error", "This ID is unavailable")
                    return
                Department = simpledialog.askstring("Input", "Enter doctor department:")
                Name = simpledialog.askstring("Input", "Enter doctor name:")
                Address = simpledialog.askstring("Input", "Enter doctor address:")
                Doctors_DataBase[Doctor_ID] = [[Department, Name, Address]]
                messagebox.showinfo("Success", "Doctor added successfully")
            except ValueError:
                messagebox.showerror("Error", "Doctor ID should be an integer")

        def display_doctor():
            try:
                Doctor_ID = int(simpledialog.askstring("Input", "Enter doctor ID:"))
                if Doctor_ID not in Doctors_DataBase:
                    messagebox.showerror("Error", "Incorrect ID")
                    return
                data = Doctors_DataBase[Doctor_ID][0]
                messagebox.showinfo("Doctor Data", f"Name: {data[1]}\nAddress: {data[2]}\nDepartment: {data[0]}")
            except ValueError:
                messagebox.showerror("Error", "Doctor ID should be an integer")

        def delete_doctor():
            try:
                Doctor_ID = int(simpledialog.askstring("Input", "Enter doctor ID:"))
                if Doctor_ID not in Doctors_DataBase:
                    messagebox.showerror("Error", "Incorrect ID")
                    return
                del Doctors_DataBase[Doctor_ID]
                messagebox.showinfo("Success", "Doctor data deleted successfully")
            except ValueError:
                messagebox.showerror("Error", "Doctor ID should be an integer")

        def edit_doctor():
            try:
                Doctor_ID = int(simpledialog.askstring("Input", "Enter doctor ID:"))
                if Doctor_ID not in Doctors_DataBase:
                    messagebox.showerror("Error", "Incorrect ID")
                    return
                edit_window = tk.Toplevel(doctor_window)
                edit_window.title("Edit Doctor Data")

                def update_field(field_index, field_name):
                    new_value = simpledialog.askstring("Input", f"Enter new {field_name}:")
                    if new_value:
                        Doctors_DataBase[Doctor_ID][0][field_index] = new_value
                        messagebox.showinfo("Success", f"Doctor {field_name} edited successfully")

                tk.Button(edit_window, text="Edit Department", command=lambda: update_field(0, "Department")).pack()
                tk.Button(edit_window, text="Edit Name", command=lambda: update_field(1, "Name")).pack()
                tk.Button(edit_window, text="Edit Address", command=lambda: update_field(2, "Address")).pack()
            except ValueError:
                messagebox.showerror("Error", "Doctor ID should be an integer")

        tk.Button(doctor_window, text="Add New Doctor", command=add_doctor).pack()
        tk.Button(doctor_window, text="Display Doctor", command=display_doctor).pack()
        tk.Button(doctor_window, text="Delete Doctor", command=delete_doctor).pack()
        tk.Button(doctor_window, text="Edit Doctor Data", command=edit_doctor).pack()

    def manage_appointments():
        appointment_window = tk.Toplevel(root)
        appointment_window.title("Manage Appointments")

        def book_appointment():
            try:
                Doctor_ID = int(simpledialog.askstring("Input", "Enter the ID of doctor:"))
                if Doctor_ID not in Doctors_DataBase:
                    messagebox.showerror("Error", "Incorrect doctor ID")
                    return
                patient_choice = simpledialog.askstring("Input", "Enter 1 for new patient or 2 for existing patient:")
                if patient_choice == '1':
                    patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
                    if patient_ID in Pateints_DataBase:
                        messagebox.showerror("Error", "This ID is unavailable")
                        return
                    Name = simpledialog.askstring("Input", "Enter patient name:")
                    Age = simpledialog.askstring("Input", "Enter patient age:")
                    Gender = simpledialog.askstring("Input", "Enter patient gender:")
                    Address = simpledialog.askstring("Input", "Enter patient address:")
                    Pateints_DataBase[patient_ID] = ["", Doctor_ID, Name, Age, Gender, Address, ""]
                    Appointment_Date = simpledialog.askstring("Input", "Enter appointment date:")
                    Doctors_DataBase[Doctor_ID].append([patient_ID, Name, Appointment_Date])
                    messagebox.showinfo("Success", "Appointment booked successfully")
                elif patient_choice == '2':
                    patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
                    if patient_ID not in Pateints_DataBase:
                        messagebox.showerror("Error", "Incorrect patient ID")
                        return
                    Name = Pateints_DataBase[patient_ID][2]
                    Appointment_Date = simpledialog.askstring("Input", "Enter appointment date:")
                    Doctors_DataBase[Doctor_ID].append([patient_ID, Name, Appointment_Date])
                    messagebox.showinfo("Success", "Appointment booked successfully")
                else:
                    messagebox.showerror("Error", "Invalid choice")
            except ValueError:
                messagebox.showerror("Error", "ID should be an integer")

        def display_appointment():
            try:
                Doctor_ID = int(simpledialog.askstring("Input", "Enter doctor ID:"))
                if Doctor_ID not in Doctors_DataBase:
                    messagebox.showerror("Error", "Incorrect doctor ID")
                    return
                for i, data in enumerate(Doctors_DataBase[Doctor_ID]):
                    if i == 0:  # Skip doctor information
                        continue
                    messagebox.showinfo("Appointment Data", f"Appointment {i}:\nPatient ID: {data[0]}\nPatient Name: {data[1]}\nAppointment Date: {data[2]}")
            except ValueError:
                messagebox.showerror("Error", "Doctor ID should be an integer")

        def delete_appointment():
            try:
                patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
                Appointment_index, Doctor_ID = AppointmentIndexInDoctorsDataBase(patient_ID)
                if Appointment_index is None:
                    messagebox.showerror("Error", "Incorrect patient ID")
                    return
                del Doctors_DataBase[Doctor_ID][Appointment_index]
                messagebox.showinfo("Success", "Appointment deleted successfully")
            except ValueError:
                messagebox.showerror("Error", "Patient ID should be an integer")

        tk.Button(appointment_window, text="Book Appointment", command=book_appointment).pack()
        tk.Button(appointment_window, text="Display Appointment", command=display_appointment).pack()
        tk.Button(appointment_window, text="Delete Appointment", command=delete_appointment).pack()

    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Mode")
    tk.Button(admin_window, text="Manage Patients", command=manage_patients).pack()
    tk.Button(admin_window, text="Manage Doctors", command=manage_doctors).pack()
    tk.Button(admin_window, text="Manage Appointments", command=manage_appointments).pack()

def user_mode():
    user_window = tk.Toplevel(root)
    user_window.title("User Mode")

    def display_patient():
        try:
            patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
            if patient_ID not in Pateints_DataBase:
                messagebox.showerror("Error", "Incorrect ID")
                return
            data = Pateints_DataBase[patient_ID]
            messagebox.showinfo("Patient Data", f"Name: {data[2]}\nAge: {data[3]}\nGender: {data[4]}\nAddress: {data[5]}\nRoom: {data[6]}\nDepartment: {data[0]}\nDoctor: {data[1]}")
        except ValueError:
            messagebox.showerror("Error", "Patient ID should be an integer")

    def display_appointment():
        try:
            patient_ID = int(simpledialog.askstring("Input", "Enter patient ID:"))
            Appointment_index, Doctor_ID = AppointmentIndexInDoctorsDataBase(patient_ID)
            if Appointment_index is None:
                messagebox.showerror("Error", "Incorrect patient ID")
                return
            data = Doctors_DataBase[Doctor_ID][Appointment_index]
            messagebox.showinfo("Appointment Data", f"Patient ID: {data[0]}\nPatient Name: {data[1]}\nAppointment Date: {data[2]}")
        except ValueError:
            messagebox.showerror("Error", "Patient ID should be an integer")

    tk.Button(user_window, text="Display Patient Data", command=display_patient).pack()
    tk.Button(user_window, text="Display Appointment Data", command=display_appointment).pack()

# Initialize databases
read_databases()

# Create the main window
root = tk.Tk()
root.title("Hospital Management System")

tk.Label(root, text="Welcome to the Hospital Management System").pack()

tk.Button(root, text="Admin Mode", command=admin_mode).pack()
tk.Button(root, text="User Mode", command=user_mode).pack()

root.mainloop()

# Save databases when closing the application
root.protocol("WM_DELETE_WINDOW", lambda: (write_databases(), root.destroy()))

