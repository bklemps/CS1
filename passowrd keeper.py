website = []
passwords = []
usernames = []

while True:
    website.append(input("enter a website:"))
    passwords.append(input("enter a password:"))
    usernames.append(input("enter a username:"))
    prompt = input("yes to continue, stop to quit")

    if prompt == "stop":
        break

    print(website)

prompt = input("would you like to print out all your usernames and passwords yes or no")

if prompt == "yes":
    print(website)
    print(usernames)
    print(passwords)

prompt = input(" would you like to accsess the usernames and passwords for a specific website? yes or no?")
if prompt == "yes":
         website = input("what website would you like information for")
for i in range(len(website)):
          if website[1] == website:
              print(usernames[1])
          print(passwords[i])


          
