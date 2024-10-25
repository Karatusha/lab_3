from lab3 import module1

text_to_translate = "Hello, world!"

# Переклад на українську
ukrainian_translation = module1.TransLate(text_to_translate, dest='uk')
print(f"Український переклад: {ukrainian_translation}")

# Визначення мови
detected_lang = module1.LangDetect(text_to_translate)
print(f"Визначена мова: {detected_lang}")

# Отримання коду мови
lang_code = module1.CodeLang("english")
print(f"Код мови: {lang_code}")

# Список мов та перекладів
module1.LanguageList(text=text_to_translate)

# Збереження перекладів у файл
module1.LanguageList(out='file', text=text_to_translate, filename='gtrans_translations.csv')