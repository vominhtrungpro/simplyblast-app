import tkinter as tk
from tkinter import ttk,messagebox
from pkg.config.config import read_config
from pkg.pickle.pickle import save_token_to_local_storage,load_token_from_local_storage
import requests
import json
from tkcalendar import Calendar


class OkRequest:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

config = read_config()
auth_url = config.get('Url', 'api_url')

def open_new_tenant(app):
    add_tenant = tk.Toplevel(app)
    add_tenant.title("New Window")

    screen_width = add_tenant.winfo_screenwidth()
    screen_height = add_tenant.winfo_screenheight()
    x = (screen_width - 600) // 2
    y = (screen_height - 600) // 2
    
    add_tenant.geometry("600x600+{}+{}".format(x, y))

    label2 = tk.Label(add_tenant, text="Account subscription expire date*")
    label2.pack()

    ased_cal = Calendar(add_tenant, selectmode='day', year=2024, month=2, day=26)
    ased_cal.pack()

    label1 = tk.Label(add_tenant, text="Sales in charge*")
    label1.pack()

    values = ('Company', 'Team A', 'Team B')  
    sales_in_charge_ccb = ttk.Combobox(add_tenant, state="readonly")
    sales_in_charge_ccb['values'] = values
    sales_in_charge_ccb.current(0) 
    sales_in_charge_ccb.pack()

    label2 = tk.Label(add_tenant, text="Billing Company Name*")
    label2.pack()

    entry_billing_company_name = tk.Entry(add_tenant)
    entry_billing_company_name.pack()

    label3 = tk.Label(add_tenant, text="Billing Company UEN*")
    label3.pack()

    entry_billing_company_uen = tk.Entry(add_tenant)
    entry_billing_company_uen.pack()

    label4 = tk.Label(add_tenant, text="Billing Business Unit*")
    label4.pack()

    entry_billing_business_unit = tk.Entry(add_tenant)
    entry_billing_business_unit.pack()

    label5 = tk.Label(add_tenant, text="Billing Contact Person*")
    label5.pack()

    entry_billing_contact_person = tk.Entry(add_tenant)
    entry_billing_contact_person.pack()

    label6 = tk.Label(add_tenant, text="Billing Contact Email*")
    label6.pack()

    entry_billing_contact_email = tk.Entry(add_tenant)
    entry_billing_contact_email.pack()

    label7 = tk.Label(add_tenant, text="Billing Contact Number*")
    label7.pack()

    entry_billing_contact_number = tk.Entry(add_tenant)
    entry_billing_contact_number.pack()

    inner_frame = tk.Frame(add_tenant, width=100, height=100)
    inner_frame.pack()

    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(inner_frame, variable=var, onvalue=True, offvalue=False)
    checkbox.pack(side=tk.LEFT)

    label8 = tk.Label(inner_frame, text="Use Credit*")
    label8.pack(side=tk.LEFT)

    label9 = tk.Label(add_tenant, text="Choose Waba*")
    label9.pack()

    wabas = get_wabas()
    waba_numbers = []  

    for waba in wabas: 
        waba_numbers.append(waba.get("wabaNumber"))

    wabas_ccb = ttk.Combobox(add_tenant, state="readonly")
    wabas_ccb['values'] = waba_numbers
    wabas_ccb.current(0) 
    wabas_ccb.pack()

    inner_frame2 = tk.Frame(add_tenant, width=100, height=100)
    inner_frame2.pack()

    ok_button = tk.Button(inner_frame2, text="OK",command=lambda: ok(OkRequest(sales_in_charge_ccb.get(), wabas.get())))
    ok_button.pack(side=tk.LEFT,padx=10,pady=10)

    back_button = tk.Button(inner_frame2, text="Back", command=add_tenant.destroy)
    back_button.pack(side=tk.LEFT,padx=10,pady=10)
    
    add_tenant.grab_set()

    add_tenant.protocol("WM_DELETE_WINDOW", enable_root_window)

def enable_root_window(app):
    app.grab_release()

def ok(request):
    print("Selected Sales in charge1:", request.value1)
    print("Selected wabas:", request.value2)

def get_wabas():
    url = auth_url + '/waba'
    access_token = ''

    access_token = load_token_from_local_storage()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
        }

    response = requests.get(url, headers=headers)

    response_data = json.loads(response.text)

    isSuccess = response_data.get("isSuccess")

    if isSuccess == True:
        return response_data.get("data", {})

    else:
        messagebox.showerror("Lỗi", "Search wabas")



