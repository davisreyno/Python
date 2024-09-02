PLACEHOLDER = "[name]"

# readlines() - returns a list containg each line in the file as a list item 
with open("./Input/invited_names.txt") as names_file:
    names = names.file.readlines()
    print(names)

with open("./Input/starting_letter.docx/") as letter_file:
    letter_contents = letter_file.read()
    # Go through starting_letter.docx and replace PLACEHOLDER with actual names in invited_names.txt 
    # strip() - removes spaces at beginning and at the end of the string 
    for name in names: 
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # Creates this new docs in designated folder which can be viewd/printed later  
        with open(f"./Output/Ready-to-Send/letter_for_{stripped_name}.docx") as completed_letter:
            completed_letter.write(new_letter)