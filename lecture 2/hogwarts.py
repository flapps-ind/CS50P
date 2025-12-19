students = ["Hermione", "Harry", "Ron"]

for student in students:
  print(student)

for i in range(len(students)):
  print(students[i])

students1 = {
  "Hermione": "Gryffindor",
  "Harry": "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin",
}


for student in students:
  print(students1[student])



print(students1["Hermione"])


students2 = [
  {"name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
  {"name":"Draco", "House": "Slytherin", "Patronus": None}
]

for student in students2:
  print(student["name"], student["Patronus"], sep=", ")