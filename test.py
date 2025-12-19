import tkinter as tk
import os
API_KEY = os.getenv("dad6addc-d461-4fc7-a407-071967c5638d")

if not API_KEY:
    raise RuntimeError("API key not found")

def call_api():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(
        "https://tcg.pokemon.com/en-us/",
        headers=headers
    )
    result_label.config(text=response.text)

root = tk.Tk()
root.title("Tkinter API App")

tk.Button(root, text="Call API", command=call_api).pack(pady=10)
result_label = tk.Label(root, text="Waiting...")
result_label.pack()

root.mainloop()