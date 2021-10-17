search_string = "Hello World Python"
src_str = input("Enter search string: ")
src_pos = search_string.find(src_str)

if(src_pos != -1):
  print("Search string position in original string: {}".format(src_pos))
else:
  exit()

replace_str = input("Enter string to replace with: ")
new_str = search_string.replace(src_str, replace_str)

print("New string: {}".format(new_str))

