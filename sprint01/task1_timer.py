total = int(input("Ведите количество секунд: "))
chasi = total // 3600
minuti = (chasi % 3600) // 60
seky = total % 60
print(f"{chasi:02d}:{minuti:02d}:{seky:02d}")









