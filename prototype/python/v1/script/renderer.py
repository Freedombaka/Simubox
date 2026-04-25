import tkinter as tk

# 1. Create the main window
root = tk.Tk()

# 2. Set window properties
root.title("My Python Window")
root.geometry("400x300")

# 3. Add a simple widget (Optional)
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# 4. Start the application
root.mainloop()
