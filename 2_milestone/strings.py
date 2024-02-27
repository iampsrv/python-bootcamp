# name = "Pranjal"
# age = 26
# # message = "My name is {} and I'm {} years old.".format(name, age)
# message = f"My name is {name} and I'm {age} years old."
# print(message)

# text = "Hello, World!"
# new_text = text.replace("World", "Python")
# print(new_text)

# text = "My name is Pranjal Srivastava. I am devops engineer"
# words = text.split(" ")
# print(words)

text = "P7y8t9h6o4n"
digits = ''.join(filter(str.isdigit, text))
letters = ''.join(filter(str.isalpha, text))
print(digits) # Output: "78964"
print(letters)