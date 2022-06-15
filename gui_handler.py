import PySimpleGUI as sg
import generator

sg.theme("DarkGrey15")
layout = [
    [sg.Text("How many to generate : "), sg.In("", key="-AMOUNT-", size=(4, 1)), sg.Button("Generate", key="-GENERATE-")],
    [sg.Output(key="-OUTPUT-", size=(37, 6))]
]

window = sg.Window("Easy Username Generator", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == "-GENERATE-":
        generator.generate(values["-AMOUNT-"])

window.close()