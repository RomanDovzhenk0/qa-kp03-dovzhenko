import PySimpleGUI as sg
import requests
from PySimpleGUI import WIN_CLOSED

layout = [
    [sg.Text('Path:'), sg.InputText(key='PATH', size=52), sg.Button("      Find      "), sg.Button("   Move   ")],
    [sg.Text(size=(60, 20), key='OUTPUT')],
    [sg.Button("      Create folder      "), sg.Button("    Create binary file    "),
     sg.Button("    Create log text file    "), sg.Button("    Create buffer file    ")]
]


def getFolders():
    response = requests.get('http://localhost:5000/directories?path=' + values['PATH'])
    list = response.text.replace('["', '/...\n/').replace('", "', '\n/').replace('"]', '').replace('[]', '/...')
    window['OUTPUT'].update(value=list)


def block_focus(window):
    for key in window.key_dict:  # Remove dash box of all Buttons
        element = window[key]
        if isinstance(element, sg.Button):
            element.block_focus()


def popup_move():
    layout = [
        [sg.Text("Path:"), sg.InputText(key='PATH')],
        [sg.Text("New Path:"), sg.InputText(key='NEW_PATH')],
        [sg.Button('OK'), sg.Button('CANCEL')]
    ]
    window = sg.Window("Move", layout, use_default_focus=False, finalize=True, modal=True)
    block_focus(window)
    while True:
        event, values = window.read()
        if event == WIN_CLOSED:
            break
        if event == 'OK':
            response = requests.put('http://localhost:5000/directories?path=' + values['PATH'] + '&newPath=' + values['NEW_PATH'])
            break
        if event == 'CANCEL':
            break
    window.close()
    return None


def popup_open_binary_file(content, path):
    col_layout = [[sg.Button('DELETE')]]
    layout = [
        [sg.Text("Content:\n")],
        [sg.Text(content)],
        [sg.Column(col_layout, expand_x=True, element_justification='center')],
    ]
    window = sg.Window("File", layout, use_default_focus=False, finalize=True, modal=True)
    block_focus(window)
    while True:
        event, values = window.read()
        if event == WIN_CLOSED:
            break
        if event == 'DELETE':
            response = requests.delete('http://localhost:5000/binaryfiles?path=' + path)
            break
    window.close()
    return None


def popup_open_buffer_file(content, path):
    col_layout = [[sg.Button('ADD CONTENT')], [sg.Button('DELETE')]]
    layout = [
        [sg.Text("Content:\n")],
        [sg.Text(content)],
        [sg.Column(col_layout, expand_x=True, element_justification='center')],
    ]
    window = sg.Window("File", layout, use_default_focus=False, finalize=True, modal=True)
    block_focus(window)
    while True:
        event, values = window.read()
        if event == WIN_CLOSED:
            break
        if event == 'ADD CONTENT':
            content = sg.popup_get_text('Enter content:', keep_on_top=True)
            response = requests.put('http://localhost:5000/bufferfiles?path=' + path + '&content=' + content)
            break
        if event == 'DELETE':
            response = requests.delete('http://localhost:5000/bufferfiles?path=' + path)
            break
    window.close()
    return None


def popup_open_log_file(content, path):
    col_layout = [[sg.Button('ADD CONTENT')], [sg.Button('DELETE')]]
    layout = [
        [sg.Text("Content:\n")],
        [sg.Text(content)],
        [sg.Column(col_layout, expand_x=True, element_justification='center')],
    ]
    window = sg.Window("File", layout, use_default_focus=False, finalize=True, modal=True)
    block_focus(window)
    while True:
        event, values = window.read()
        if event == WIN_CLOSED:
            break
        if event == 'ADD CONTENT':
            content = sg.popup_get_text('Enter content:', keep_on_top=True)
            response = requests.put('http://localhost:5000/logtextfiles?path=' + path + '&content=' + content)
            break
        if event == 'DELETE':
            response = requests.delete('http://localhost:5000/logtextfiles?path=' + path)
            break
    window.close()
    return None


window = sg.Window('FileSystem', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break

    if event == '   Move   ':
        popup_move()
        getFolders()

    if event == '      Find      ':
        if str(values['PATH']).endswith('.bin'):
            response = requests.get('http://localhost:5000/binaryfiles?path=' + values['PATH'])
            popup_open_binary_file(response.text, values['PATH'])
        if str(values['PATH']).endswith('.buf'):
            response = requests.get('http://localhost:5000/bufferfiles?path=' + values['PATH'])
            popup_open_buffer_file(response.text, values['PATH'])
        if str(values['PATH']).endswith('.log'):
            response = requests.get('http://localhost:5000/logtextfiles?path=' + values['PATH'])
            popup_open_log_file(response.text, values['PATH'])
        else:
            getFolders()

    if event == '      Create folder      ':
        folder_name = sg.popup_get_text('Enter folder name:', keep_on_top=True)
        response = requests.post('http://localhost:5000/directories?path=' + values['PATH'] + '/' + folder_name)
        if response.status_code != 201:
            sg.popup_error("Can't create folder\n" + response.text)
        getFolders()

    if event == '    Create binary file    ':
        file_name = sg.popup_get_text('Enter file name:', keep_on_top=True)
        content = sg.popup_get_text('Enter content:', keep_on_top=True)
        response = requests.post('http://localhost:5000/binaryfiles?path=' + values['PATH'] + '/' + file_name + '.bin&content=' + content)
        if response.status_code != 201:
            sg.popup_error("Can't create folder\n" + response.text)
        getFolders()

    if event == '    Create log text file    ':
        file_name = sg.popup_get_text('Enter file name:', keep_on_top=True)
        response = requests.post('http://localhost:5000/logtextfiles?path=' + values['PATH'] + '/' + file_name + '.log')
        if response.status_code != 201:
            sg.popup_error("Can't create folder\n" + response.text)
        getFolders()

    if event == '    Create buffer file    ':
        file_name = sg.popup_get_text('Enter file name:', keep_on_top=True)
        response = requests.post('http://localhost:5000/bufferfiles?path=' + values['PATH'] + '/' + file_name + '.buf')
        if response.status_code != 201:
            sg.popup_error("Can't create folder\n" + response.text)
        getFolders()
