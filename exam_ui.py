import customtkinter as ctk


# Create the main window
root = ctk.CTk()

# Set the title and size of the window
root.title("Fancy Application")
root.geometry("500x300")


# Create a frame for the panels
panel_frame = ctk.CTkFrame(root)
panel_frame.pack(pady=20)


# Create the radio buttons
radio_var = ctk.IntVar()


radio_1 = ctk.CTkRadioButton(panel_frame, text="Option 1", variable=radio_var, value=1, font=("Arial", 12, "bold"))
radio_1.grid(row=0, column=0, padx=(10, 0), pady=10)


radio_2 = ctk.CTkRadioButton(panel_frame, text="Option 2", variable=radio_var, value=2, font=("Arial", 12, "bold"))
radio_2.grid(row=0, column=1, padx=(10, 0), pady=10)


# Create the checkboxes
check_var = ctk.IntVar()


check_1 = ctk.CTkCheckBox(panel_frame, text="Checkbox 1", variable=check_var, onvalue=1, offvalue=0, font=("Arial", 12, "bold"))
check_1.grid(row=1, column=0, padx=(10, 0), pady=10)


check_2 = ctk.CTkCheckBox(panel_frame, text="Checkbox 2", variable=check_var, onvalue=1, offvalue=0, font=("Arial", 12, "bold"))
check_2.grid(row=1, column=1, padx=(10, 0), pady=10)


# Create the buttons
def button_click():
    print("Button clicked!")


button = ctk.CTkButton(panel_frame, text="Click me!", font=("Arial", 12, "bold"), command=button_click)
button.grid(row=2, column=0, columnspan=2, padx=(10, 0), pady=10)


# Run the main loop
root.mainloop()