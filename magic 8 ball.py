import random

print("I Am The Magic 8 Ball")

while True:
    question = input("ask a question: ")

    if question == "stop":
        print("done")
        break

    answers = ["yes", "no", "maybe", "100 percent", "I dont know", "possibly"]
    
    print(random.choice(answers))
    
