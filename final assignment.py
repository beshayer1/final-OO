import tkinter as tk
from tkinter import messagebox
import pickle


class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                 catering_company, cleaning_company, decorations_company, entertainment_company,
                 furniture_supply_company,
                 invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice


class Employee:
    def __init__(self, emp_id, name, department, job_title, basic_salary, age, dob, passport_details):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details


class Client:
    def __init__(self, client_id, name, address, contact, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact = contact
        self.budget = budget


class Guest:
    def __init__(self, guest_id, name, address, contact):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact = contact


class Supplier:
    def __init__(self, supplier_id, name, address, contact):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact = contact


class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests


def add_event(event):
    events = load_data("events_data.pkl")
    events.append(event)
    save_data(events, "events_data.pkl")


def delete_event(event_id):
    events = load_data("events_data.pkl")
    for event in events:
        if event.event_id == event_id:
            events.remove(event)
            save_data(events, "events_data.pkl")
            return True
    return False


def modify_event(event_id, new_event_data):
    events = load_data("events_data.pkl")
    for event in events:
        if event.event_id == event_id:
            event.__dict__.update(new_event_data)
            save_data(events, "events_data.pkl")
            return True
    return False


def display_event(event_id):
    events = load_data("events_data.pkl")
    for event in events:
        if event.event_id == event_id:
            return event.__dict__
    return None


def add_employee(employee):
    employees.append(employee)
    save_data(employees, "employees_data.pkl")


def delete_employee(emp_id):
    for employee in employees:
        if employee.emp_id == emp_id:
            employees.remove(employee)
            save_data(employees, "employees_data.pkl")
            return True
    return False


def modify_employee(emp_id, new_employee_data):
    for employee in employees:
        if employee.emp_id == emp_id:
            employee.__dict__.update(new_employee_data)
            save_data(employees, "employees_data.pkl")
            return True
    return False


def display_employee(emp_id):
    for employee in employees:
        if employee.emp_id == emp_id:
            return employee.__dict__
    return None


def add_client(client):
    clients.append(client)
    save_data(clients, "clients_data.pkl")


def delete_client(client_id):
    for client in clients:
        if client.client_id == client_id:
            clients.remove(client)
            save_data(clients, "clients_data.pkl")
            return True
    return False


def modify_client(client_id, new_client_data):
    for client in clients:
        if client.client_id == client_id:
            client.__dict__.update(new_client_data)
            save_data(clients, "clients_data.pkl")
            return True
    return False


def display_client(client_id):
    for client in clients:
        if client.client_id == client_id:
            return client.__dict__
    return None


def add_guest(guest):
    guests.append(guest)
    save_data(guests, "guests_data.pkl")


def delete_guest(guest_id):
    for guest in guests:
        if guest.guest_id == guest_id:
            guests.remove(guest)
            save_data(guests, "guests_data.pkl")
            return True
    return False


def modify_guest(guest_id, new_guest_data):
    for guest in guests:
        if guest.guest_id == guest_id:
            guest.__dict__.update(new_guest_data)
            save_data(guests, "guests_data.pkl")
            return True
    return False


def display_guest(guest_id):
    for guest in guests:
        if guest.guest_id == guest_id:
            return guest.__dict__
    return None


def add_supplier(supplier):
    suppliers.append(supplier)
    save_data(suppliers, "suppliers_data.pkl")


def delete_supplier(supplier_id):
    for supplier in suppliers:
        if supplier.supplier_id == supplier_id:
            suppliers.remove(supplier)
            save_data(suppliers, "suppliers_data.pkl")
            return True
    return False


def modify_supplier(supplier_id, new_supplier_data):
    for supplier in suppliers:
        if supplier.supplier_id == supplier_id:
            supplier.__dict__.update(new_supplier_data)
            save_data(suppliers, "suppliers_data.pkl")
            return True
    return False


def display_supplier(supplier_id):
    for supplier in suppliers:
        if supplier.supplier_id == supplier_id:
            return supplier.__dict__
    return None


def add_venue(venue):
    venues.append(venue)
    save_data(venues, "venues_data.pkl")


def delete_venue(venue_id):
    for venue in venues:
        if venue.venue_id == venue_id:
            venues.remove(venue)
            save_data(venues, "venues_data.pkl")
            return True
    return False


def modify_venue(venue_id, new_venue_data):
    for venue in venues:
        if venue.venue_id == venue_id:
            venue.__dict__.update(new_venue_data)
            save_data(venues, "venues_data.pkl")
            return True
    return False


def display_venue(venue_id):
    for venue in venues:
        if venue.venue_id == venue_id:
            return venue.__dict__
    return None


def save_data(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_data(filename):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return []


employees = load_data("employees_data.pkl")
clients = load_data("clients_data.pkl")
guests = load_data("guests_data.pkl")
events = load_data("events_data.pkl")
suppliers = load_data("suppliers_data.pkl")
venues = load_data("venues_data.pkl")


def add_event_gui():
    top = tk.Toplevel()
    top.title("Add Event")

    tk.Label(top, text="Event ID:").grid(row=0, column=0)
    tk.Label(top, text="Type:").grid(row=1, column=0)
    tk.Label(top, text="Theme:").grid(row=2, column=0)
    tk.Label(top, text="Date:").grid(row=3, column=0)
    tk.Label(top, text="Time:").grid(row=4, column=0)
    tk.Label(top, text="Duration:").grid(row=5, column=0)
    tk.Label(top, text="Venue Address:").grid(row=6, column=0)
    tk.Label(top, text="Client ID:").grid(row=7, column=0)
    tk.Label(top, text="Guest List:").grid(row=8, column=0)
    tk.Label(top, text="Catering Company:").grid(row=9, column=0)
    tk.Label(top, text="Cleaning Company:").grid(row=10, column=0)
    tk.Label(top, text="Decorations Company:").grid(row=11, column=0)
    tk.Label(top, text="Entertainment Company:").grid(row=12, column=0)
    tk.Label(top, text="Furniture Supply Company:").grid(row=13, column=0)
    tk.Label(top, text="Invoice:").grid(row=14, column=0)

    event_id_entry = tk.Entry(top)
    event_type_entry = tk.Entry(top)
    theme_entry = tk.Entry(top)
    date_entry = tk.Entry(top)
    time_entry = tk.Entry(top)
    duration_entry = tk.Entry(top)
    venue_address_entry = tk.Entry(top)
    client_id_entry = tk.Entry(top)
    guest_list_entry = tk.Entry(top)
    catering_company_entry = tk.Entry(top)
    cleaning_company_entry = tk.Entry(top)
    decorations_company_entry = tk.Entry(top)
    entertainment_company_entry = tk.Entry(top)
    furniture_supply_company_entry = tk.Entry(top)
    invoice_entry = tk.Entry(top)

    event_id_entry.grid(row=0, column=1)
    event_type_entry.grid(row=1, column=1)
    theme_entry.grid(row=2, column=1)
    date_entry.grid(row=3, column=1)
    time_entry.grid(row=4, column=1)
    duration_entry.grid(row=5, column=1)
    venue_address_entry.grid(row=6, column=1)
    client_id_entry.grid(row=7, column=1)
    guest_list_entry.grid(row=8, column=1)
    catering_company_entry.grid(row=9, column=1)
    cleaning_company_entry.grid(row=10, column=1)
    decorations_company_entry.grid(row=11, column=1)
    entertainment_company_entry.grid(row=12, column=1)
    furniture_supply_company_entry.grid(row=13, column=1)
    invoice_entry.grid(row=14, column=1)

   

    def save_event():
        try:
            event_id = int(event_id_entry.get())
            event_type = event_type_entry.get()
            theme = theme_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            duration = duration_entry.get()
            venue_address = venue_address_entry.get()
            client_id = int(client_id_entry.get())
            guest_list = guest_list_entry.get()
            catering_company = catering_company_entry.get()
            cleaning_company = cleaning_company_entry.get()
            decorations_company = decorations_company_entry.get()
            entertainment_company = entertainment_company_entry.get()
            furniture_supply_company = furniture_supply_company_entry.get()
            invoice = invoice_entry.get()

            event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                          catering_company, cleaning_company, decorations_company, entertainment_company,
                          furniture_supply_company, invoice)

            add_event(event)

            messagebox.showinfo("Success", "Event added successfully.")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    tk.Button(top, text="Save", command=save_event).grid(row=15, columnspan=2)


def add_employee_gui():
    top = tk.Toplevel()
    top.title("Add Employee")

    tk.Label(top, text="Employee ID:").grid(row=0, column=0)
    tk.Label(top, text="Name:").grid(row=1, column=0)
    tk.Label(top, text="Department:").grid(row=2, column=0)
    tk.Label(top, text="Job Title:").grid(row=3, column=0)
    tk.Label(top, text="Basic Salary:").grid(row=4, column=0)
    tk.Label(top, text="Age:").grid(row=5, column=0)
    tk.Label(top, text="Date of Birth:").grid(row=6, column=0)
    tk.Label(top, text="Passport Details:").grid(row=7, column=0)

    emp_id_entry = tk.Entry(top)
    name_entry = tk.Entry(top)
    department_entry = tk.Entry(top)
    job_title_entry = tk.Entry(top)
    basic_salary_entry = tk.Entry(top)
    age_entry = tk.Entry(top)
    dob_entry = tk.Entry(top)
    passport_details_entry = tk.Entry(top)

    emp_id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    department_entry.grid(row=2, column=1)
    job_title_entry.grid(row=3, column=1)
    basic_salary_entry.grid(row=4, column=1)
    age_entry.grid(row=5, column=1)
    dob_entry.grid(row=6, column=1)
    passport_details_entry.grid(row=7, column=1)

    def save_employee():
        try:
            emp_id = int(emp_id_entry.get())
            name = name_entry.get()
            department = department_entry.get()
            job_title = job_title_entry.get()
            basic_salary = float(basic_salary_entry.get())
            age = int(age_entry.get())
            dob = dob_entry.get()
            passport_details = passport_details_entry.get()

            employee = Employee(emp_id, name, department, job_title, basic_salary, age, dob, passport_details)
            add_employee(employee)
            messagebox.showinfo("Success", "Employee added successfully.")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    tk.Button(top, text="Save", command=save_employee).grid(row=8, columnspan=2)


def add_client_gui():
    top = tk.Toplevel()
    top.title("Add Client")

    tk.Label(top, text="Client ID:").grid(row=0, column=0)
    tk.Label(top, text="Name:").grid(row=1, column=0)
    tk.Label(top, text="Address:").grid(row=2, column=0)
    tk.Label(top, text="Contact:").grid(row=3, column=0)
    tk.Label(top, text="Budget:").grid(row=4, column=0)

    client_id_entry = tk.Entry(top)
    name_entry = tk.Entry(top)
    address_entry = tk.Entry(top)
    contact_entry = tk.Entry(top)
    budget_entry = tk.Entry(top)

    client_id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    contact_entry.grid(row=3, column=1)
    budget_entry.grid(row=4, column=1)

    def save_client():
        try:
            client_id = int(client_id_entry.get())
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            budget = float(budget_entry.get())

            client = Client(client_id, name, address, contact, budget)
            add_client(client)
            messagebox.showinfo("Success", "Client added successfully.")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    tk.Button(top, text="Save", command=save_client).grid(row=5, columnspan=2)

    def delete_client_gui():
        top = tk.Toplevel()
        top.title("Delete Client")

        tk.Label(top, text="Client ID:").grid(row=0, column=0)
        client_id_entry = tk.Entry(top)
        client_id_entry.grid(row=0, column=1)

        def delete_client():
            try:
                client_id = int(client_id_entry.get())
                if delete_client(client_id):
                    messagebox.showinfo("Success", "Client deleted successfully.")
                else:
                    messagebox.showerror("Error", "Client not found.")
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input.")

        tk.Button(top, text="Delete", command=delete_client).grid(row=1, columnspan=2)

    def modify_client_gui():
        top = tk.Toplevel()
        top.title("Modify Client")

        tk.Label(top, text="Client ID:").grid(row=0, column=0)
        client_id_entry = tk.Entry(top)
        client_id_entry.grid(row=0, column=1)

        def modify_client():
            try:
                client_id = int(client_id_entry.get())
                new_client_data = {} 
                if modify_client(client_id, new_client_data):
                    messagebox.showinfo("Success", "Client modified successfully.")
                else:
                    messagebox.showerror("Error", "Client not found.")
                top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input.")

        tk.Button(top, text="Modify", command=modify_client).grid(row=5, columnspan=2)


def add_guest_gui():
    top = tk.Toplevel()
    top.title("Add Guest")

    tk.Label(top, text="Guest ID:").grid(row=0, column=0)
    tk.Label(top, text="Name:").grid(row=1, column=0)
    tk.Label(top, text="Address:").grid(row=2, column=0)
    tk.Label(top, text="Contact:").grid(row=3, column=0)

    guest_id_entry = tk.Entry(top)
    name_entry = tk.Entry(top)
    address_entry = tk.Entry(top)
    contact_entry = tk.Entry(top)

    guest_id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    contact_entry.grid(row=3, column=1)

    def save_guest():
        try:
            guest_id = int(guest_id_entry.get())
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()

            guest = Guest(guest_id, name, address, contact)
            add_guest(guest)
            messagebox.showinfo("Success", "Guest added successfully.")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    tk.Button(top, text="Save", command=save_guest).grid(row=4, columnspan=2)


def add_supplier_gui():
    top = tk.Toplevel()
    top.title("Add Supplier")

    tk.Label(top, text="Supplier ID:").grid(row=0, column=0)
    tk.Label(top, text="Name:").grid(row=1, column=0)
    tk.Label(top, text="Address:").grid(row=2, column=0)
    tk.Label(top, text="Contact:").grid(row=3, column=0)

    supplier_id_entry = tk.Entry(top)
    name_entry = tk.Entry(top)
    address_entry = tk.Entry(top)
    contact_entry = tk.Entry(top)

    supplier_id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    contact_entry.grid(row=3, column=1)

    def save_supplier():
        try:
            supplier_id = int(supplier_id_entry.get())
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()

            supplier = Supplier(supplier_id, name, address, contact)
            add_supplier(supplier)
            messagebox.showinfo("Success", "Supplier added successfully.")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    tk.Button(top, text="Save", command=save_supplier).grid(row=4, columnspan=2)


def add_venue_gui():
    top = tk.Toplevel()
    top.title("Add Venue")

    tk.Label(top, text="Venue ID:").grid(row=0, column=0)
    tk.Label(top, text="Name:").grid(row=1, column=0)
    tk.Label(top, text="Address:").grid(row=2, column=0)
    tk.Label(top, text="Contact:").grid(row=3, column=0)
    tk.Label(top, text="Minimum Guests:").grid(row=4, column=0)
    tk.Label(top, text="Maximum Guests:").grid(row=5, column=0)

    venue_id_entry = tk.Entry(top)
    name_entry = tk.Entry(top)
    address_entry = tk.Entry(top)
    contact_entry = tk.Entry(top)
    min_guests_entry = tk.Entry(top)
    max_guests_entry = tk.Entry(top)

    venue_id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    contact_entry.grid(row=3, column=1)
    min_guests_entry.grid(row=4, column=1)
    max_guests_entry.grid(row=5, column=1)

    def save_venue():
        try:
            venue_id = int(venue_id_entry.get())
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            min_guests = int(min_guests_entry.get())
            max_guests = int(max_guests_entry.get())

            venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
            add_venue(venue)
            messagebox.showinfo("Success", "Venue added successfully.")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")

    tk.Button(top, text="Save", command=save_venue).grid(row=6, columnspan=2)


root = tk.Tk()
root.title("Events Management System")

add_event_button = tk.Button(root, text="Add Event", command=add_event_gui)
add_event_button.pack()

add_employee_button = tk.Button(root, text="Add Employee", command=add_employee_gui)
add_employee_button.pack()

add_client_button = tk.Button(root, text="Add Client", command=add_client_gui)
add_client_button.pack()

add_guest_button = tk.Button(root, text="Add Guest", command=add_guest_gui)
add_guest_button.pack()

add_supplier_button = tk.Button(root, text="Add Supplier", command=add_supplier_gui)
add_supplier_button.pack()

add_venue_button = tk.Button(root, text="Add Venue", command=add_venue_gui)
add_venue_button.pack()

root.mainloop()
