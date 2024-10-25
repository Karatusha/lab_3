from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text, src='auto', dest='en'):
    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(text, set='all'):
    try:
        detection = translator.detect(text)
        if set == 'lang':
            return detection.lang
        elif set == 'confidence':
            return detection.confidence
        else:
            return f"Мова: {detection.lang}, Довіра: {detection.confidence}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

def CodeLang(lang):
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
    try:
        if out == 'screen':
            print("N Language ISO-639 code Text")
            for i, (lang_code, lang_name) in enumerate(LANGUAGES.items(), 1):
                translated_text = TransLate(text, dest=lang_code) if text else ""
                print(f"{i} {lang_name} {lang_code} {translated_text}")

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"