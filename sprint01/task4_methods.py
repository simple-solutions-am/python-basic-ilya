# 1) strip

ut = "  Бойцовский клуб Python  "
tu = ut.strip()
print(tu)

# 2) upper

ut = "Бойцовский клуб Python"
tu = ut.upper()
print(tu)

# 3) lower

ut = "Бойцовский клуб Python"
tu = ut. lower()
print(tu)

# 4) count

ut = "Бойцовский клуб Python"
tu = ut.count("й")
print(tu)

# 5) split

ut = "Бойцовский клуб Python"
tu = ut.split()
print(tu)

# 6) join

ut = "Бойцовский клуб Python"
tu = ut.split()
su = "-".join(tu)
print(su)

# 7) replace

ut = "Бойцовский клуб Python"
tu = ut.replace("клуб", "club")
print(tu)

# 8) find

ut = "Бойцовский клуб Python"
tu = ut.find("Python")
print(tu)

# 9) startswith

ut = "Бойцовский клуб Python"
tu = "клуб" in ut
print(tu)

# 10) ?

ut = "  Бойцовский клуб Python  "
print(len(ut))
print(len(ut.strip()))






