import tkinter as tk

def create_user(content):
    for widget in content.winfo_children():
        widget.destroy()