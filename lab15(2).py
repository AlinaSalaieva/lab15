import tkinter as tk
from collections import Counter

def count_letters():
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read().lower()
        counts = Counter(c for c in text if c.isalpha())
        result = "\n".join(f"{char}: {count}" for char, count in counts.items())
        result_label.config(text=result)

root = tk.Tk()
root.title("Лічильник літер")
root.geometry("450x280")

button = tk.Button(root, text="Порахувати літери", command=count_letters)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
