from customtkinter import *
from PIL import Image
import Database
import tkinter as tk
from io import BytesIO


class book_description_window_for_reader:
    def __init__(self,i_path,booktitle,author,bookdescription,ID,book_id,prev_page):
        self.prev_page = prev_page
        self.bookID = book_id
        self.ID = ID
        self.app = CTk()
        self.app.geometry("900x600")
        self.app.configure(fg_color="#d9ca8d")

        shaded_frame = CTkFrame(master=self.app, fg_color="#c4b168")
        shaded_frame.place(relx=0, rely=0, relwidth=0.35, relheight=1.5)

        # Load an example image (replace with your image file path)
        image_path = "book covers/rosie project.png"
        img = Image.open(BytesIO(Database.get_photo(book_id)))
        #img = img.resize((300, 400), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        ct_img = CTkImage(light_image=img, dark_image=img, size=(300, 400))

        # Display the image on the right
        image_label = CTkLabel(shaded_frame, image=ct_img,text="")
        image_label.place(relx=0.5, rely=0.35, anchor="center")

        # Book title
        title_label = CTkLabel(self.app, text=booktitle,text_color="black", font=("Arial", 30))
        title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Author title
        author_label = CTkLabel(self.app, text=author, text_color="black", font=("Arial", 20))
        author_label.place(relx=0.51, rely=0.17, anchor="center")

        # Book description
        description_text = tk.Text(self.app, width=50, height=20, wrap="word", bg="#c4b168", font=("Arial", 12))
        description_text.insert("1.0", bookdescription)
        description_text.place(relx=0.42, rely=0.55, anchor="w")

        # Add a scrollbar for the text widget
        scrollbar = CTkScrollbar(self.app,height=370, command=description_text.yview)
        description_text['yscrollcommand'] = scrollbar.set

        # Set the initial position and length of the scrollbar
        #scrollbar.set(scrollbar_start, scrollbar_start + scrollbar_height)

        scrollbar.place(relx=0.95, rely=0.55, anchor="w")

        # Rounded square buttons
        self.button1 = CTkButton(shaded_frame, text="❤",width=20,fg_color="red",hover_color="#bd2413", corner_radius=50, font=("Arial", 12),command=self.fav)
        self.button1.place(relx=0.05, rely=0.595, anchor="w")

        self.button2 = CTkButton(shaded_frame, text="♻",width=10,fg_color="black",hover_color="white", corner_radius=50, font=("Arial", 12),command=self.delete)
        self.button2.place(relx=0.25, rely=0.595, anchor="w")

        # Back button
        back_button = CTkButton(self.app, text="►",width=20,height=30, corner_radius=10,fg_color="#8c8445",hover_color="#78713b", font=("Arial", 12),command=self.back)
        back_button.place(relx=0.93, rely=0.93, anchor="w")

        fav = Database.check_state(self.ID,self.bookID)
        if fav == 2:
            self.button1.configure(fg_color="red")
        else:
            self.button1.configure(fg_color="black")

        self.app.mainloop()

    def back(self):
        self.app.destroy()
        if self.prev_page == "library":
            lib_instance = own_library(self.ID)
        elif self.prev_page == "favourite":
            lib_instance = favourite_library(self.ID)
        elif self.prev_page == "wishlist":
            lib_instance = wishlist_library(self.ID)

    def delete(self):
        Database.delete_from_library(self.ID,self.bookID)

    def fav(self):
        Database.add_to_favourite(self.ID,self.bookID)
        fav = Database.check_state(self.ID, self.bookID)
        if fav == 2:
            self.button1.configure(fg_color="red")
        else:
            self.button1.configure(fg_color="black")

class store_library:
    def __init__(self, ID, role, word=''):
        self.role = role
        self.ID = ID
        self.app = CTk()
        self.app.geometry("900x600")
        self.app.configure(fg_color="white")
        self.GUI(self.ID, self.role, word)
        self.app.mainloop()

    def GUI(self, ID, role, word=''):
        shaded_frame = CTkFrame(master=self.app, fg_color="#3ab2c9")
        shaded_frame.place(relx=0.0, rely=-0.1, relwidth=0.2, relheight=1.5)
        # Create a search entry
        self.search_entry = CTkEntry(master=shaded_frame, width=120, height=1, placeholder_text="Search...",
                                     font=("Arial", 10),
                                     fg_color="white", bg_color="black", text_color="black", corner_radius=0)
        self.search_entry.place(relx=0.5, rely=0.1, anchor="center")

        # Create a search button with a magnifying glass icon
        search_button = CTkButton(master=shaded_frame, text="🔍", width=2, height=4, corner_radius=0,
                                  font=("Arial", 12), fg_color="#b603fc", hover_color="lightblue",
                                  command=self.search_button)
        search_button.place(relx=0.885, rely=0.1, anchor="center")

        if role == 0:
            # Create a "Favourite" button
            favorite_button = CTkButton(master=shaded_frame, text="Favourite❤", width=120, height=4, corner_radius=0,
                                        font=("Arial", 12), fg_color="red", hover_color="pink",
                                        command=self.open_favourites)
            favorite_button.place(relx=0.5, rely=0.2, anchor="center")

            # Create a "Library" button
            Library_button = CTkButton(master=shaded_frame, text="Library📚", text_color="black", width=120, height=4,
                                       corner_radius=0,
                                       font=("Arial", 12), fg_color="yellow", hover_color="pink",
                                       command=self.open_library)
            Library_button.place(relx=0.5, rely=0.225, anchor="center")

            # Create a "Wishlist" button
            wishlist_button = CTkButton(master=shaded_frame, text="Wishlist⭐", width=120, height=4, corner_radius=0,
                                        font=("Arial", 12), fg_color="black", hover_color="lightyellow",
                                        command=self.open_wishlist)
            wishlist_button.place(relx=0.5, rely=0.25, anchor="center")

            # Create checkboxes for book genres
            genres = ["all", "Fantasy", "Mystery", "Romance", "Science Fiction", "Non-fiction",
                      "Thriller", "Biography", "History", "Horror"]

            genre_combobox = CTkComboBox(master=shaded_frame, width=125, values=genres, text_color='black',
                                         fg_color="white")
            genre_combobox.place(relx=0.5, rely=0.3, anchor="center")

            # Right side frame
            self.content_frame = CTkScrollableFrame(master=self.app,fg_color="white")
            self.content_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

            self.covers = []
            if word == '':
                self.covers = Database.wish(self.ID)
            else:
                self.covers = Database.search_user_store(self.ID, word)

            self.display_items()

        elif role == 1:
            # Create a "Favourite" button
            add_button = CTkButton(master=shaded_frame, text="add +", width=120, height=4, corner_radius=0,
                                   font=("Arial", 12), fg_color="black", hover_color="pink",
                                   command=self.add_button)
            add_button.place(relx=0.5, rely=0.2, anchor="center")

            # Create checkboxes for book genres
            genres = ["all", "Fantasy", "Mystery", "Romance", "Science Fiction", "Non-fiction",
                      "Thriller", "Biography", "History", "Horror"]

            genre_combobox = CTkComboBox(master=shaded_frame, width=125, values=genres, text_color='black',
                                         fg_color="white")
            genre_combobox.place(relx=0.5, rely=0.3, anchor="center")

            # Right side frame
            self.content_frame = CTkScrollableFrame(master=self.app,fg_color="white")
            self.content_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

            self.covers = []
            if word == '':
                self.covers = Database.store_books()
            else:
                self.covers = Database.search_store(self.ID, word)

            self.display_items()

    def display_items(self):
        # Display the items on the scrollable frame
        for i, item in enumerate(self.covers):
            x = self.covers[i]
            img = Image.open(BytesIO(x[4]))

            # Create a frame for each item with padding
            item_frame = tk.Frame(self.content_frame, padx=40, pady=40, bg="white")
            item_frame.grid(row=i // 3, column=i % 3, sticky="w")

            ct_img = CTkImage(light_image=img, dark_image=img, size=(150, 200))

            # Add label to the item frame
            label = CTkLabel(item_frame, text="", font=("Arial", 12), text_color="black")
            label.configure(image=ct_img)
            label.pack()

            # Bind the label to a click event
            label.bind("<Button-1>",
                       lambda event, ct_img=ct_img, book_info=x: self.label_clicked(ct_img, book_info))

    def search_button(self):
        self.search_word = self.search_entry.get()
        self.GUI(self.ID, self.role, self.search_word)

    def label_clicked(self, ct_img, book_info):
        # self.app.destroy()
        print(book_info[0])
        if self.role == 0:
            Database.add_to_wishlist(self.ID,book_info[0])
        self.GUI(self.ID, 0)
        #inst = book_description_window_for_reader(1,book_info[1],book_info[2],"hazem",self.ID,book_info[0],"library")

    def open_favourites(self):
        self.app.destroy()
        fav_instance = favourite_library(self.ID)

    def open_wishlist(self):
        self.app.destroy()
        wish_instance = wishlist_library(self.ID)

    def open_library(self):
        self.app.destroy()
        inst = own_library(self.ID)

    def add_button(self):
        self.app.destroy()
        inst = AddWindow(self.ID)


class favourite_library:
    def __init__(self,ID,word=''):
        self.ID=ID
        self.app = CTk()
        self.app.geometry("900x600")
        self.app.configure(fg_color="white")
        self.GUI(ID,0,word)

        self.app.mainloop()

    def GUI(self,ID,role,word=''):
        shaded_frame = CTkFrame(master=self.app, fg_color="#3ab2c9")
        shaded_frame.place(relx=0.0, rely=-0.1, relwidth=0.2, relheight=1.5)
        # Create a search entry
        self.search_entry = CTkEntry(master=shaded_frame, width=120, height=1, placeholder_text="Search...",
                                     font=("Arial", 10),
                                     fg_color="white", bg_color="black", text_color="black", corner_radius=0)
        self.search_entry.place(relx=0.5, rely=0.1, anchor="center")

        # Create a search button with a magnifying glass icon
        search_button = CTkButton(master=shaded_frame, text="🔍", width=2, height=4, corner_radius=0,
                                  font=("Arial", 12), fg_color="#b603fc", hover_color="lightblue",
                                  command=self.search_button)
        search_button.place(relx=0.885, rely=0.1, anchor="center")

        # Create a "Library" button
        Library_button = CTkButton(master=shaded_frame, text="Library📚", text_color="black", width=120, height=4,
                                   corner_radius=0,
                                   font=("Arial", 12), fg_color="yellow", hover_color="pink", command=self.open_library)
        Library_button.place(relx=0.5, rely=0.2, anchor="center")

        # create store button
        store_button = CTkButton(master=shaded_frame, text="Store📖", text_color="black", width=120, height=4,
                                 corner_radius=0,
                                 font=("Arial", 12), fg_color="#6e1ba1", hover_color="#7f1eba", command=self.open_store)
        store_button.place(relx=0.5, rely=0.225, anchor="center")

        # Create a "Wishlist" button
        wishlist_button = CTkButton(master=shaded_frame, text="Wishlist⭐", width=120, height=4, corner_radius=0,
                                    font=("Arial", 12), fg_color="black", hover_color="lightyellow",
                                    command=self.open_wishlist)
        wishlist_button.place(relx=0.5, rely=0.25, anchor="center")

        # Create checkboxes for book genres
        genres = ["all", "Fantasy", "Mystery", "Romance", "Science Fiction", "Non-fiction",
                  "Thriller", "Biography", "History", "Horror"]

        genre_combobox = CTkComboBox(master=shaded_frame, width=125, values=genres, text_color='black',
                                     fg_color="white")
        genre_combobox.place(relx=0.5, rely=0.3, anchor="center")

        # Right side frame
        self.content_frame = CTkScrollableFrame(master=self.app, fg_color="white")
        self.content_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        self.covers = []
        if word == '':
            self.covers = Database.user_favourite(self.ID)
        else:
            self.covers = Database.search_favourite(self.ID, word)

        self.display()


    def display(self):
        # Create a list of 9 items (you can replace this with your actual items)
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9"]

        num_columns = 3
        num_rows = (len(items) + num_columns - 1) // num_columns
        self.BOOk_ID = 0
        # Display the items on the canvas
        for i, item in enumerate(self.covers):
            row, col = divmod(i, num_columns)
            x = self.covers[i][0]
            img = Image.open(BytesIO(x[4]))
            self.BOOk_ID = x[0]
            # Create a frame for each item with padding
            item_frame = tk.Frame(self.content_frame, padx=40, pady=40, bg="white")
            item_frame.grid(row=row, column=col, sticky="w")

            ct_img = CTkImage(light_image=img, dark_image=img, size=(150, 200))

            # Add label to the item frame
            label = CTkLabel(item_frame, text="", font=("Arial", 12), text_color="black")
            label.configure(image=ct_img)
            label.pack()

            # Bind the label to a click event
            img_pathh = "book covers/all this time.png"
            label.bind("<Button-1>",
                       lambda event, item=item, ct_img=ct_img, book_info=x: self.label_clicked(ct_img, book_info))

    def search_button(self):
        self.search_word = self.search_entry.get()
        self.app.destroy()
        instance = favourite_library(self.ID,self.search_word)

    def label_clicked(self, ct_img,book_info):
        self.app.destroy()
        print(book_info)
        inst = book_description_window_for_reader(1,book_info[1],book_info[2],book_info[3],self.ID,book_info[0],"favourite")

    def open_wishlist(self):
        self.app.destroy()
        wish_instance = wishlist_library(self.ID)

    def open_library(self):
        self.app.destroy()
        library_instance = own_library(self.ID)

    def open_store(self):
        self.app.destroy()
        store_instance = store_library(self.ID,0)


class wishlist_library:
    def __init__(self,ID,word=''):
        self.ID=ID
        self.app = CTk()
        self.app.geometry("900x600")
        self.app.configure(fg_color="white")
        self.GUI(ID,word)

        self.app.mainloop()

    def GUI(self,ID,word=''):
        shaded_frame = CTkFrame(master=self.app, fg_color="#3ab2c9")
        shaded_frame.place(relx=0.0, rely=-0.1, relwidth=0.2, relheight=1.5)
        # Create a search entry
        self.search_entry = CTkEntry(master=shaded_frame, width=120, height=1, placeholder_text="Search...",
                                     font=("Arial", 10),
                                     fg_color="white", bg_color="black", text_color="black", corner_radius=0)
        self.search_entry.place(relx=0.5, rely=0.1, anchor="center")

        # Create a search button with a magnifying glass icon
        search_button = CTkButton(master=shaded_frame, text="🔍", width=2, height=4, corner_radius=0,
                                  font=("Arial", 12), fg_color="#b603fc", hover_color="lightblue",
                                  command=self.search_button)
        search_button.place(relx=0.885, rely=0.1, anchor="center")

        # Create a "Library" button
        Library_button = CTkButton(master=shaded_frame, text="Library📚", text_color="black", width=120, height=4,
                                   corner_radius=0,
                                   font=("Arial", 12), fg_color="yellow", hover_color="pink", command=self.open_library)
        Library_button.place(relx=0.5, rely=0.2, anchor="center")

        # create store button
        store_button = CTkButton(master=shaded_frame, text="Store📖", text_color="black", width=120, height=4,
                                 corner_radius=0,
                                 font=("Arial", 12), fg_color="#6e1ba1", hover_color="#7f1eba", command=self.open_store)
        store_button.place(relx=0.5, rely=0.225, anchor="center")

        # Create a "Favorite" button
        favorite_button = CTkButton(master=shaded_frame, text="Favourite❤", width=120, height=4, corner_radius=0,
                                    font=("Arial", 12), fg_color="red", hover_color="pink",
                                    command=self.open_favourites)
        favorite_button.place(relx=0.5, rely=0.25, anchor="center")

        # Create checkboxes for book genres
        genres = ["all", "Fantasy", "Mystery", "Romance", "Science Fiction", "Non-fiction",
                  "Thriller", "Biography", "History", "Horror"]

        genre_combobox = CTkComboBox(master=shaded_frame, width=125, values=genres, text_color='black',
                                     fg_color="white")
        genre_combobox.place(relx=0.5, rely=0.3, anchor="center")

        # Right side frame
        self.content_frame = CTkScrollableFrame(master=self.app, fg_color="white")
        self.content_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        self.covers = Database.search_wishlist(self.ID, word)



        self.display()

    def display(self):
        # Create a list of 9 items (you can replace this with your actual items)
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9"]

        num_columns = 3
        num_rows = (len(items) + num_columns - 1) // num_columns
        self.BOOk_ID = 0
        # Display the items on the canvas
        for i, item in enumerate(self.covers):
            row, col = divmod(i, num_columns)
            x = self.covers[i][0]
            img = Image.open(BytesIO(x[4]))
            self.BOOk_ID = x[0]
            # Create a frame for each item with padding
            item_frame = tk.Frame(self.content_frame, padx=40, pady=40, bg="white")
            item_frame.grid(row=row, column=col, sticky="w")

            ct_img = CTkImage(light_image=img, dark_image=img, size=(150, 200))

            # Add label to the item frame
            label = CTkLabel(item_frame, text="", font=("Arial", 12), text_color="black")
            label.configure(image=ct_img)
            label.pack()

            # Bind the label to a click event
            img_pathh = "book covers/all this time.png"
            label.bind("<Button-1>",
                       lambda event, item=item, ct_img=ct_img, book_info=x: self.label_clicked(ct_img, book_info))

    def search_button(self):
        self.search_word = self.search_entry.get()
        self.app.destroy()
        instance = wishlist_library(self.ID,self.search_word)

    def label_clicked(self, ct_img,book_info):
        self.app.destroy()
        print(book_info)
        inst = book_description_window_for_reader(1,book_info[1],book_info[2],book_info[3],self.ID,book_info[0],"wishlist")

    def open_library(self):
        self.app.destroy()
        library_instance = own_library(self.ID)

    def open_favourites(self):
        self.app.destroy()
        fav_instance = favourite_library(self.ID)

    def open_store(self):
        self.app.destroy()
        store_instance = store_library(self.ID,0)

class own_library:
    def __init__(self,ID,word=''):
        self.ID=ID
        self.app = CTk()
        self.app.geometry("900x600")
        self.app.configure(fg_color="white")
        self.GUI(ID,word)

        self.app.mainloop()

    def GUI(self,gui_id,gui_word=''):
        shaded_frame = CTkFrame(master=self.app, fg_color="#3ab2c9")
        shaded_frame.place(relx=0.0, rely=-0.1, relwidth=0.2, relheight=1.5)
        # Create a search entry
        self.search_entry = CTkEntry(master=shaded_frame, width=120, height=1, placeholder_text="Search...",
                                     font=("Arial", 10),
                                     fg_color="white", bg_color="black", text_color="black", corner_radius=0)
        self.search_entry.place(relx=0.5, rely=0.1, anchor="center")

        # Create a search button with a magnifying glass icon
        search_button = CTkButton(master=shaded_frame, text="🔍", width=2, height=4, corner_radius=0,
                                  font=("Arial", 12), fg_color="#b603fc", hover_color="lightblue",
                                  command=self.search_button)
        search_button.place(relx=0.885, rely=0.1, anchor="center")

        # Create a "Favourite" button
        favorite_button = CTkButton(master=shaded_frame, text="Favourite❤", width=120, height=4, corner_radius=0,
                                    font=("Arial", 12), fg_color="red", hover_color="pink",
                                    command=self.open_favourites)
        favorite_button.place(relx=0.5, rely=0.2, anchor="center")

        # create store button
        store_button = CTkButton(master=shaded_frame, text="Store📖", text_color="black", width=120, height=4,
                                 corner_radius=0,
                                 font=("Arial", 12), fg_color="#6e1ba1", hover_color="#7f1eba", command=self.open_store)
        store_button.place(relx=0.5, rely=0.225, anchor="center")

        # Create a "Wishlist" button
        wishlist_button = CTkButton(master=shaded_frame, text="Wishlist⭐", width=120, height=4, corner_radius=0,
                                    font=("Arial", 12), fg_color="black", hover_color="lightyellow",
                                    command=self.open_wishlist)
        wishlist_button.place(relx=0.5, rely=0.25, anchor="center")

        # Create checkboxes for book genres
        genres = ["all", "Fantasy", "Mystery", "Romance", "Science Fiction", "Non-fiction",
                  "Thriller", "Biography", "History", "Horror"]

        genre_combobox = CTkComboBox(master=shaded_frame, width=125, values=genres, text_color='black',
                                     fg_color="white")
        genre_combobox.place(relx=0.5, rely=0.3, anchor="center")

        # Right side frame
        self.content_frame = CTkScrollableFrame(master=self.app,fg_color="white")
        self.content_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        self.covers = []
        if gui_word == '':
            self.covers = Database.user_library(self.ID)
        else:
            self.covers = Database.search_library(self.ID, gui_word)

        # Create a list of 9 items (you can replace this with your actual items)
        items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9"]

        self.num_columns = 3
        self.num_rows = (len(items) + self.num_columns - 1) // self.num_columns
        self.BOOk_ID = 0
        # Display the items on the canvas

        self.display()

    def display(self):
        for i, item in enumerate(self.covers):
            row, col = divmod(i, self.num_columns)
            x = self.covers[i][0]
            img = Image.open(BytesIO(x[4]))
            self.BOOk_ID = x[0]
            # Create a frame for each item with padding
            item_frame = tk.Frame(self.content_frame, padx=40, pady=40, bg="white")
            item_frame.grid(row=row, column=col, sticky="w")

            ct_img = CTkImage(light_image=img, dark_image=img, size=(150, 200))

            # Add label to the item frame
            label = CTkLabel(item_frame, text="", font=("Arial", 12), text_color="black")
            label.configure(image=ct_img)
            label.pack()

            # Bind the label to a click event
            label.bind("<Button-1>",
                       lambda event, item=item, ct_img=ct_img, book_info=x: self.label_clicked(ct_img, book_info))

    def search_button(self):
        self.search_word = self.search_entry.get()
        self.app.destroy()
        instance = own_library(self.ID,self.search_word)

    def label_clicked(self, ct_img,book_info):
        self.app.destroy()
        print(book_info)
        inst = book_description_window_for_reader(1,book_info[1],book_info[2],book_info[3],self.ID,book_info[0],"library")

    def open_favourites(self):
        self.app.destroy()
        fav_instance = favourite_library(self.ID)

    def open_wishlist(self):
        self.app.destroy()
        wish_instance = wishlist_library(self.ID)

    def open_store(self):
        self.app.destroy()
        store_instance = store_library(self.ID,0)

    #def open_store(self):
        #self.app.destroy()
        #login_instance = store_library()

class AddWindow:
    def __init__(self,ID):
        self.ID = ID
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
        back_button = CTkButton(self.app, text="►", width=20, height=30, corner_radius=10, border_width=0,
                                fg_color="#8c8445",
                                hover_color="#78713b", font=("Arial", 12), command=self.back)
        back_button.place(relx=0.93, rely=0.93, anchor="w")

        # Create hidden error label
        self.error_label = CTkLabel(master=frame, text="", font=("Arial", 12), text_color="red")
        self.error_label.place(relx=0.5, rely=0.9, anchor="center")

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

    def back(self):
        inst = store_library(self.ID,1)

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
        self.registration_label = CTkLabel(master=shaded_frame, text="Register",text_color="#b5ac4c", font=("Arial", 16))
        self.registration_label.place(relx=0.5,rely=0.1,anchor='center')

        # Text box for username
        self.username_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="Username", text_color="black",
                               font=("Arial", 12), fg_color="transparent")
        self.username_entry.place(relx=0.5, rely=0.25, anchor='center')

        # Text box for email
        self.email_entry = CTkEntry(master=shaded_frame,width=250, placeholder_text="Email",text_color="black", font=("Arial", 12),fg_color="transparent")
        self.email_entry.place(relx=0.5,rely=0.3,anchor='center')

        # Text box for password
        self.password_entry = CTkEntry(master=shaded_frame,width=250, placeholder_text="Password", show="*",text_color="black", font=("Arial", 12),fg_color="transparent")
        self.password_entry.place(relx=0.5,rely=0.35,anchor='center')

        # Text box for phone
        self.phone_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="Phone", text_color="black",
                                  font=("Arial", 12), fg_color="transparent")
        self.phone_entry.place(relx=0.5, rely=0.4, anchor='center')

        # Text box for address
        self.address_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="Address", text_color="black",
                                  font=("Arial", 12), fg_color="transparent")
        self.address_entry.place(relx=0.5, rely=0.45, anchor='center')

        # Text box for birthdate
        self.birthdate_entry = CTkEntry(master=shaded_frame, width=250, placeholder_text="Year-Month-Day", text_color="black",
                                  font=("Arial", 12), fg_color="transparent")
        self.birthdate_entry.place(relx=0.5, rely=0.5, anchor='center')

        # Combo box for gender
        self.Gender_combobox = CTkComboBox(master=shaded_frame,width=125,values=['Male','Female'],text_color='black', fg_color="white")
        self.Gender_combobox.place(relx=0.354, rely=0.55, anchor='center')

        # Combo box for role
        self.role_combobox = CTkComboBox(master=shaded_frame, width=125, values=['reader', 'store'], text_color='black',
                                      fg_color="white")
        self.role_combobox.place(relx=0.645, rely=0.55, anchor='center')

        # register button
        reg_button = CTkButton(master=shaded_frame, text="Register", corner_radius=60, font=("Arial", 14),
                                 fg_color="#b5ac4c", hover_color="#b0aa68", command=self.check_register)
        reg_button.place(relx=0.5, rely=0.7, anchor='center')

        # back button
        back_button = CTkButton(master=shaded_frame, text="←",width=15,height=10, corner_radius=100, font=("Arial", 14),
                               fg_color="#b5ac4c", hover_color="#b0aa68", command=self.Back)
        back_button.place(relx=0.1, rely=0.9, anchor='center')

        #error message
        self.error_label = CTkLabel(master=shaded_frame, text="", text_color="red", font=("Arial", 12),
                                    fg_color='transparent')
        self.error_label.place(relx=0.5, rely=0.8, anchor='center')


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

    def check_register(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        birthdate = self.birthdate_entry.get()

        # Get data from combo boxes
        gender = self.Gender_combobox.get()
        role = self.role_combobox.get()

        if role == "reader":
            role=0
        elif role == "store":
            role=1

        print(username)
        print(email)
        print(password)
        print(phone)
        print(address)
        print(birthdate)
        print(gender)
        if gender == 'Male':
            gender = 'M'
        elif gender == 'Female':
            gender = 'F'

        API = Database.sign_in(email,password,username,phone,address,gender,birthdate,role)
        flag = API.registration()
        if flag == -1:
            self.error_label.configure(text="email already exists", text_color="red")
        elif flag == -2:
            self.error_label.configure(text="username already exists", text_color="red")
        else:
            self.error_label.configure(text="registration successful", text_color="green")



    def Back(self):
        self.app.destroy()
        login_instance = login_page()

class login_page():
    def __init__(self):
        self.app = CTk()
        self.app.geometry("900x600")
        img_1 = Image.open("background_images/5.png")
        img_2 = Image.open("background_images/6.png")
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
        login_label = CTkLabel(master=shaded_frame, text="Login",text_color="#b5ac4c", font=("Arial", 16))
        login_label.grid(row=4, column=0, pady=(10, 5), sticky="nsew")

        # Text box for email
        self.email_entry = CTkEntry(master=shaded_frame,width=250, placeholder_text="Email",text_color="black", font=("Arial", 12),fg_color="transparent")
        self.email_entry.place(relx=0.5,rely=0.4,anchor='center')

        # Text box for password
        self.password_entry = CTkEntry(master=shaded_frame,width=250, placeholder_text="Password", show="*",text_color="black", font=("Arial", 12),fg_color="transparent")
        self.password_entry.place(relx=0.5,rely=0.45,anchor='center')

        # Combo box for role
        self.role_combobox = CTkComboBox(master=shaded_frame, width=125, values=['reader', 'store'], text_color='black',
                                    fg_color="white")
        self.role_combobox.place(relx=0.31, rely=0.5, anchor='center')

        # Login button
        login_button = CTkButton(master=shaded_frame, text="Login", corner_radius=60, font=("Arial", 14),
                                 fg_color="#b5ac4c", hover_color="#b0aa68", command=self.login_user)
        login_button.place(relx=0.5, rely=0.65, anchor='center')

        # sign-up? label
        signup_label = CTkLabel(master=shaded_frame, height=1, text="not signed-in?", text_color="black",
                                   fg_color='transparent')
        signup_label.place(relx=0.3, rely=0.72, anchor='center')

        # registration button
        Registration_button = CTkButton(master=shaded_frame,width=1, text="Registration", corner_radius=50, font=("Arial", 14),
                                 fg_color="white" ,hover_color='white', text_color="blue",command=self.Open_registration_page)
        #Registration_button.grid(row=9, column=0, pady=(10, 20))
        Registration_button.place(relx=0.6,rely=0.72,anchor='center')

        #error message
        self.error_label = CTkLabel(master=shaded_frame, text="", text_color="red", font=("Arial", 12),
                                    fg_color='transparent')
        self.error_label.place(relx=0.5, rely=0.8, anchor='center')


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


    def login_user(self):
        # Get the email and password from the entry widgets
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = self.role_combobox.get()
        if role == "reader":
            role=0
        elif role == "store":
            role=1
        # Call your login function with the obtained email and password
        print(email)
        print(password)
        print(role)
        API = Database.login(email,password,role)
        flag = API.check_login()
        print(flag)
        if flag == 0:
            self.error_label.configure(text="Invalid email or password")
        else:
            if role == 0:
                self.app.destroy()
                lib_instance = own_library(flag)
            else:
                self.app.destroy()
                inst = store_library(flag,1)


    def Open_registration_page(self):
        self.app.destroy()
        registration_instance = Registartion_page()

log = login_page()
