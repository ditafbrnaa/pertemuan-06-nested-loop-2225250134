# Peran loop luar: mengontrol nilai i (1..3)
# Peran loop dalam: mengontrol nilai j (1..4)
count = 0
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1
print(f"Banyak pasangan = {count}")
