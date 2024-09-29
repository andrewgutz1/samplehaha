Temp=[10,-11,-12,13,-15,-14]

names=["jake", "sam","luke","mark"]

for bugok in Temp:
    if bugok > 0:
        print(str(bugok) + "-positve")
    elif bugok < 0:
        print(str(bugok) +"-negative")

for mga in names:
    if mga == "jake":
        print("present")
    else:
        print("none")    