with open("yazkora.txt", "r") as f:
    with open("answer.txt", "w")as answ:
        text = f.read().replace("\n", " ")
        propositions = text.split(".")
        for proposition in propositions:
            words = proposition.split(" ")
            adjectives = str()
            for word in words:
                if word[-2:] == "yo":
                    adjectives += word + " "
            answ.write(adjectives + "\n")
