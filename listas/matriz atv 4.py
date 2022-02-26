arr = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0], [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

arr_sum = [];

for row in range(0, 7):
  arr_sum.append([])
  for col in range(0,8):
    arr[row] = int(input(
        'Digite um valor para [{row}}]: '))
    arr[col] = int(input(
        'Digite um valor para [{col}]: '))
    soma = arr[row][col]
    arr_sum[row].append(sum)

print(arr_sum)