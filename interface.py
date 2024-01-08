import PySimpleGUI as sg
from tts import SoundGenerator 
 
sg.theme('DarkBrown1') # тема

layout = [[sg.Text('Please enter the text to convert it to mp3: ')], 
          [sg.Text()],
          [sg.OK(), sg.Cancel()]]

window = sg.Window('Text to speach', layout, size=(500, 200), enable_close_attempted_event=True)

while True:
    event, values = window.read()

    if event:
        pass

    if (event in (sg.WIN_CLOSED, 'Cancel')) and sg.popup_yes_no('Do you really want to exit?') == "Yes":
        break


window.close()



# import PySimpleGUI as sg
# from tts import SoundGenerator

# layout = [
#     [sg.Text('Filename:'), sg.Input(key='filename_input')],
#     [sg.Text('Phrase:'), sg.Input(key='phrase_input')],
#     [sg.Button('Save As')],
# ]

# window = sg.Window('Sound Generator', layout, size=(None, None), element_justification='left')

# while True:
#     event, values = window.read()

#     if event == sg.WINDOW_CLOSED:
#         break

#     if event == 'Save As':
#         filename = values['filename_input']
#         phrase = values['phrase_input']

#         if filename:
#             if not filename.endswith('.mp3'):
#                 filename += '.mp3'

#             sound_generator = SoundGenerator(filename, phrase)
#             sound_generator.save_sound()
#             # Здесь можно добавить любую другую логику, связанную с сохранением звука

# window.close()





