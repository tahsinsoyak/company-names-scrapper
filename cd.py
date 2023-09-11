import datetime

# Read the content of the input file
with open('data/job-names-tr.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time as needed
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Initialize an empty list to store the modified lines
modified_lines = []

# Iterate through the lines and add the formatted date and time
for line in lines:
    modified_lines.append(f'{formatted_datetime},{formatted_datetime},{line.strip()}')

# Join the modified lines into a single string
result = '\n'.join(modified_lines)

# Print the result
print(result)

# Optionally, you can write the result to a new file
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(result)
