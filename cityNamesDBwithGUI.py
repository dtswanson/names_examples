import sqlite3
import tkinter as tk

# Connect to swim.db and retrieve cities
def get_cities_by_letter(letter):
    connection = sqlite3.connect("dbswim.db")
    cursor = connection.cursor()
    cursor.execute("SELECT City FROM tblCities WHERE City LIKE ?", (letter + '%',))
    cities = [row[0] for row in cursor.fetchall()]
    connection.close()
    return cities

# Show list of cities in a Listbox view
def show_cities(letter):
    # Clear main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Display the selected cities in a Listbox
    cities = get_cities_by_letter(letter)
    label = tk.Label(main_frame, text=f"Cities starting with '{letter}':", font=("Arial", 14))
    label.pack(pady=10)

    listbox = tk.Listbox(main_frame, width=50, height=15, font=("Arial", 12))
    for city in cities:
        listbox.insert(tk.END, city)
    listbox.pack()

    # Add a back button to return to the letters view
    back_button = tk.Button(main_frame, text="Back to Letters", command=show_letters_view, font=("Arial", 12))
    back_button.pack(pady=10)

# Show the alphabet selection view
def show_letters_view():
    # Clear main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Create buttons for each letter A to Z
    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        button = tk.Button(main_frame, text=letter, width=5, command=lambda l=letter: show_cities(l), font=("Arial", 12))
        button.grid(row=i // 6, column=i % 6, padx=5, pady=5)

# Set up main window and frame
root = tk.Tk()
root.title("City Finder")

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Show the alphabet selection view at startup
show_letters_view()

root.mainloop()
