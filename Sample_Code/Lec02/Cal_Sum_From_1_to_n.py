n = int(input("Nhập 1 số nguyên dương n: "))

sum = 0
for i in range(1, n+1):
    sum += i
print("Tổng các số từ 1 đến", n, "là", sum)