totalPrizes=53
numberOfStudents=8

prizesPerStudent = totalPrizes // numberOfStudents
prizesLeftOver = totalPrizes % numberOfStudents

print(f"Each student gets {prizesPerStudent} prizes.")
print(f"Prizes left over: {prizesLeftOver}")
