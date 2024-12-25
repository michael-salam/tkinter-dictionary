
from tkinter import Tk, Entry, Button, Label, StringVar

# Initialize the main window
window = Tk()
window.geometry("600x250")
window.title("World Dictionary")

# Input field for user to enter a word
entry_text = Entry(window, font=("Arial", 11))
entry_text.pack(pady=10)

# Result display
result = StringVar()
result_label = Label(window, textvariable=result, font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Expanded Dictionaries in hausa and igbo
hausa_dict = {
    "come": "zo",
    "go": "je",
    "head": "kai",
    "leg": "kafa",
    "food": "adinci",
    "water": "ruwa",
    "money": "kudi",
    "house": "gida",
    "friend": "aboki",
    "love": "kauna",
    "work": "aiki",
    "sleep": "bacci",
    "market": "kasuwa",
    "father": "uba",
    "mother": "uwa",
    "child": "yaro",
}

igbo_dict = {
    "water": "miri",
    "poo": "shit",
    "problem": "nosba",
    "come": "bịa",
    "go": "ga",
    "head": "isi",
    "leg": "ukwu",
    "food": "nri",
    "money": "ego",
    "house": "ụlọ",
    "friend": "enyi",
    "love": "ịhụnanya",
    "work": "ọrụ",
    "sleep": "ụra",
    "market": "ahịa",
    "father": "nna",
    "mother": "nne",
    "child": "nwata",
}

# Function to search for the word
def search(word):
    word = word.lower().strip()  # Normalize the input
    if word in hausa_dict:
        result.set(f"Hausa: {hausa_dict[word]}")
    elif word in igbo_dict:
        result.set(f"Igbo: {igbo_dict[word]}")
    else:
        result.set("Not found")

# Search button
search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()), font=("Arial", 11))
search_btn.pack(pady=10)

# Run the application
window.mainloop()
