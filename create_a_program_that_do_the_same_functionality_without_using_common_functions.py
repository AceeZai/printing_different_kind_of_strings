#rstrip()
user_text = input("Enter text: ")
last_index = len(user_text) - 1
#Use while loop
while last_index >= 0 and user_text[last_index] == " ":
    last_index -= 1
#identify the variables and within the given index 
trimmed_text = user_text[:last_index + 1]
print(trimmed_text)
#done

#removesuffix()
user_text = input("Enter text: ")
suffix_text = input("Enter suffix: ")
#Use len() function
suffix_len = len(suffix_text)
#if else loop
if user_text[-suffix_len:] == suffix_text:
    result_text = user_text[:-suffix_len]
else:
    result_text = user_text

print(result_text)
#done

#upper()
user_text = input("Enter text: ")
upper_text = ""
#ascii code stores value or digits for every character
for char_item in user_text:
    ascii_code = ord(char_item)
#Use True or False for executing 
    if 97 <= ascii_code <= 122:
        upper_text += chr(ascii_code - 32)
    else:
        upper_text += char_item

print(upper_text)
#done

#lower()
user_text = input("Enter text: ")
all_lower = True
#Use ascii 
for char_item in user_text:
    ascii_code = ord(char_item) #Checks corresponding digits
#False loop
    if 65 <= ascii_code <= 90:
        all_lower = False
#done 

#startswith()
#rjust

#count
user_text = input("Enter text: ")
search_char = input("Enter character: ")

char_total = 0
#Set condition
for char_item in user_text:
    if char_item == search_char:
        char_total += 1
