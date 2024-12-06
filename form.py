import PySimpleGUI as sg
import pandas as pd
sg.theme('DarkTeal9')
EXCEL_FILE = 'form.xlsx'
df = pd.read_excel(EXCEL_FILE)
layout = [
    [sg.Text('Please fill the form')],
    [sg.Text('Name', size=(15, 1)), sg.InputText(key='Name')],
    [sg.Text('Reg.no', size=(15, 1)), sg.InputText(key='Reg.no')],
    [sg.Text('Department', size=(15, 1)), sg.Combo(['CSE', 'ECE', 'Mech'], key='Department')],
    [sg.Text('After College', size=(15, 1))],
    [
        sg.Checkbox('Placement', key='Placement'),
        sg.Checkbox('Higher studies', key='Higher studies'),
        sg.Checkbox('Business', key='Business')
    ],
    [sg.Button('Submit'), sg.Button('Clear'), sg.Button('Exit')]
]
def clear_input():
    for key in values:
        window[key]('')
    return None

window = sg.Window('Form', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':  
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
         new_data = pd.DataFrame([values])
         df = pd.concat([df, new_data], ignore_index=True)
         df.to_excel(EXCEL_FILE, index=False)
         sg.popup('Data saved!')
         clear_input()
window.close()

