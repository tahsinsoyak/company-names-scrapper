from googletrans import Translator

# Function to translate a text from Turkish to English
def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='tr', dest='en')
    return translation.text

# Input and output file paths
input_file_path = 'data/job-names-tr.txt'
output_file_path = 'translated_output_file.txt'

# Open the input and output files
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            turkish_name = line.strip()
            english_name = translate_to_english(turkish_name)
            output_file.write(english_name + '\n')

print("Translation complete. The translated names are saved in 'translated_output_file.txt'.")
