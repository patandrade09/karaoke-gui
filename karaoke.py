import PySimpleGUI as sg
import vlc


sg.theme('Dark Blue 3')  

layout = [[sg.Text('Insira o código da Música'), sg.Text(size=(12,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Abrir'), sg.Button('Fechar')]]

window = sg.Window('Karaokê do Academy', layout)


def open_video():   
    value = values['-IN-']
    if value == '1':
        value = value + '.mp4'
        media = vlc.MediaPlayer(value)
        media.play()
        vlc.libvlc_set_fullscreen(media, True)
        
    else:
        value = value + '.avi'
        media = vlc.MediaPlayer(value)
        media.play()
        vlc.libvlc_set_fullscreen(media, True)


while True:  
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Fechar':
        break
    if event == 'Abrir':
        open_video()
        window['-OUTPUT-'].update(values['-IN-'])
        

window.close()




