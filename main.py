botning_tanlovi = ["tosh", "qaychi", "qog'oz"]
botning_tanlovi = random.choice(botning_tanlovi)
for i in range(1, 3):
    soz = input("Chin gan chuk boshshlandi!")
    if soz == "qaychi":
        if botning_tanlovi == "tosh":
            print("Siz yutdingiz!")
        elif botning_tanlovi == botning_tanlovi[2]:
            print("Siz yutdingiz")
        else:
            print("Durang")
    elif soz == "tosh":
        if botning_tanlovi == botning_tanlovi[2]:
            print("Durang")
        elif botning_tanlovi == botning_tanlovi[2]:
            print("Men yutdim!")
        else:
            print("Siz yutdingiz!")
    elif soz == botning_tanlovi[2]:
        if botning_tanlovi == botning_tanlovi[2]:
            print("DUrang")
        elif botning_tanlovi == botning_tanlovi[1]:
            print("Men yutdim!")
        else:
            print("Siz yutdingiz!")
    else:
        print("Man tushunmadim")