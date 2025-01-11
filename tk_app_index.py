import tkinter as tk

# All dictionaries are stored in this file
from dictionaries import *

def pack_first_page():
    sub_heading.pack()
    button_frame.pack()
    yoruba_button.pack()
    spanish_button.pack()
    igbo_button.pack()
    italian_button.pack()
    german_button.pack()

def handle_navigate_forward(target):
    global current_language
    current_language = target
    print(f"{target} button clicked!")
    print(f"Current language: {current_language}")
    button_frame.pack_forget()
    sub_heading.pack_forget()
    translation_frame.pack()
    word_entry.pack()
    translation_label.pack()
    translate_button.pack()
    back_button.pack()

def handle_navigate_back():
    translation.set("")
    word_entry.delete(0, tk.END)
    translation_frame.pack_forget()
    pack_first_page()

def translate_word(word, language):
    print(f"Translating {word} from {language}")
    
    # Convert the word to lowercase to account for different cases
    word = word.lower()

    if language == "yoruba":
        if word in yoruba_dictionary:
            print(yoruba_dictionary[word])
            translation.set(yoruba_dictionary[word])
        else:
            print("Not found")
            translation.set("Word not found")

    elif language == "spanish":
        if word in spanish_dict:
            print(spanish_dict[word])
            translation.set(spanish_dict[word])
        else:
            print("Not found")
            translation.set("Word not found")
            
    elif language == "igbo":
        if word in igbo_dictionary:
            print(igbo_dictionary[word]) 
            translation.set(igbo_dictionary[word])      
        else:
            print("Not found")
            translation.set("Word not found")

    elif language == "italian":
        if word in italian_dictionary:
            print(italian_dictionary[word])
            translation.set(italian_dictionary[word])
        else:
            print("Not found")
            translation.set("Word not found")

    elif language == "german":
        if word in german_dictionary:
            print(german_dictionary[word])
            translation.set(german_dictionary[word])
        else:
            print("Not found")
            translation.set("word not found")

    else:
        print("Language not supported")

# Initialise tkinter app
root = tk.Tk()
root.geometry("720x480")
root.title("Tkinter Language Dictionary")

# Create a heading and subheading
heading = tk.Label(root, text="Welcome to the Tkinter language dictionary", font=("Arial", 20), pady=20)
sub_heading = tk.Label(root, text="Select a language to translate from", font=("Arial", 15), pady=10)

# Create buttons frame with buttons for each language
button_frame = tk.Frame(root)
yoruba_button = tk.Button(button_frame, text="Yoruba", width=30, pady=5, command=lambda:handle_navigate_forward("yoruba"))
spanish_button = tk.Button(button_frame, text="Spanish", width=30, pady=5, command=lambda:handle_navigate_forward("spanish"))
igbo_button = tk.Button(button_frame,text="Igbo", width=30, pady=5, command=lambda:handle_navigate_forward("igbo"))
italian_button = tk.Button(button_frame, text="Italian", width=30, pady=5, command=lambda:handle_navigate_forward("italian"))
german_button = tk.Button(button_frame, text="German", width=30, pady=5, command=lambda:handle_navigate_forward("german"))

# Create frame for second page - specific language translation
translation = tk.StringVar()
translation_frame = tk.Frame(root)
word_entry = tk.Entry(translation_frame, width=30, font=("Arial", 15))
translate_button = tk.Button(translation_frame, text="Translate", width=30, pady=5, command=lambda:translate_word(word_entry.get(), current_language))
translation_label = tk.Label(translation_frame, textvariable=translation, font=("Arial", 15), pady=10)
back_button = tk.Button(translation_frame, text="Back", width=30, pady=5, command=handle_navigate_back)

# Pack UI for first page
heading.pack()
pack_first_page()

root.mainloop()
