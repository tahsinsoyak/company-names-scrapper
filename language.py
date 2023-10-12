import pandas as pd
from translate import Translator

# Read CSV into a DataFrame
df = pd.read_csv('languages.csv')

# Create a translator
translator = Translator(to_lang='tr')  # Specify the target language as 'tr' for Turkish

# Create a list to store lines for the text file
lines = []

for index, row in df.iterrows():
    # Translate the "name" (name_en) to Turkish
    name_tr = translator.translate(row['name'])

    # Format the line
    line = f"{row['name']}, {name_tr}, {row['nativeName']}, {row['639-1']}, {row['639-2']}"
    lines.append(line)

# Write lines to a text file
with open('languages.txt', 'w', encoding='utf-8') as text_file:
    text_file.write('\n'.join(lines))

print("Data has been saved to 'languages.txt'")
