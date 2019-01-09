batteri = 50
with open("forbruk", "r") as fil:
    for rad in fil:
        batteri -= float(rad[:-1])
        print(batteri, " kw/t")