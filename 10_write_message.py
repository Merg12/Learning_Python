file_name = '10_write_message_text.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love Python!")

#be careful, this erases the text file in question and adds in the new text