#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# running main from different folder
# https://docs.replit.com/programming-ide/configuring-repl

with open("mail-merge-project/input/names/invited_names.txt", mode="r") as data:
  list_names = data.readline()

with open("mail-merge-project/input/letters/starting_letter.txt", mode="r") as words:
  letter = words.read()
  
  for name in list_names:
    new_letter = letter.replace("[name]", name)
    with open(f"mail-merge-project/output/ready_to_send/{name}.txt", mode="w") as new_words:
      new_words.write(new_letter)


  
