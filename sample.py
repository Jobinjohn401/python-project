print("Welcome to my quiz!")

playing = input("Shall we start ? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
print("\nTECHNICAL QUESTIONS !!!")
score = 0

answer = input("\nWhat does www stand for? ")
if answer.lower() == "world wide web":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does AI stand for? ")
if answer.lower() == "artificial intelligence":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does ROM stand for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does GUI stand for? ")
if answer.lower() == "graphical user interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

non_tech = input("\nShall we go the nxt part of the quiz? ")

if non_tech.lower() != "yes":
    quit()

print("\nNon-TECHNICAL QUESTIONS !!!")

answer = input("\nWhat is the capital of india? ")
if answer.lower() == "new delhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nWho is the current prime minister of India? ")
if answer.lower() == "narendra modi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat is the national game of india? ")
if answer.lower() == "hockey":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat is the national bird of india? ")
if answer.lower() == "peacock":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("\nIn which continent india is located? ")
if answer.lower() == "asia":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
