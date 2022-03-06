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
# NUM_APPLICANTS = int(input())
# NUM_PLACES = int(input())
#
# applicants = list(map(lambda x: input().split(), range(NUM_APPLICANTS)))
# applicants = list(map(lambda x: [x[0], x[1], float(x[2])], applicants))
# applicants.sort(key=lambda x: (-x[2], x[0], x[1]))
#
# applicants_output = [f"{x[0]} {x[1]}" for x in applicants[0:NUM_PLACES]]
# print("Successful applicants:")
# output_str = '\n'.join(applicants_output)
# print(output_str)

# -----------------------------------------------STAGE 4-----------------------------------------------
# DEPARTMENTS_LIST = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
# departments_enrollment = {i: [] for i in DEPARTMENTS_LIST}
#
# with open('applicants.txt', 'r', encoding='utf-8') as reader:
#     applicants_str = reader.read()
# all_applicants_list = applicants_str.split('\n')
# all_applicants_list = list(map(lambda x: x.split(), all_applicants_list))
# all_applicants_list = list(map(lambda x: [x[0], x[1], float(x[2]), x[3], x[4], x[5]], all_applicants_list))
# all_applicants_dict = {(i[0], i[1], i[2]): [i[3], i[4], i[5]] for i in all_applicants_list}
#
# N = int(input())
#
# for i in range(3):
#     applicants = {}
#     for department in departments_enrollment.keys():
#         applicants[department] = [x for x, y in all_applicants_dict.items() if y[i] == department]
#         applicants[department].sort(key=lambda x: (-x[2], x[0], x[1]))
#         applicants_can_accept = N - len(departments_enrollment[department])
#         if applicants_can_accept > 0:
#             applicants_to_accept_list = applicants[department][0:applicants_can_accept]
#             departments_enrollment[department].extend(applicants_to_accept_list)
#             for applicant in applicants_to_accept_list:
#                 all_applicants_dict.__delitem__(applicant)
#
# for department, students in departments_enrollment.items():
#     print(department)
#     students.sort(key=lambda x: (-x[2], x[0], x[1]))
#     for student in students:
#         print(*student)
#     print()

# -----------------------------------------------STAGE 5-----------------------------------------------
DEPARTMENTS_LIST = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
departments_enrollment = {i: [] for i in DEPARTMENTS_LIST}
DEPARTMENTS_EXAMS = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}

with open('applicants.txt', 'r', encoding='utf-8') as reader:
    applicants_str = reader.read()
all_applicants_list = applicants_str.split('\n')
all_applicants_list = list(map(lambda x: x.split(), all_applicants_list))
all_applicants_list = list(map(lambda x: [x[0], x[1], float(x[2]), float(x[3]), float(x[4]), float(x[5]), x[6], x[7], x[8]],
                               all_applicants_list))
all_applicants_dict = {(i[0], i[1], i[2], i[3], i[4], i[5]): [i[6], i[7], i[8]] for i in all_applicants_list}

N = int(input())

for i in range(3):
    applicants = {}
    for department in departments_enrollment.keys():
        applicants[department] = [x for x, y in all_applicants_dict.items() if y[i] == department]
        applicants[department].sort(key=lambda x: (-x[DEPARTMENTS_EXAMS[department]], x[0], x[1]))
        applicants_can_accept = N - len(departments_enrollment[department])
        if applicants_can_accept > 0:
            applicants_to_accept_list = applicants[department][0:applicants_can_accept]
            applicants_to_accept_list_short = list(map(lambda x: (x[0], x[1], x[DEPARTMENTS_EXAMS[department]]),
                                                       applicants_to_accept_list))
            departments_enrollment[department].extend(applicants_to_accept_list_short)
            for applicant in applicants_to_accept_list:
                all_applicants_dict.__delitem__(applicant)

for department, students in departments_enrollment.items():
    print(department)
    students.sort(key=lambda x: (-x[2], x[0], x[1]))
    for student in students:
        print(*student)
    print()