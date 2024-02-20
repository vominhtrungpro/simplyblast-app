import tkinter as tk

def create_tenant(navbar_frame):
    for widget in navbar_frame.winfo_children():
        widget.destroy()

    inner_frame = tk.Frame(navbar_frame, width=100, height=100)
    inner_frame.pack(side="top", anchor="ne")

    changepassword_button = tk.Label(inner_frame, text="Change password", height=2)
    changepassword_button.config(font=("Arial", 12))
    changepassword_button.pack(padx=20)
    changepassword_button.bind("<Button-1>", lambda event: print("Label clicked"))

    logout_button = tk.Label(inner_frame, text="Logout", height=2)
    logout_button.config(font=("Arial", 12))
    logout_button.pack(padx=20)
    logout_button.bind("<Button-1>", lambda event: print("Label clicked"))

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

    search_button = tk.Button(inner_frame4, text="Search", command=lambda: print("Text in the TextBox:", entry.get()))
    search_button.grid(row=0, column=1, padx=10, pady=10)

    inner_frame5 = tk.Frame(navbar_frame, width=1200,height=600)
    inner_frame5.pack(side="top")

    data = [
        {"id": "33892667-eda5-4d20-1e4b-08dac3b95ed7", "tenantName": "UAT Tenant 2", "wabaNumber": "+886 903 444 62",
        "accSubExpireDate": "2023-11-16T23:59:59", "saleInCharge": "Team A", "billingCompanyName": "UAT Tenant 2",
        "billingCompanyUEN": "GOA", "billingCompanyUnit": "BUS_UNIT_TBL_BI", "billingContactPerson": "GOA",
        "billingContactEmail": "ervin.khoo@smsdome.com", "billingContactNumber": "84921870531", "preferredCurrency": "SGD",
        "currentBalance": 156.63339999999954, "setLowCreditCardWarningLevel": 502, "dataRentionPeriod": 550, "status": 1},
        {"id": "eb7f7897-5c4d-46b3-1e4c-08dac3b95ed7", "tenantName": "UAT Tenant 1", "wabaNumber": "+46 76 514 69 99",
        "accSubExpireDate": "2024-03-22T23:59:58", "saleInCharge": "Company", "billingCompanyName": "UAT Tenant 1",
        "billingCompanyUEN": " 6001665870", "billingCompanyUnit": "Singtel VN", "billingContactPerson": "Chinh Nguyen",
        "billingContactEmail": "ervin.khoo@smsdome.com", "billingContactNumber": "84901530015", "preferredCurrency": "SGD",
        "currentBalance": 334.2309000000803, "setLowCreditCardWarningLevel": 484, "dataRentionPeriod": 30, "status": 1},
        {"id": "8544b707-d3c7-4c7f-128c-08dacd1df085", "tenantName": "UAT Tenant 3", "wabaNumber": "UAT Tenant 3",
        "accSubExpireDate": "2023-04-29T23:59:59", "saleInCharge": "Team A", "billingCompanyName": "UAT Tenant 3",
        "billingCompanyUEN": "UAT Tenant 3", "billingCompanyUnit": "UAT Tenant 3", "billingContactPerson": "UAT Tenant 3",
        "billingContactEmail": "UAT Tenant 3", "billingContactNumber": "UAT Tenant 3", "preferredCurrency": "SGD",
        "currentBalance": 40, "setLowCreditCardWarningLevel": 550, "dataRentionPeriod": 0, "status": 1},
        {"id": "96695981-7322-42d1-4ca1-08db5aa86850", "tenantName": "a", "wabaNumber": "+46 76 514 69 99",
        "accSubExpireDate": "2023-08-30T23:59:59", "saleInCharge": "Company", "billingCompanyName": "a",
        "billingCompanyUEN": "a", "billingCompanyUnit": "a", "billingContactPerson": "a",
        "billingContactEmail": "binh.phan@s3corp.com.vn", "billingContactNumber": "1", "preferredCurrency": "SGD",
        "currentBalance": -3, "setLowCreditCardWarningLevel": 550, "dataRentionPeriod": 0, "status": 0},
        {"id": "09bf9d9a-7a2a-4714-995c-08db72cc23b1", "tenantName": "test", "wabaNumber": "+6580286591",
        "accSubExpireDate": "2023-06-23T23:59:59", "saleInCharge": "Company", "billingCompanyName": "test",
        "billingCompanyUEN": "test", "billingCompanyUnit": "test", "billingContactPerson": "test",
        "billingContactEmail": "test@test.test", "billingContactNumber": "test", "preferredCurrency": "SGD",
        "currentBalance": -1, "setLowCreditCardWarningLevel": 550, "dataRentionPeriod": 0, "status": 1}
]

    table = DataTable(inner_frame5, data)
    table.pack(expand=True, fill="both")

    inner_frame6 = tk.Frame(navbar_frame, width=1200,height=600)
    inner_frame6.pack(side="top")

    previous_button = tk.Button(inner_frame6, text="Previous", command=previous_page)
    previous_button.grid(row=0, column=0)

    num_pages = 5
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
            for col_index, key in enumerate(["billingContactPerson", "wabaNumber", "saleInCharge","currentBalance","accSubExpireDate","status"]):
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

    

