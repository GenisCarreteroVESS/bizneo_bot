import tkinter as tk
from tkinter import messagebox

def process():
    value1 = entry1.get()
    value2 = entry2.get()
    messagebox.showinfo("Resultat", f"Camp 1: {value1}\nCamp 2: {value2}")

root = tk.Tk()
root.title("La meva GUI")
root.geometry("300x150")

tk.Label(root, text="Camp 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Camp 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Enviar", command=process).pack(pady=10)

root.mainloop()
