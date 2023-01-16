

matrix1 = []

# matrix1
for i in range(2):
    row = []
    for j in range(2):
        Element = int(input('enter element:'))
        row.append(Element)
    matrix1.append(row)
print(matrix1)

for i in range(2):
    for j in range(2):
        matrix1[i][j]=matrix1[j][i] + matrix1[i][j]


for k in matrix1:
    print(k)
print()


