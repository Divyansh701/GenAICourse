print("Grade Checker")
Score = int(input("Enter your Score:\n"))
if Score >= 90:
    print("A")
elif Score >= 80:
    print("B")
elif Score >= 70:
    print("C")
elif Score >= 60:
    print("D")
else:
    print("F")

Dic = {"Ram": "A", "Shyam": "B", "Hari": "C", "Sita": "D", "Gita": "F"}
Dic["Ramesh"] = "B"
Dic["Gita"] = "A"
print(Dic)
Grades = {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}
if Grades[Dic["Ram"]] > Grades[Dic["Shyam"]]:
    print("Ram has a higher grade than Shyam.")
elif Grades[Dic["Ram"]] < Grades[Dic["Shyam"]]:
    print("Shyam has a higher grade than Ram.")