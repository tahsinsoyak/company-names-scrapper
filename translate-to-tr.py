from googletrans import Translator, exceptions

# Function to translate a text from English to Turkish
def translate_to_turkish(text):
    translator = Translator()
    try:
        translation = translator.translate(text, src='en', dest='tr')
        return translation.text
    except exceptions.TranslatorError as e:
        print(f"Translation error: {e}")
        return None

# Input and output file paths
input_file_path = 'data/university-names-eng.txt'  # Replace with your input file path
output_file_path = 'translated_to_turkish_output.txt'

# Open the input and output files
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            english_name = line.strip()
            turkish_name = translate_to_turkish(english_name)
            if turkish_name is not None:
                output_file.write(turkish_name + '\n')

print("Translation complete. The translated names are saved in 'translated_to_turkish_output.txt'.")
