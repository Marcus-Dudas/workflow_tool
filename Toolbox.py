#! /usr/bin/env python3

"""
08/18/19- Make buttons editable with names stored in variables used as labels. In Edit Mode, 1st screen edits buttons,
second screen allows for input of url list. See if Python has built-in Path finders for applications, to include entry
box for list of Apps to launch. May be good to enforce double-click to avoid surprise launches. For Windows version,
figure out path conventions and make Desktop icon.
ASAP: Ditch variables for URLS, include directly in list as string with direction to separate with ", "


How to start off every day?
Open sites to have some play.
News and quizzes, forums, vids,
Trading news and eBay bids

Get that stuff right out the way
so you can have productive day
"""

import webbrowser
import os

from tkinter import *
from tkinter import ttk

"""
Core functions: webkit call, app call, notebook save
"""
def open_pages (url_list):

    for item in url_list:
        current_url= item
        webbrowser.open_new(current_url)

def open_app (app_path):

    try:
        os.system("open "+app_path)
    except:
        return

def open_tools(url_list, app_path=None):

    open_pages(url_list)
    open_app(app_path)


def new_note_procedure(event=None):

    new_note_file= open('tool_notes.txt', 'w')
    new_note = notes.get('1.0', 'end-1c')
    new_note_file.write(new_note)
    new_note_file.close()

#def button_edit ():

"""
Names of Buttons, for function directly above. 
"""

b_one= str("General")
b_two= str("JavaScript")
b_three= str("R")
b_four= str("Python")
b_five= str("Web-Dev")
b_six= str("Research")
b_seven= str("Business/Finance")
b_eight= str("Communication")
"""
Apps to be called
"""
r_studio_app= str("/Applications/RStudio.app")
brackets_app= str("/Applications/Brackets.app")
pycharm_app= str("/Applications/PyCharm\ CE.app")
zotero_app= str("/Applications/Zotero.app")
oanda_app= str("/Applications/fxTradePractice\ 4.app")

"""
Online resources
"""

#News and like resources
CNN = str('https://www.cnn.com/')
TheGuardian= str('https://www.theguardian.com/us')
Reuters = str('https://www.reuters.com/')
APnews = str('https://www.apnews.com/')
BuzzfeedNews = str("https://www.buzzfeednews.com/")
wired= str("https://www.wired.com/")
dzone= str("https://dzone.com/portals")
ecosia = str('https://www.ecosia.org/')

#Python Resources
PythonSite = str('https://docs.python.org/3/')
Kivy = str('https://kivy.org/doc/stable/api-kivy.html')
ATBS = str ('https://automatetheboringstuff.com/')
PyTutorials= str("https://www.python-course.eu/")
NatLangTK= str("http://www.nltk.org/")

#JavaScript resources
JS_docs= str("https://developer.mozilla.org/en-US/docs/Web/JavaScript")
eloquent_JS= str("https://eloquentjavascript.net/")
jquer= str("https://api.jquery.com/")

#R resources
cran= str("https://cran.r-project.org/")
ggplot= str("https://ggplot2.tidyverse.org/index.html")
r_studio= str("https://www.rstudio.com/online-learning/")

#Research
OnlineRes= str('https://www.tandfonline.com/doi/full/10.1080/14780887.2015.1008909')
research_database= str()
open_sci_found= str("https://osf.io/")

#Comm & Collab
github= str("https://github.com/")
email= str("https://mail.google.com/")
Reddit= str('https://www.reddit.com/')
stack= str("https://stackoverflow.com/")

#Web Development
w3= str("https://www.w3schools.com/")
mozilla_web= str("https://developer.mozilla.org/en-US/docs/Web")
color_picker= str("https://www.colorcodehex.com/design-color-scheme.html")
browser_check= str("https://caniuse.com/")
design_resource= str("https://tympanus.net/codrops/")

#Business and Finance
forex= str("https://www.forexfactory.com/")
oanda_api= str("https://developer.oanda.com/rest-live-v20/introduction/")

#list definition
python = [PythonSite, Kivy, ATBS, PyTutorials, NatLangTK]
news = [CNN, TheGuardian, APnews, Reuters, wired, dzone, BuzzfeedNews, ecosia]
comms = [github, email, Reddit, stack]
javaScript = [JS_docs, eloquent_JS, jquer]
R_lang = [cran, ggplot, r_studio]
research= [OnlineRes, research_database, open_sci_found]
web_dev = [w3, mozilla_web, color_picker, browser_check, design_resource]
business = [forex, oanda_api]

"""GUI code"""

root = Tk()
root.title("Workflow Interface")

#Tools grid
mainframe = ttk.Frame(root)
mainframe.grid()
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Button object creation and event bindings
start_up_B= ttk.Button(mainframe, width=15, text=b_one, command= lambda: open_pages(news))
javascript_docs_B= ttk.Button(mainframe, width=15, text=b_two, command= lambda: open_pages(javaScript))
learning_r_B= ttk.Button(mainframe, width=15, text=b_three, command= lambda: open_tools(R_lang, r_studio_app))
python_docs_B= ttk.Button(mainframe, width=15, text=b_four, command= lambda: open_tools(python, pycharm_app))
web_dev_B = ttk.Button(mainframe, width=15, text=b_five, command= lambda: open_tools(web_dev, brackets_app))
research_B= ttk.Button(mainframe, width=15, text=b_six, command= lambda: open_tools(research, zotero_app))
money_B= ttk.Button(mainframe, width=15, text=b_seven, command= lambda: open_tools(business, oanda_app))
communication_B= ttk.Button(mainframe, width=15, text=b_eight, command= lambda: open_pages(comms))
help_B= ttk.Button(mainframe, width=15, text="Edit")

#Note object creation, note-file object creation
notes= Text(mainframe, height=14)


note_file= open('tool_notes.txt', 'rt')
notes_contents= note_file.read()
notes.insert('1.0', notes_contents)
note_file.close()

notes.bind("<Shift-Up>", new_note_procedure)

#placements
notes.grid(column= 2, row=1, rowspan=9, sticky=N+E+S+W)
start_up_B.grid(column=1, row=1, sticky='w')
javascript_docs_B.grid(column=1, row=2, sticky='w')
learning_r_B.grid(column=1, row=3, sticky='w')
python_docs_B.grid(column=1, row=4, sticky='w')
web_dev_B.grid(column=1, row=5, sticky='w')
research_B.grid(column=1, row=6, sticky='w')
money_B.grid(column=1, row=7, sticky='w')
communication_B.grid(column=1, row=8, sticky='w')
help_B.grid(column=1, row=9, sticky='w')


#initializations of tabs and other
for child in root.winfo_children(): child.grid_configure()
for child in mainframe.winfo_children(): child.grid_configure()


#enter the infinite loop
root.mainloop()