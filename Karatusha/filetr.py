import json
from lab3 import module1, module2
import os

def translate_from_file(config_filepath):
    try:
        with open(config_filepath, 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)

        input_filepath = config["input_file"]
        output_lang = config["output_lang"]
        output_type = config["output_type"]  # "screen" або "file"
        max_chars = config.get("max_chars", float('inf'))
        max_words = config.get("max_words", float('inf'))
        max_sentences = config.get("max_sentences", float('inf'))
        translator_module = config.get("translator", "googletrans")


        if not os.path.exists(input_filepath):
            raise FileNotFoundError(f"Файл {input_filepath} не знайдено.")

        with open(input_filepath, 'r', encoding='utf-8') as input_file:
            text = ""
            char_count = 0
            word_count = 0
            sentence_count = 0

            for line in input_file:
                sentences = line.split('.')  # Розбиваємо на речення
                for sentence in sentences:
                    sentence = sentence.strip() # Видаляємо зайві пробіли
                    if sentence: #перевіряємо, чи речення не пусте
                        words = sentence.split()
                        if char_count + len(sentence) <= max_chars and word_count + len(words) <= max_words and sentence_count < max_sentences:
                            text += sentence + "."  # Додаємо крапку після кожного речення
                            char_count += len(sentence) + 1 # +1 для врахування крапки
                            word_count += len(words)
                            sentence_count += 1
                        else:
                            break  # Зупиняємо, якщо досягнуто ліміту
                if char_count >= max_chars or word_count >= max_words or sentence_count >= max_sentences:
                    break



        # Вибір модуля та переклад
        if translator_module == "deeptr":
            translate_func = module2.TransLate
        else:
            translate_func = module1.TransLate

        translated_text = translate_func(text, dest=output_lang)



        if output_type == "screen":
            print(f"Переклад на {output_lang}:")
            print(translated_text)
        elif output_type == "file":
            output_filename = f"{os.path.splitext(input_filepath)[0]}_{output_lang}.txt"
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(translated_text)
            print(f"Переклад збережено у файл {output_filename}")

        print("Ok")

    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Помилка: {e}")


# Приклад використання
translate_from_file('config.json')