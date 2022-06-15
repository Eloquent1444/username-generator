import random

with open("names.txt", "r") as file:
    names = file.read().split("\n")
with open("surnames.txt", "r") as file:
    surnames = file.read().split("\n")
with open("words.txt", "r") as file:
    random_words = file.read().split("\n")


def generate(amount):
    randomUsernameList = []
    try:
        for i in range(int(amount)):
            assets = [""]
            assets.append(str(random.randint(1, 1000)))
            assets.append(random.choice(names))
            assets.append(random.choice(surnames))
            assets.append(random.choice(random_words))

            random.shuffle(assets)
            username = ""
            for j in assets:
                if random.randint(0, 2):
                    username += j
            if username:
                randomUsernameList.append(username)
        for i in randomUsernameList:
            print(i)

    except ValueError as ve:
        print("Not a number")