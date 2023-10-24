import json

import functions
from functions import *
import PySimpleGUI as sg

with open('recipes.json', 'r', encoding='utf-8') as file:
    content = file.read()

# import recipes
recipes = json.loads(content)

# load names in a list
name_list = []
for cocktail in recipes:
    name_list.append(cocktail['name'])
    name_list = sorted(name_list)

# create buttons / boxes
list_box = sg.Listbox(values=name_list,key='name_list',
                      enable_events=True, size=(20, 20))
info_box = sg.Multiline(key='info_box', size=(48, 20), disabled=True)
search_button1 = sg.Button('Search', key='search_name_b')
search_button2 = sg.Button('Search', key='search_ingr_b')
label1 = sg.Text('Search by name:')
label2 = sg.Text('Search by ingredient:')
search_name = sg.InputText(tooltip='enter cocktail name', key='search_name')
search_ingr = sg.InputText(tooltip='enter an ingredient', key='search_ingr')
found_matches = sg.Text()

# window layout
window = sg.Window("Cocktail Database",
                   layout=[[label1, search_name, search_button1],
                           [label2, search_ingr, search_button2],
                           [found_matches],
                           [list_box, info_box]],
                   font=('Helvetica', 14))
# main loop
while True:
    event, values = window.read()
    match event:
        case 'name_list':
            window['info_box'].update('')
            hgl_name = values['name_list'][0]
            for line in functions.display_info(hgl_name, recipes):
                window['info_box'].print(line)
        case sg.WIN_CLOSED:
            break

