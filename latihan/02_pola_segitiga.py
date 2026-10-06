# Peran loop luar: mengontrol jumlah baris (1..n)
# Peran loop dalam: mencetak simbol '*' sebanyak nilai i
n = int(input("n: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()