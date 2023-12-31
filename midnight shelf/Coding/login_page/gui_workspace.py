from customtkinter import *
from PIL import Image
import Database
import tkinter as tk
from io import BytesIO

img_pathh = ""
description = """In the highly anticipated Thinking, Fast and Slow, Kahneman takes us on a groundbreaking tour of the mind and explains the two systems that drive the way we think. System 1 is fast, intuitive, and emotional; System 2 is slower, more deliberative, and more logical. Kahneman exposes the extraordinary capabilities—and also the faults and biases—of fast thinking, and reveals the pervasive influence of intuitive impressions on our thoughts and behavior. The impact of loss aversion and overconfidence on corporate strategies, the difficulties of predicting what will make us happy in the future, the challenges of properly framing risks at work and at home, the profound effect of cognitive biases on everything from playing the stock market to planning the next vacation—each of these can be understood only by knowing how the two systems work together to shape our judgments and decisions.

Engaging the reader in a lively conversation about how we think, Kahneman reveals where we can and cannot trust our intuitions and how we can tap into the benefits of slow thinking. He offers practical and enlightening insights into how choices are made in both our business and our personal lives—and how we can use different techniques to guard against the mental glitches that often get us into trouble. Thinking, Fast and Slow will transform the way you think about thinking."""

class AddWindow:
    def __init__(self):
        self.app = CTk()
        self.app.geometry("500x400")
        self.app.configure(fg_color="white")

        self.book_name_entry = None
        self.author_name_entry = None
        self.book_description_entry = None
        self.image_path_entry = None
        self.price_entry = None
        self.error_label = None

        self.create_gui()

        self.app.mainloop()

    def create_gui(self):
        # Create a frame
        frame = CTkFrame(master=self.app, fg_color="#3ab2c9")
        frame.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)

        # Create entry boxes
        self.book_name_entry = CTkEntry(master=frame, width=220, height=2, placeholder_text="Book Name",
                                        font=("Arial", 10), fg_color="white", bg_color="black", text_color="black",
                                        corner_radius=0)
        self.book_name_entry.place(relx=0.5, rely=0.1, anchor="center")

        self.author_name_entry = CTkEntry(master=frame, width=220, height=2, placeholder_text="Author Name",
                                          font=("Arial", 10), fg_color="white", bg_color="black", text_color="black",
                                          corner_radius=0)
        self.author_name_entry.place(relx=0.5, rely=0.2, anchor="center")

        self.book_description_entry = CTkEntry(master=frame, width=220, height=2, placeholder_text="Book Description",
                                               font=("Arial", 10), fg_color="white", bg_color="black",
                                               text_color="black", corner_radius=0)
        self.book_description_entry.place(relx=0.5, rely=0.3, anchor="center")

        self.image_path_entry = CTkEntry(master=frame, width=220, height=2, placeholder_text="Image Path",
                                         font=("Arial", 10), fg_color="white", bg_color="black", text_color="black",
                                         corner_radius=0)
        self.image_path_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.price_entry = CTkEntry(master=frame, width=220, height=2, placeholder_text="Price",
                                    font=("Arial", 10), fg_color="white", bg_color="black", text_color="black",
                                    corner_radius=0)
        self.price_entry.place(relx=0.5, rely=0.5, anchor="center")

        # Create confirm button
        confirm_button = CTkButton(master=frame, text="Confirm", width=20, height=3, corner_radius=0,
                                    font=("Arial", 12), fg_color="#b603fc", hover_color="lightblue",
                                    command=self.confirm_button_clicked)
        confirm_button.place(relx=0.5, rely=0.6, anchor="center")

        # Back button
        back_button = CTkButton(self.app, text="►", width=20, height=30, corner_radius=10,border_width=0, fg_color="#8c8445",
                                hover_color="#78713b", font=("Arial", 12), command=self.back)
        back_button.place(relx=0.93, rely=0.93, anchor="w")

        # Create hidden error label
        self.error_label = CTkLabel(master=frame, text="", font=("Arial", 12), text_color="red")
        self.error_label.place(relx=0.5, rely=0.9, anchor="center")

    def back(self):
        pass

    def confirm_button_clicked(self):
        # Example validation: Check if book name is not empty
        book_name = self.book_name_entry.get()
        book_author = self.author_name_entry.get()
        book_description = self.book_description_entry.get()
        book_image_path = self.image_path_entry.get()
        book_price = self.price_entry.get()

        if len(book_name)==0 or len(book_author)==0 or len(book_description)==0 or len(book_image_path)==0 or len(book_price)==0:
            self.error_label.configure(text="Don't leave empty slots")
            self.error_label.pack()
        else:
            # Reset error label
            self.error_label.configure(text="")
            # Perform actions to add the book successfully (you can add your logic here)
            Database.add_photo(book_name,book_author,book_description,book_image_path,book_price)


# Example usage:
add_window_instance = AddWindow()
