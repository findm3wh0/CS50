# Ask user to give his/her name
''' userName = input("What is your Name? ") '''

# or

userName = input("What is your Name? ").strip().title()

# Input filter spaces
#--- Type 1

''' userName = userName.strip()
userName = userName.title() '''

#--- Type 2
userName = userName.strip().title()

# Output greeting with username
# Method - 1
print("Method - 1")
print("Hello,",userName)
# Method - 2
print("Method - 2")
print("Hello, " + userName)
# Method - 3
print("Method - 3")
print(f"Hello, {userName}")