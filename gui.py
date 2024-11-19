import PySimpleGUI as sg

# Where we will build our GUI.  This one is for gathering a name. Maybe Supriti? Maybe not.
layout = [
    [sg.Text("What's your name?")],
    [sg.InputText(key='-INPUT-')],
    [sg.Text(size=(55, 1), key='-OUTPUT-')],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

# Makes the window,
window = sg.Window('Hello MIS', layout)

# Event Loop to get the value entered --  the requested name in this file.
while True:
    event, values = window.read()

    # this tells the program to break -- stop -- when the window is closed or cancel is hit. Breaks the loop.
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # This takes the input and displays it back out in the window.
    if event == 'Ok':
        greeting = f'Hello {values["-INPUT-"]}, I hope you are having a good Tuesday.'
        window['-OUTPUT-'].update(greeting)

window.close()
