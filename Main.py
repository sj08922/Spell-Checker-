from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from TST_Helpers import *


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # Allowing only .txt files
    if filepath:
        # Read the content of the selected file
        with open(filepath, 'r') as file:
            content = file.read()
        text.delete(1.0, END)
        text.insert(1.0, content)

def display_checked_text(): #Average/Worst Case: O(n * k), where n is the number of words in the input text and k is the average length of the words. This is because it calls check_spelling, which in turn calls search for each word
    input_text = text.get("1.0", END).strip()
    if not input_text:
        messagebox.showinfo("Empty Text", "Please enter text.")
        return

    checked_text, misspelled_words = check_spelling(input_text)
    misspelledText.set(", ".join(misspelled_words))

    new_window = Toplevel(window)
    new_window.title("Checked Text")
    new_window.geometry('800x600')
    new_window.config(bg='white')

    # Create a Text widget for the checked text
    checked_text_widget = Text(new_window, wrap=WORD, font=('calibre', 15))
    checked_text_widget.pack(expand=True, fill=BOTH)

# Insert the checked text into the Text widget
    for word in checked_text:
        if word in misspelled_words:
            # Insert misspelled word with a tag for highlighting
            checked_text_widget.insert(END, word, 'misspelled')
            checked_text_widget.insert(END, " ")  # Insert space without any tag
        else:
        # Insert correctly spelled word followed by a space
            checked_text_widget.insert(END, word + " ")
    
    # Configure the tag for highlighting misspelled words
    checked_text_widget.tag_configure('misspelled', background='red', underline=True)
    checked_text_widget.delete("end-2c", END)

    # Disable the Text widget to prevent editing
    checked_text_widget.config(state=DISABLED)

def display_text():
    input_text = text.get("1.0", END).strip() 
    if not input_text:
        messagebox.showinfo("Empty Text", "Please enter text.")
        return 

window = Tk()
window.title("Spell Checker")
window.geometry('1920x1080')
window.config(bg='coral1')

misspelledText = StringVar(window)

Label(window, text='Spell Checker', bg='coral1', fg='gray10', font=('Times', 30, 'bold')).place(x=770, y=30, anchor='center')
Label(window, text='Please enter text or upload file:', bg='coral1', font=('calibre', 18, 'normal')).place(x=200, y=100, anchor='center')
text = ScrolledText(window, width=70, height=10, font=('calibre', 15, 'normal'))
text.place(x=770, y=190, anchor='center')
Button(window, text="Check Spelling", bg='SlateGray4', font=('calibre', 15), command=display_checked_text).place(x=700, y=320)
Button(window, text="Upload File", bg='SlateGray4', font=('calibre', 15), command=open_file).place(x=1000, y=320)

Label(window, text='Misspelled Words:', bg='coral1', font=('calibre', 14)).place(x=770, y=400, anchor='center')
misspelled_words_label = Label(window, textvariable=misspelledText, bg='coral1', font=('calibre', 14))
misspelled_words_label.place(x=770, y=430, anchor='center')

window.mainloop()








