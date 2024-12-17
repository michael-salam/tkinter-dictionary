from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("600x250")
window.title("Hausa Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

yoruba_dict = {
    "come": "wa",
    "go": "lo",
    "head": "ori",
    "back": "pada",
    "yes": "benni"
}

def search(word):
    if word in yoruba_dict:
        result.set(yoruba_dict[word])
        print(yoruba_dict[word])
    else:
        result.set("Not found")
        print("Not found")

search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()