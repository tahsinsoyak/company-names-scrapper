from googletrans import Translator

# Function to read university names from a file and translate them to Turkish
def translate_universities(file_path):
    translator = Translator()
    with open(file_path, 'r', encoding='utf-8') as file:
        universities = file.readlines()

    translated_universities = []
    for university in universities:
        translation = translator.translate(university.strip(), src='auto', dest='tr')
        translated_universities.append(translation.text)

    return translated_universities

# Input file path
file_path = 'data/university-names-eng.txt'

# Translate and print the university names in Turkish
translated_universities = translate_universities(file_path)
for i, university in enumerate(translated_universities, start=1):
    print(f"{i}. {university.strip()}")

# Optionally, you can save the translated universities to a new file
with open('translated_universities.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(translated_universities)
