import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define a function to filter and select reasonable skills
def filter_reasonable_skills(skill_list):
    reasonable_skills = set()
    
    for skill in skill_list:
        # Tokenize the skill using spaCy
        doc = nlp(skill.lower())  # Convert to lowercase for better matching
        
        # Filter for nouns and non-stopwords
        nouns = [token.text for token in doc if token.pos_ == "NOUN" and not token.is_stop]
        
        # Check if there are valid nouns in the skill
        if nouns:
            reasonable_skills.add(skill.strip())
    
    return reasonable_skills

# Input: List of skills as a list of lines (already obtained from reading a file)
with open("cleaned_normalized_skills.txt", "r") as file:
    input_skills = file.readlines()

# Filter and select reasonable skills
reasonable_skills = filter_reasonable_skills(input_skills)

# Define the output file path
output_file_path = "filtered_skills.txt"

# Save the reasonable skills to the output file
with open(output_file_path, "w") as output_file:
    for skill in reasonable_skills:
        output_file.write(skill.strip() + "\n")  # Strip any leading/trailing whitespace

print(f"Filtered skills have been saved to {output_file_path}")
