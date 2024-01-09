from googletrans import Translator, constants
from pprint import pprint

translator = Translator()
def translate(text, language):
    # translate a spanish text to english text (by default)
    translation = translator.translate(text, dest=language)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


translate('Como é amigo?', 'en')