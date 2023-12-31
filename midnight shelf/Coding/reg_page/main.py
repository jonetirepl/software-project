import numpy
from customtkinter import *
from PIL import Image

class Registartion_page:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("900x600")
        img_1 = Image.open("background_images/5.png")
        background = CTkLabel(master=self.app, text="", padx=0, pady=0)
        background.configure(image=CTkImage(light_image=img_1, dark_image=img_1, size=(900, 600)))
        background.grid(row=0, column=0, padx=0, pady=0, rowspan=2, columnspan=3,sticky="nsew")
        shaded_frame = CTkFrame(master=self.app,fg_color="white")
        shaded_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=1)
        self.app.grid_columnconfigure(2, weight=1)
        self.app.grid_columnconfigure(3, weight=1)
        self.app.grid_columnconfigure(4, weight=1)
        self.app.grid_columnconfigure(5, weight=1)
        self.app.grid_columnconfigure(6, weight=1)
        self.app.grid_columnconfigure(7, weight=1)

        # Label for "Login"
        login_label = CTkLabel(master=shaded_frame, text="Register",text_color="#b5ac4c", font=("Arial", 16))
        login_label.place(relx=0.5,rely=0.1,anchor='center')

        # Text box for username
        username_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="Username", text_color="black",
                               font=("Arial", 12), fg_color="transparent")
        username_entry.place(relx=0.5, rely=0.25, anchor='center')

        # Text box for email
        email_entry = CTkEntry(master=shaded_frame,width=250, placeholder_text="Email",text_color="black", font=("Arial", 12),fg_color="transparent")
        email_entry.place(relx=0.5,rely=0.3,anchor='center')

        # Text box for password
        password_entry = CTkEntry(master=shaded_frame,width=250, placeholder_text="Password", show="*",text_color="black", font=("Arial", 12),fg_color="transparent")
        password_entry.place(relx=0.5,rely=0.35,anchor='center')

        # Text box for phone
        phone_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="Phone", text_color="black",
                                  font=("Arial", 12), fg_color="transparent")
        phone_entry.place(relx=0.5, rely=0.4, anchor='center')

        # Text box for address
        address_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="Address", text_color="black",
                                  font=("Arial", 12), fg_color="transparent")
        address_entry.place(relx=0.5, rely=0.45, anchor='center')

        # Text box for birthdate
        birthdate_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="DD/MM/YY", text_color="black",
                                  font=("Arial", 12), fg_color="transparent")
        birthdate_entry.place(relx=0.5, rely=0.5, anchor='center')

        # Combo box for gender
        Gender_combobox = CTkComboBox(master=shaded_frame,width=125,values=['Male','Female'],text_color='black', fg_color="white")
        Gender_combobox.place(relx=0.354, rely=0.55, anchor='center')

        # Combo box for role
        role_combobox = CTkComboBox(master=shaded_frame, width=125, values=['reader', 'store'], text_color='black',
                                      fg_color="white")
        role_combobox.place(relx=0.645, rely=0.55, anchor='center')

        # register button
        reg_button = CTkButton(master=shaded_frame, text="Register", corner_radius=60, font=("Arial", 14),
                                 fg_color="#b5ac4c", hover_color="#b0aa68")
        reg_button.place(relx=0.5, rely=0.7, anchor='center')

        # back button
        back_button = CTkButton(master=shaded_frame, text="←",width=15,height=10, corner_radius=100, font=("Arial", 14),
                               fg_color="#b5ac4c", hover_color="#b0aa68")
        back_button.place(relx=0.1, rely=0.9, anchor='center')


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

        self.app.mainloop()

    def check_login(self):
        print('pressed')

