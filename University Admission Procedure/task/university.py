# -----------------------------------------------STAGE 1-----------------------------------------------
# marks = list(map(lambda x: int(input()), range(3)))
# print(sum(marks) / len(marks))
# print("Congratulations, you are accepted!")

# -----------------------------------------------STAGE 2-----------------------------------------------
# marks = list(map(lambda x: int(input()), range(3)))
# mean_score = sum(marks) / len(marks)
# print(mean_score)
# print("Congratulations, you are accepted!") if mean_score >= 60 else print(
#     "We regret to inform you that we will not be able to offer you admission.")

# -----------------------------------------------STAGE 3-----------------------------------------------
NUM_APPLICANTS = int(input())
NUM_PLACES = int(input())

applicants = list(map(lambda x: input().split(), range(NUM_APPLICANTS)))
applicants = list(map(lambda x: [x[0], x[1], float(x[2])], applicants))
applicants.sort(key=lambda x: (-x[2], x[0], x[1]))

applicants_output = [f"{x[0]} {x[1]}" for x in applicants[0:NUM_PLACES]]
print("Successful applicants:")
output_str = '\n'.join(applicants_output)
print(output_str)
