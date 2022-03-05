# -----------------------------------------------STAGE 1-----------------------------------------------
# marks = list(map(lambda x: int(input()), range(3)))
# print(sum(marks) / len(marks))
# print("Congratulations, you are accepted!")

# -----------------------------------------------STAGE 2-----------------------------------------------
marks = list(map(lambda x: int(input()), range(3)))
mean_score = sum(marks) / len(marks)
print(mean_score)
print("Congratulations, you are accepted!") if mean_score >= 60 else print(
    "We regret to inform you that we will not be able to offer you admission.")
