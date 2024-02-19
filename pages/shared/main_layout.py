import tkinter as tk
from pages.shared.nav_menu import create_navbar
from pages.shared.content import create_content

def show_main_layout(main_window,token_manager):
    main_layout = tk.Toplevel(main_window)
    main_layout.title("SimplyBlast")

    screen_width = main_layout.winfo_screenwidth()
    screen_height = main_layout.winfo_screenheight()
    window_width = 1600
    window_height = 900
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    main_layout.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # label_dashboard = tk.Label(main_layout, text="Welcome to App!")
    # label_dashboard.pack(pady=10)

    # back_button = tk.Button(main_layout, text="Back to Login", command=lambda: back_to_login(main_window, main_layout))
    # back_button.pack(pady=10)

    create_navbar(main_layout)
    create_content(main_layout)

def back_to_login(main_window, layout):
    layout.destroy()
    main_window.deiconify()