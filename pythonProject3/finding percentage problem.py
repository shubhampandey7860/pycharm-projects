# n = int(input('enter number:'))
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
#
# query_name = input()
#
# if query_name in student_marks:
#     x = ((float(student_marks[query_name][0]) + float(student_marks[query_name][1]) + float(
#         student_marks[query_name][2])) / 3)

# print('%.2f' % x)

for i in range(1,int(input())):
    print((10**i)//9*i)
#


