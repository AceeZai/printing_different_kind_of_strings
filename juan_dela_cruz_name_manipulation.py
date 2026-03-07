#Ask for name with leading spaces. ex; ____ Acee Zai Mendez
full_name = input("Enter your fullname: ")
#Use lstrip.(), this function removes spaces in the beginning of a string
clean_name = full_name.lstrip()
#Print clean_name
print(clean_name)
