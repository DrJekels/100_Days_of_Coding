#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
with open(r"Input/Letters/starting_letter.txt", "r") as file:
    letter = file.readlines()

for name in names:
    with open(rf"Output/ReadyToSend/{name.strip()}.txt", "w") as file:
        for line in letter:
            if line.strip() == "Dear [name],":
                file.write(line.replace("[name],", name).strip() + ",\n")
            else:
                file.write(line.strip() + "\n")