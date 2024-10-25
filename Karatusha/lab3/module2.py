from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException

def TransLate(text, src='auto', dest='en'):
    try:
        if src == 'auto':
            try:
                src = detect(text)
            except LangDetectException:
                src = 'en'
        translator = GoogleTranslator(source=src, target=dest)
        return translator.translate(text)
    except Exception as e:
        return f"Помилка перекладу: {e}"


def LangDetect(text, set='all'):
    try:
        lang = detect(text)
        if set == 'lang':
            return lang
        elif set == 'confidence':
            # langdetect не надає показник довіри напряму
            return "N/A"
        else:
            return f"Мова: {lang}"
    except LangDetectException as e:
        return f"Помилка визначення мови: {e}"



def CodeLang(lang):
    from googletrans import LANGUAGES
    try:
        if lang in LANGUAGES:
            return lang
        elif lang in LANGUAGES.values():
            return [k for k, v in LANGUAGES.items() if v == lang][0]
        else:
            return "Мова не знайдена"
    except Exception as e:
        return f"Помилка: {e}"


def LanguageList(out='screen', text=None):

    from googletrans import LANGUAGES
    try:

        if out == 'screen':
            print("N Language ISO-639 code Text")
            for i, (lang_code, lang_name) in enumerate(LANGUAGES.items(), 1):  # Використовуємо LANGUAGES з googletrans
                translated_text = TransLate(text, dest=lang_code) if text else ""
                print(f"{i} {lang_name} {lang_code} {translated_text}")

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"