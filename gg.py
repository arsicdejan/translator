from translate import Translator
translator = Translator(to_lang='ja')
try:
    with open('./test.txt', mode='r+') as file_to_translate:
        text_to_translate = (file_to_translate.read())
        translation = translator.translate(text_to_translate)
    with open('./translated.txt', mode='a') as translated:
        translated.write(translation)
except FileNotFoundError as e:
    print('File not found!')











