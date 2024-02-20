import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from pkg.token.token import TokenManager
from pkg.config.config import read_config
import shelve
from PIL import Image, ImageTk
from io import BytesIO
from pages.shared.main_layout import show_main_layout
from pkg.pickle.pickle import save_token_to_local_storage,load_token_from_local_storage

config = read_config()
auth_url = config.get('Url', 'api_url')

token_manager = TokenManager()

def login():
    email = app.entry_email.get()
    password = app.entry_password.get()

    url = auth_url + '/auth/login'
    headers = {'Content-Type': 'application/json'}
    data = {
        "email": "admin@yopmail.com",
        "password": "Password@123"
    }

    response = requests.post(url, json=data, headers=headers)

    response_data = json.loads(response.text)

    isSuccess = response_data.get("isSuccess")
    data = response_data.get("data", {})

    if isSuccess == True:
        if data:
            access_token = data.get("accessToken")

            save_token_to_local_storage(access_token)
            
            messagebox.showinfo("Login", "Đăng nhập thành công!")
            app.withdraw() 
            show_main_layout(app,token_manager)

    else:
        messagebox.showerror("Lỗi", "Số điện thoại hoặc mật khẩu không đúng.")

def close_app(event=None):
    app.destroy()

def save_token_info(accessToken, refreshToken):
    with shelve.open("token_info.db") as db:
        db['access_token'] = accessToken
        db['refresh_token'] = refreshToken

def toggle_fullscreen(event=None):
    fullscreen_state = app.attributes('-fullscreen')
    if not fullscreen_state:
        app.attributes('-fullscreen', True)
    else:
        app.attributes('-fullscreen', False)

def load_image_from_url(url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    photo_image = ImageTk.PhotoImage(image)
    return photo_image


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SimplyBlast Login")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 1000
        window_height = 600

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


        self.sidebar_left = tk.Frame(self, bg="lightblue", width=200)
        self.sidebar_left.pack(fill="both", expand=True, side="left")

        self.content = tk.Frame(self, bg="white")
        self.content.pack(fill="both", expand=True, side="right")

        self.label_title = tk.Label(self.sidebar_left, text="SimplyBlast", font=("Helvetica", 24), bg="lightblue")
        self.label_title.pack(pady=(30, 10))

        self.image_whatsapp = tk.Frame(self.sidebar_left, bg="lightblue")
        self.image_whatsapp.pack()

        self.image_large = tk.Label(self.image_whatsapp, bg="lightblue")

        url_large = "https://app-simplyblast-app-qa-sea.azurewebsites.net/images/whatsapp.png"
        url_small = "https://app-simplyblast-app-qa-sea.azurewebsites.net/images/whatsapp-right.png"

        whatsapp_large = load_image_from_url(url_large)
        whatsapp_small = load_image_from_url(url_small)
        self.image_large.config(image=whatsapp_large)
        self.image_large.image = whatsapp_large
        self.image_large.grid(row=0, column=0)

        self.image_small = tk.Label(self.image_whatsapp, bg="lightblue")
        self.image_small.config(image=whatsapp_small)
        self.image_small.image = whatsapp_small
        self.image_small.grid(row=0, column=1)

        self.label_caption = tk.Label(self.sidebar_left, text="WhatsApp Marketing for Business Made Simple", font=("Helvetica", 12), bg="lightblue")
        self.label_caption.pack(pady=(10, 30))

        self.label_signin = tk.Label(self.content, text="Sign in", font=("Helvetica", 18), bg="white")
        self.label_signin.pack(pady=(50, 10))

        self.label_email = tk.Label(self.content, text="Email address", bg="white")
        self.label_email.pack()

        self.entry_email = tk.Entry(self.content)
        self.entry_email.pack()
        self.entry_email.focus_set()

        self.label_password = tk.Label(self.content, text="Password", bg="white")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.content, show="*")
        self.entry_password.pack()

        self.button_signin = tk.Button(self.content, text="Sign in", command=login)
        self.button_signin.pack(pady=(20, 10))


app = LoginPage()
app.bind("<Return>", lambda event=None: login())
app.bind("<Escape>", close_app)
app.bind("<F11>", toggle_fullscreen)
app.mainloop()

