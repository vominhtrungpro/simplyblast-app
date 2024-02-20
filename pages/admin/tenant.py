import tkinter as tk
from tkinter import ttk, messagebox
from pkg.config.config import read_config
from pkg.token.token import TokenManager
import requests
import json
import shelve
from pkg.pickle.pickle import save_token_to_local_storage,load_token_from_local_storage

default_page_index = 1
default_page_size = 5
default_sort_field_name = "Id"
default_sort_field_status = True
default_filter_name = ""

config = read_config()
auth_url = config.get('Url', 'api_url')

token_manager = TokenManager()

def create_tenant(navbar_frame,main_window,main_layout):
    for widget in navbar_frame.winfo_children():
        widget.destroy()

    inner_frame = tk.Frame(navbar_frame, width=100, height=100)
    inner_frame.pack(side="top", anchor="ne")

    changepassword_button = tk.Label(inner_frame, text="Change password", height=2)
    changepassword_button.config(font=("Arial", 12))
    changepassword_button.pack(padx=20)

    logout_button = tk.Label(inner_frame, text="Logout", height=2)
    logout_button.config(font=("Arial", 12))
    logout_button.pack(padx=20)
    logout_button.bind("<Button-1>", lambda event: back_to_login(main_window, main_layout))

    inner_frame2 = tk.Frame(navbar_frame, width=100, height=100)
    inner_frame2.pack(side="top", anchor="nw")

    tenants_label = tk.Label(inner_frame2, text="Tenants", height=2)
    tenants_label.config(font=("Arial", 16))
    tenants_label.pack(padx=20)
    tenants_label.bind("<Button-1>", lambda event: print("Label clicked"))

    inner_frame3 = tk.Frame(navbar_frame, width=200, height=100)
    inner_frame3.pack(side="top", anchor="ne")

    new_button = tk.Button(inner_frame3,text="New",width=10,height=2)
    new_button.pack(padx=20)

    inner_frame4 = tk.Frame(navbar_frame, width=1200, height=100)
    inner_frame4.pack(side="top")

    entry = tk.Text(inner_frame4, width=100,height=1)
    entry.grid(row=0, column=0, padx=10, pady=10)

    inner_frame5 = tk.Frame(navbar_frame, width=1200,height=600)

    inner_frame6 = tk.Frame(navbar_frame, width=1200,height=600)

    search_button = tk.Button(inner_frame4, text="Search", command=lambda: update_table(entry,inner_frame5,inner_frame6))
    search_button.grid(row=0, column=1, padx=10, pady=10)

    
    inner_frame5.pack(side="top")

    response = search(default_page_index,default_page_size,default_sort_field_name,default_sort_field_status,default_filter_name)

    table = DataTable(inner_frame5, response['data'])
    table.pack(expand=True, fill="both")

    
    inner_frame6.pack(side="top")

    previous_button = tk.Button(inner_frame6, text="Previous", command=previous_page)
    previous_button.grid(row=0, column=0)

    num_pages = response['numOfPages']
    for i in range(num_pages):
        page_button = tk.Button(inner_frame6, text=str(i+1), command=lambda num=i+1: goto_page(num))
        page_button.grid(row=0, column=i+1,padx=1)

    next_button = tk.Button(inner_frame6, text="Next", command=next_page)
    next_button.grid(row=0, column=num_pages+1)

    return navbar_frame

def previous_page():
    pass  

def next_page():
    pass  

def goto_page(page_num):
    pass 

def update_table(text,frame5,frame6):
    for widget1 in frame5.winfo_children():
        widget1.destroy()

    hel = text.get("1.0", "end-1c")

    response = search(default_page_index,default_page_size,default_sort_field_name,default_sort_field_status,hel)
        
    table = DataTable(frame5, response['data'])
    table.pack(expand=True, fill="both")

    for widget2 in frame6.winfo_children():
        widget2.destroy()

    previous_button = tk.Button(frame6, text="Previous", command=previous_page)
    previous_button.grid(row=0, column=0)

    num_pages = response['numOfPages']
    for i in range(num_pages):
        page_button = tk.Button(frame6, text=str(i+1), command=lambda num=i+1: goto_page(num))
        page_button.grid(row=0, column=i+1,padx=1)

    next_button = tk.Button(frame6, text="Next", command=next_page)
    next_button.grid(row=0, column=num_pages+1)

class DataTable(tk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.data = data
        self.current_page = 0
        self.create_table()

    def create_table(self):
        # Create headings
        headings = ["Company name", "Waba number", "Sales in charge","Credit balance","Subscription Expiry Date","Account status"]
        for col_index, heading in enumerate(headings):
            label = tk.Label(self, text=heading, relief=tk.RIDGE, width=25)
            label.grid(row=0, column=col_index, sticky="nsew")

        # Create data cells
        for row_index, row_data in enumerate(self.data, start=1):
            for col_index, key in enumerate(["tenantName", "wabaNumber", "saleInCharge","currentBalance","accSubExpireDate","status"]):
                value = row_data.get(key, "")
                label = tk.Label(self, text=value, relief=tk.RIDGE, width=25)
                label.grid(row=row_index, column=col_index, sticky="nsew")
            button = tk.Button(self, text="Button", command=lambda row=row_index: self.button_click(row))
            button.grid(row=row_index, column=len(headings), sticky="nsew")

        # Configure grid rows and columns to expand properly
        for i in range(len(headings)):
            self.grid_columnconfigure(i, weight=1)
        for i in range(len(self.data) + 1):
            self.grid_rowconfigure(i, weight=1)

    def button_click(self, row):
        row_data = self.data[row - 1]
        print("ID:", row_data["id"])

def search(page_index,page_size,sort_field_name,sort_field_status,filter_name):
    url = auth_url + '/tenant/search'
    access_token = ''

    access_token = load_token_from_local_storage()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
        }
    data = {
        "pageIndex": page_index,
        "pageSize": page_size,
        "filters": [
            {
                "fieldName": "Company name",
                "value": filter_name,
                "operation": 0
            }
        ],
        "sortBy": {
            "fieldName": sort_field_name,
            "ascending": sort_field_status
        }
    }

    response = requests.post(url, json=data, headers=headers)

    response_data = json.loads(response.text)

    isSuccess = response_data.get("isSuccess")

    if isSuccess == True:
        if data:
            return response_data.get("data", {})
    else:
        messagebox.showerror("Lỗi", "Search tenant")
    

def back_to_login(main_window, dashboard):
    dashboard.destroy()
    main_window.deiconify()
    

