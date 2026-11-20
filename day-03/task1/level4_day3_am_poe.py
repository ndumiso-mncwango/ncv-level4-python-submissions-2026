learners = {"Ndumiso": 45,
           "Samkelo": 65,
           "Ntwenhle": 48,
           "Mandisa": 70,
           "Luyanda": 56}

mark_list = [(mark,learner) for learner, mark in learners.items()]

sortList = mark_list[:]

n = len(sortList)
for i in range(n -1):
    for j in range(0, n- i - 1):
        if sortList[j][0] < sortList[j +1][0]:
            sortList[j], sortList[j + 1] = sortList[j + 1], sortList[j]
print("Learner Ranking:")
for rank, (mark, learner) in enumerate(sortList,start = 1):
    print(f"{rank}.{learner} - {mark}%")
