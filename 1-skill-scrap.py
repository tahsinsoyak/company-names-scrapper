


with open("skill2vec_50K.txt", "r") as file:
    lines = file.readlines()



with open("cleaned_skills.txt", "w") as output_file:
    for line in lines:
        # Split each line by commas to separate skills
        skills = line.strip().split(',')
        
        # Iterate through the skills and write them to the output file
        for skill in skills[1:]:  # Skip the first element (job code)
            skill = skill.strip()  # Remove leading/trailing whitespace
            if skill:
                output_file.write(skill + "\n")



# Read the extracted skills from the file
with open("cleaned_skills.txt", "r") as file:
    extracted_skills = file.read().splitlines()

# Remove duplicates and normalize the skills
normalized_skills = set()  # Using a set to automatically remove duplicates

for skill in extracted_skills:
    # Capitalize the skill
    skill = skill.strip().capitalize()
    
    # Replace underscores with spaces (if needed)
    skill = skill.replace("_", " ")
    
    # Add the normalized skill to the set
    normalized_skills.add(skill)

# Convert the set of normalized skills back to a list
normalized_skills_list = list(normalized_skills)

# Sort the list alphabetically
normalized_skills_list.sort()

# Write the cleaned and normalized skills to a new text file
with open("cleaned_normalized_skills.txt", "w") as output_file:
    for skill in normalized_skills_list:
        output_file.write(skill + "\n")
