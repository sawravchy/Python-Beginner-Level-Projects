import re
print("A simple online email extractor by python")
print()
text = input("Please enter your text here:")
while text in [""," "]:
  text = input("\nText field is empty please enter your text here:")
else:
  pattern = re.compile("[a-zA-Z0-9\.\_\-]+[@]+[a-zA-Z0-9]+\.[a-zA-Z]+")
  result =pattern.findall(text)
if result == []:
  print("Sorry we didn't find any email in your text.")
else:  
  print(f"\nList Of Email Address: {result}")
