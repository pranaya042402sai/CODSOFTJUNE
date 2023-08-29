import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_list.insert(tk.END, f"{name}: {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter both name and phone number!")

# Function to edit a contact
def edit_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        name = name_entry.get()
        phone = phone_entry.get()
        if name and phone:
            contact_list.delete(selected_index)
            contact_list.insert(selected_index, f"{name}: {phone}")
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both name and phone number!")
    else:
        messagebox.showerror("Error", "Select a contact to edit!")

# Function to delete a contact
def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        contact_list.delete(selected_index)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Select a contact to delete!")

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")  # Set window dimensions
root.configure(bg="orange")  # Set background color to red

# Create labels and entry widgets for name and phone number
name_label = tk.Label(root, text="Name:", bg="red", fg="white")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone Number:", bg="green", fg="white")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Create buttons to add, edit, and delete contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white")
add_button.pack()

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact, bg="blue", fg="white")
edit_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg="violet", fg="white")
delete_button.pack()

# Create a listbox to display contacts
contact_list = tk.Listbox(root)
contact_list.pack()

# Start the GUI main loop
root.mainloop()
