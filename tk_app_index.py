import tkinter as tk

# All dictionaries are stored in this file
from dictionaries import *

def handle_navigate_forward(target):
    global current_language
    current_language = target
    print(f"{target} button clicked!")
    print(f"Current language: {current_language}")
    button_frame.pack_forget()
    subheading1.pack_forget()
    subheading2.pack()
    translation_frame.pack()
    word_entry.pack()
    translation_label.pack()
    translate_button.pack()
    back_button.pack()

def handle_navigate_back():
    translation.set("")
    word_entry.delete(0, tk.END)
    translation_frame.pack_forget()
    subheading1.pack()
    button_frame.pack()
    yoruba_button.pack()
    # Make sure you change the name of your button here
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()

def translate_word(word, language):
    print(f"Translating {word} from {language}")

    if language == "yoruba":
        if word in yoruba_dictionary:
            print(yoruba_dictionary[word])
            translation.set(yoruba_dictionary[word])
        else:
            print("Not found")
            translation.set("Word not found")

    # Check for other languages here (right not we are only checking for the yoruba words)
    # Make sure your add your dictionary to the ./dictionaries file first 

    else:
        print("Language not supported")

root = tk.Tk()
root.geometry("720x480")
root.title("Tkinter Language Dictionary")

# Create a heading and subheading
subheading2_text = tk.StringVar()
heading = tk.Label(root, text="Welcome to the Tkinter language dictionary", font=("Arial", 20), pady=20)
subheading1 = tk.Label(root, text="Select a language to translate from", font=("Arial", 15), pady=10)
subheading2 = tk.Label(root, textvariable=subheading2_text, font=("Arial", 15), pady=10)

# Create buttons frame with buttons for each language
button_frame = tk.Frame(root)
yoruba_button = tk.Button(button_frame, text="Yoruba", width=30, pady=5, command=lambda:handle_navigate_forward("yoruba"))

# Pick a button for your desired language
# Miracle - button2/language2
# Israel - button3/language3
# Benedict - button3/language3
# King David - button4/language4

# Replace the text attribute from "LanguageX" to your desired language
# Replace the "language" parameters in the lambda functions with your corresponding language
button2 = tk.Button(button_frame, text="Language2", width=30, pady=5, command=lambda:handle_navigate_forward("language2"))
button3 = tk.Button(button_frame, text="Language3", width=30, pady=5, command=lambda:handle_navigate_forward("language3"))
button4 = tk.Button(button_frame, text="Language4", width=30, pady=5, command=lambda:handle_navigate_forward("language4"))
button5 = tk.Button(button_frame, text="Language5", width=30, pady=5, command=lambda:handle_navigate_forward("language5"))

# Create frame for specific language translation
translation = tk.StringVar()
translation_frame = tk.Frame(root)
word_entry = tk.Entry(translation_frame, width=30)
translate_button = tk.Button(translation_frame, text="Translate", width=30, pady=5, command=lambda:translate_word(word_entry.get(), current_language))
translation_label = tk.Label(translation_frame, textvariable=translation, font=("Arial", 15), pady=10)
back_button = tk.Button(translation_frame, text="Back", width=30, pady=5, command=handle_navigate_back)

heading.pack()
subheading1.pack()
button_frame.pack()
yoruba_button.pack()

# Make sure your change the name of your button here
button2.pack()
button3.pack()
button4.pack()
button5.pack()

root.mainloop()