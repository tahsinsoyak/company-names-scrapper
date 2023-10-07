# Open the input file for reading
with open("filtered_skills.txt", "r") as file:
    lines = file.readlines()

# Remove duplicates while preserving order using a set
unique_lines = []
seen = set()

for line in lines:
    # Remove leading/trailing whitespace and convert to lowercase for case-insensitive comparison
    cleaned_line = line.strip().lower()
    
    if cleaned_line not in seen:
        seen.add(cleaned_line)
        unique_lines.append(line)

# Open the output file for writing
with open("output.txt", "w") as output_file:
    output_file.writelines(unique_lines)

print("Duplicate lines removed, and unique lines saved to 'output.txt'.")
