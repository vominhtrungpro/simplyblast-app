import tkinter as tk
from pages.shared.nav_menu import create_navbar
from pages.shared.content import create_content

def show_app(login):
    app = tk.Toplevel(login)
    app.title("SimplyBlast")

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 1600
    window_height = 900
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    content_frame = create_content(app)

    create_navbar(app,content_frame,login)
