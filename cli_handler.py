import generator

while True:
    generator.generate(input("Number of usernames to generate"))

    a = input("Generate more ? (y/n)")
    if a.lower() != "y":
        break
    print("\n")
