# Packages
from tkinter import *


# NLP Pkgs
from nltk_summarization import nltk_summarizer

# Structure and Layout
window = Tk()
window.title("Text Summarization")
window.config(background='black')

# Functions
def get_summary():
	raw_text = str(textentry.get('1.0',END))
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	output.insert(END,result)


# Clear entry
def clear_text():
	textentry.delete('1.0',END)

def clear_display_result():
	output.delete('1.0',END)

def close():
	window.destroy()
	exit()

#GUI
Label(window, text="Enter the text below to summarize: ", padx=248, pady=10, bg="yellow").grid(row=0, column=0, sticky=W)
textentry=Text(window,width=75,height=25,wrap=WORD,padx=100, pady=10,background="white")
textentry.grid(row=1, column=0)


Button(window,text="submit", width=7,command=get_summary).grid(row=4, column=0)
Label(window, text="   ", padx=248, pady=10, bg="black").grid(row=3, column=0, sticky=W)
Button(window,text="clear", width=7,command=clear_text).grid(row=1, column=1)
Label(window, text="   ", padx=248, pady=10, bg="black").grid(row=5, column=0, sticky=W)

Label(window, text="The Summarized text is:  ", padx=280, pady=10, bg="yellow").grid(row=6, column=0, sticky=W)

output=Text(window,width=75,height=15,wrap=WORD,padx=100, pady=10,background="white")
output.grid(row=7, column=0, columnspan=1)

Button(window,text="clear result", width=10,command=clear_display_result).grid(row=7, column=1)
Label(window, text="   ", padx=248, pady=10, bg="black").grid(row=8, column=0, sticky=W)
Label(window, text="   ", padx=248, pady=10, bg="black").grid(row=10, column=0, sticky=W)

#exit
Button(window,text="Exit", width=5,command=close).grid(row=9, column=0)

window.mainloop()






# #GUI
# Label(window, text="Enter the text below to summarize: ", padx=248, pady=10, bg="yellow").grid(row=0, column=0, sticky=W)
# textentry=Text(window,width=75,height=10,wrap=WORD,padx=100, pady=10,background="white")
# textentry.grid(row=1, column=0)
#
#
# Button(window,text="submit", width=7,command=get_summary).grid(row=3, column=0)
# Label(window, text="   ", padx=248, pady=10, bg="black").grid(row=4, column=0, sticky=W)
# Button(window,text="clear", width=7,command=clear_text).grid(row=5, column=0)
#
# Label(window, text="The Summarized text is:  ", padx=280, pady=10, bg="yellow").grid(row=6, column=0, sticky=W)
#
# output=Text(window,width=75,height=10,wrap=WORD,padx=100, pady=10,background="white")
# output.grid(row=7, column=0, columnspan=1)
#
# Button(window,text="clear result", width=15,command=clear_display_result).grid(row=8, column=0)
#
# #exit
# Button(window,text="Exit", width=5,command=close).grid(row=9, column=0)
#
# window.mainloop()