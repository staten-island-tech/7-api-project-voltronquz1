import tkinter as tk
from tkinter import messagebox
import requests
import random

# ------------------ POKEAPI FUNCTIONS ------------------

def get_random_pokemon():
    pokemon_id = random.randint(1, 151)  # First generation
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()

    name = data["name"]
    types = [t["type"]["name"] for t in data["types"]]

    return name, types

# ------------------ GAME LOGIC ------------------

def new_game():
    global pokemon_name, pokemon_types
    pokemon_name, pokemon_types = get_random_pokemon()
    entry.delete(0, tk.END)
    hint_label.config(text="")
    result_label.config(text="Guess the Pokémon!")

def check_guess():
    guess = entry.get().lower()

    if not guess:
        messagebox.showwarning("Warning", "Enter a Pokémon name.")
        return

    if guess == pokemon_name:
        result_label.config(text="Correct! 🎉", fg="green")
    else:
        result_label.config(text="Wrong! ❌ Try again.", fg="red")

def show_hint():
    types = ", ".join(t.capitalize() for t in pokemon_types)
    hint_label.config(text=f"Hint: Type(s) → {types}")

# ------------------ TKINTER UI ------------------

root = tk.Tk()
root.title("Pokémon Guessing Game")
root.geometry("400x300")

title = tk.Label(root, text="Guess the Pokémon!", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

hint_button = tk.Button(root, text="Hint", command=show_hint)
hint_button.pack(pady=5)

hint_label = tk.Label(root, text="", font=("Arial", 10))
hint_label.pack(pady=5)

result_label = tk.Label(root, text="Guess the Pokémon!", font=("Arial", 12))
result_label.pack(pady=10)

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack(pady=10)

# Start first game
new_game()

root.mainloop()