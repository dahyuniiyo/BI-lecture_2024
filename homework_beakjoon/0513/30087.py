N = int(input())

for i in range(N):

    seminar = str(input())

    if seminar == "Algorithm":
        print("204")

    elif seminar == "DataAnalysis":
        print("207")

    elif seminar == "ArtificialIntelligence":
        print("302")

    elif seminar == "CyberSecurity":
        print("B101")

    elif seminar == "Network":
        print("303")

    elif seminar == "Startup":
        print("501")

    elif seminar == "TestStrategy":
        print("105")


"""
# 딕셔너리 사용
N = int(input())

data = {
    "Algorithm": "204",
    "DataAnalysis": "207",
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": "501",
    "TestStrategy": "105",
}

for i in range(N):
    s = input()
    print(data[s])
"""
