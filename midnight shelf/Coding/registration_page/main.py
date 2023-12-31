import numpy
from customtkinter import *
from PIL import Image

def login_window():
    app = CTk()
    app.geometry("900x600")
    img_1 = Image.open("background_images/5.png")
    img_2 = Image.open("background_images/6.png")
    background = CTkLabel(master=app, text="", padx=0, pady=0)
    background.configure(image=CTkImage(light_image=img_1, dark_image=img_1, size=(900, 600)))
    background.grid(row=0, column=0, padx=0, pady=0, rowspan=2, columnspan=3,sticky="nsew")
    shaded_frame = CTkFrame(master=app,fg_color="white")
    shaded_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)
    app.grid_columnconfigure(3, weight=1)
    app.grid_columnconfigure(4, weight=1)
    app.grid_columnconfigure(5, weight=1)
    app.grid_columnconfigure(6, weight=1)
    app.grid_columnconfigure(7, weight=1)

    # Label for "Login"
    login_label = CTkLabel(master=shaded_frame, text="Login",text_color="#b5ac4c", font=("Arial", 16))
    login_label.grid(row=4, column=0, pady=(10, 5), sticky="nsew")

    # Text box for email
    email_entry = CTkEntry(master=shaded_frame,width=250, placeholder_text="Email",text_color="black", font=("Arial", 12),fg_color="transparent")
    email_entry.place(relx=0.5,rely=0.4,anchor='center')

    # Text box for password
    password_entry = CTkEntry(master=shaded_frame,width=200, placeholder_text="Password", show="*",text_color="black", font=("Arial", 12),fg_color="transparent")
    password_entry.place(relx=0.5,rely=0.45,anchor='center')

    # Login button
    login_button = CTkButton(master=shaded_frame, text="Login", corner_radius=60, font=("Arial", 14),
                             fg_color="#b5ac4c", hover_color="#b0aa68")
    login_button.grid(row=8, column=0, pady=(10, 20))

    # registration button
    Registration_button = CTkButton(master=shaded_frame, text="Registration", corner_radius=50, font=("Arial", 14),
                             fg_color="white" ,hover_color='white', text_color="blue" ,command=check_login)
    #Registration_button.grid(row=9, column=0, pady=(10, 20))
    Registration_button.place(relx=0.5,rely=0.59,anchor='center')

    # Center the content in the frame
    shaded_frame.grid_rowconfigure(0, weight=1)
    shaded_frame.grid_rowconfigure(1, weight=1)
    shaded_frame.grid_rowconfigure(2, weight=1)
    shaded_frame.grid_rowconfigure(3, weight=1)
    shaded_frame.grid_rowconfigure(4, weight=1)
    shaded_frame.grid_rowconfigure(5, weight=1)
    shaded_frame.grid_rowconfigure(6, weight=1)
    shaded_frame.grid_rowconfigure(7, weight=1)
    shaded_frame.grid_rowconfigure(8, weight=1)
    shaded_frame.grid_rowconfigure(9, weight=1)
    shaded_frame.grid_rowconfigure(10, weight=1)
    shaded_frame.grid_rowconfigure(11, weight=1)
    shaded_frame.grid_rowconfigure(12, weight=1)
    shaded_frame.grid_rowconfigure(13, weight=1)
    shaded_frame.grid_rowconfigure(14, weight=1)
    shaded_frame.grid_rowconfigure(15, weight=1)
    shaded_frame.grid_rowconfigure(100, weight=1)
    shaded_frame.grid_columnconfigure(0, weight=1)

    app.mainloop()

def check_login():
    print('pressed')

login_window();