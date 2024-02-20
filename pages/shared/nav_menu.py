import tkinter as tk
from pages.admin.tenant import create_tenant
from pages.admin.user import create_user

def create_navbar(main_window,content):
    navbar_frame = tk.Frame(main_window,bg="#ffffff", width=400)
    navbar_frame.pack_propagate(False)
    navbar_frame.pack(side=tk.LEFT, fill=tk.Y)

    home_button = tk.Label(navbar_frame, bg="#90EE90", text="SimplyBlast", height=3)
    home_button.config(font=("Arial", 16))
    home_button.pack(fill=tk.X)
    home_button.bind("<Button-1>", lambda event: print("Label clicked"))

    tenant_button = tk.Label(navbar_frame,bg="#ffffff", text="Tenants", height=3)
    tenant_button.config(font=("Arial", 16))
    tenant_button.pack(fill=tk.X)
    tenant_button.bind("<Enter>", lambda event: tenant_button.config(bg="#90EE90"))
    tenant_button.bind("<Leave>", lambda event: tenant_button.config(bg="#ffffff"))
    tenant_button.bind("<Button-1>", lambda event: create_tenant(content))

    user_button = tk.Label(navbar_frame,bg="#ffffff", text="User management", height=3)
    user_button.config(font=("Arial", 16))
    user_button.pack(fill=tk.X)
    user_button.bind("<Enter>", lambda event: user_button.config(bg="#90EE90"))
    user_button.bind("<Leave>", lambda event: user_button.config(bg="#ffffff"))
    user_button.bind("<Button-1>", lambda event: create_user(content))

    messagetemplate_button = tk.Label(navbar_frame,bg="#ffffff", text="Message templates", height=3)
    messagetemplate_button.config(font=("Arial", 16))
    messagetemplate_button.pack(fill=tk.X)
    messagetemplate_button.bind("<Enter>", lambda event: messagetemplate_button.config(bg="#90EE90"))
    messagetemplate_button.bind("<Leave>", lambda event: messagetemplate_button.config(bg="#ffffff"))

    countryprice_button = tk.Label(navbar_frame,bg="#ffffff", text="Country price list", height=3)
    countryprice_button.config(font=("Arial", 16))
    countryprice_button.pack(fill=tk.X)
    countryprice_button.bind("<Enter>", lambda event: countryprice_button.config(bg="#90EE90"))
    countryprice_button.bind("<Leave>", lambda event: countryprice_button.config(bg="#ffffff"))

    waba_button = tk.Label(navbar_frame,bg="#ffffff", text="Waba management", height=3)
    waba_button.config(font=("Arial", 16))
    waba_button.pack(fill=tk.X)
    waba_button.bind("<Enter>", lambda event: waba_button.config(bg="#90EE90"))
    waba_button.bind("<Leave>", lambda event: waba_button.config(bg="#ffffff"))

    topup_button = tk.Label(navbar_frame,bg="#ffffff", text="Topup history", height=3)
    topup_button.config(font=("Arial", 16))
    topup_button.pack(fill=tk.X)
    topup_button.bind("<Enter>", lambda event: topup_button.config(bg="#90EE90"))
    topup_button.bind("<Leave>", lambda event: topup_button.config(bg="#ffffff"))


    

