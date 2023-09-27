import os

# Read the contents of the file
with open('names_eng.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Split the text by numbers and remove empty or whitespace-only lines
lines = text.split('\n')
company_names = [lines[i].strip() for i in range(len(lines)) if i % 4 == 1]

# Capitalize each word in the company names
capitalized_company_names = [name.title() for name in company_names]

# Save the capitalized company names to a new text file
with open('capitalized_names_eng.txt', 'w', encoding='utf-8') as output_file:
    for name in capitalized_company_names:
        output_file.write(name + '\n')

