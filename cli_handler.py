import generator

while True:
    generator.generate(input("How many usernames should be generated"))

    a = input("Generate more ? (y/n)")
    if a.lower() != "y":
        break
    print("\n")