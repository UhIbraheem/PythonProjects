#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter = open("input/letters/starting_letter.txt", "r")
names = open("input/names/invited_names.txt", "r")
letter = letter.read()
for name in names:
    f = open(f"output/ReadyToSend/letter_for_{name}.txt", "w")
    new_letter = letter.replace("[name]", f"{name},")
    f.write(new_letter)
    f.close()

names.close()
print(letter)
