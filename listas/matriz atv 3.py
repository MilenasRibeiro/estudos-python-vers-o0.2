arr = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

arr_sum = [];
sum = 0

for row in range(0,7):
  arr_sum.append([])
  for col in range(0,8):
    arr[row][col] = int(input(f'Digite um valor para [{row}, {col}]: '))
    sum += arr[row][col]
    arr_sum[row].append(sum)

print(arr_sum)