import os
from gtts import gTTS

class SoundGenerator:
    def __init__(self, filename, phrase, lang='en', path=None):
        self.phrase = phrase
        self.filename = filename
        self.lang = lang
        self.path = path

    def generate_sound(self):
        tts = gTTS(self.phrase, lang=self.lang)
        return tts

    def save_sound(self):
        if not self.filename:
            self.filename = 'default'

        if self.path == '' or self.path is None:  # Используйте директорию скрипта в качестве пути по умолчанию
            self.path = os.path.dirname(os.path.realpath(__file__))
            path_and_file = os.path.join(self.path, self.filename + '.mp3')
        else:  # Используйте указанный путь
            path_and_file = os.path.join(self.path, self.filename + '.mp3')

        tts = self.generate_sound()
        tts.save(path_and_file)

if __name__ == '__main__':
    filename = input('Введите название файла: ')
    phrase = input('Введите фразу для озвучки (обязательно): ')
    path = input('Введите желаемый путь до файла (необязательно): ')
    lang = input('ru/en: ').lower()

    generated_sound = SoundGenerator(filename, phrase, lang, path)
    generated_sound.save_sound()

# from gtts import gTTS
# import os

# class SoundGenerator:
#     def __init__(self, filename, phrase, lang='en', path=None):
#         self.phrase = phrase
#         self.filename = filename
#         self.lang = lang
#         self.path = path

#     def generate_sound(self):
#         tts = gTTS(self.phrase, lang=self.lang)
#         return tts

#     def save_sound(self):
#         if not self.filename:
#             self.filename = 'default'

#         if self.path is None: # путь по умолчанию
#             self.path = os.path.dirname(os.path.abspath(__file__))
#             path_and_file = os.path.join(self.path, self.filename + '.mp3')
#         else: # указываемый путь
#             path_and_file = os.path.join(self.path, self.filename + '.mp3')

#         tts = self.generate_sound()
#         tts.save(path_and_file)

# if __name__ == '__main__':
#     filename = input('Введите название файла : ')
#     phrase = input('Введите фразу для озвучки (обязательно): ')
#     path = input('Введите желаемый путь до файла (необязательно): ')
#     lang = input('ru/en: ').lower()

#     generated_sound = SoundGenerator(filename, phrase, lang, path)
#     generated_sound.save_sound()

# from gtts import gTTS
# import os

# class SoundGenerator:
#     def __init__(self, filename, phrase, lang='en', path=None):
#         self.phrase = phrase
#         self.filename = filename
#         self.lang = lang
#         self.path = path

#     def generate_sound(self):
#         tts = gTTS(self.phrase, lang=self.lang)
#         return tts

#     def save_sound(self):
#         if not self.filename:
#             self.filename = 'default'

#         if self.path is None:
#             self.path = os.path.dirname(os.path.abspath(__file__))
#             path_and_file = os.path.join(self.path, self.filename + '.mp3')
#         else:
#             path_and_file = os.path.join(self.path, self.filename + '.mp3')

#         tts = self.generate_sound()
#         tts.save(path_and_file)

# if __name__ == '__main__':
#     filename = input('Введите название файла : ')
#     phrase = input('Введите фразу для озвучки (обязательно): ')
#     path = input('Введите желаемый путь до файла (необязательно): ')
#     lang = input('ru/en: ').lower()

#     generated_sound = SoundGenerator(filename, phrase, lang, path)
#     generated_sound.save_sound()



"""
from gtts import gTTS
import os

class SoundGenerator:
    def __init__(self, filename, phrase, lang='en', path=None):
        self.phrase = phrase
        self.filename = filename
        self.lang = lang
        self.path = path

    def generate_sound(self):
        tts = gTTS(self.phrase, lang=self.lang)
        return tts

    def save_sound(self, path_and_file=None):
        if not self.filename:
            self.filename = 'default'

        if path_and_file is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            path_and_file = os.path.join(script_dir, self.filename + '.mp3')
        else:
            path_and_file = os.path.join(self.path, self.filename + '.mp3')

        tts = self.generate_sound()
        tts.save(path_and_file)

if __name__ == '__main__':
    filename = input('Введите название файла : ')
    phrase = input('Введите фразу для озвучки (обязательно): ')
    path = input('Введите желаемый путь до файла (необязательно): ')
    lang = input('ru/en: ').lower()

    generated_sound = SoundGenerator(filename, phrase, lang, path)
    generated_sound.save_sound()

"""

"""
from gtts import gTTS
import os

class SoundGenerator:
    def __init__(self, filename, phrase, lang='en', path=None): # можно менять язык на 'ru'
        self.phrase = phrase
        self.filename = filename
        self.lang = lang
        self.path = path

    def generate_sound(self):
        if not self.filename: # проверка имени файла
            self.filename = 'default.mp3'
        else:
            self.filename = self.filename + '.mp3'

        if self.path is None: # путь в ту же папку с исполняемым скриптом
            script_dir = os.path.dirname(os.path.abspath(__file__))
            path_and_file = os.path.join(script_dir, self.filename)
        else:
            path_and_file = os.path.join(self.path, self.filename)

        tts = gTTS(self.phrase, lang=self.lang)
        self.save_sound(tts, path_and_file)
        print('Файл сохранен по пути:', path_and_file)

    def save_sound(self, tts, path_and_file):
        tts.save(path_and_file)
"""

# class SoundGenerator:
#     def __init__(self, filename, phrase, lang='en', path=None): # можно менять язык на 'ru'
#         self.phrase = phrase
#         self.filename = filename
#         self.lang = lang
#         self.path = path

#     def generate_sound(self, phrase, path_and_file):
#         tts = gTTS(phrase, path_and_file )
#         return tts


#     def save_sound(self, phrase, path_and_file):
#         generate_sound(phrase, path_and_file)
#         if not self.filename: # проверка имени файла
#             self.filename = 'default.mp3'
#         else:
#             self.filename = self.filename + '.mp3'

#         if self.path is None: # путь в ту же папку с исполняемым скриптом
#             script_dir = os.path.dirname(os.path.abspath(__file__))
#             path_and_file = os.path.join(script_dir, self.filename)
#         else:
#             path_and_file = os.path.join(self.path, self.filename)
#         tts.save(path_and_file)


# if __name__ == '__main__':
#     phrase = input('Введите фразу для озвучки: ')
#     filename = input('Введите название файла: ')
#     path = input('Введите желаемый путь до файла (необязательно):')

#     sound_generator = SoundGenerator(filename, phrase)
#     sound_generator.generate_sound()