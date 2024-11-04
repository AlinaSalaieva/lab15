import tkinter as tk
import json

def find_workers():
    company_name = entry.get()
    with open('companies.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        workers_count = data.get(company_name, "Фірму не знайдено")
        result_label.config(text=f"Чисельність робітників: {workers_count}")

root = tk.Tk()
root.title("Будівельні фірми")
root.geometry("450x280")
root.configure(bg='yellow')

label = tk.Label(root, text="Введіть назву фірми:", bg='yellow')
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Знайти", command=find_workers)
button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", bg='yellow')
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
