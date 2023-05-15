student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}
grade=""
#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:

    score=student_scores[student]

    if score>90 and score<=100:
        student_grades[student]="Outstanding"
    if score>80 and score<=90:
        student_grades[student]="Exceeds Expectations"
    if score>70 and score<=80:
        student_grades[student]="Acceptable"
    if score<=70:
        student_grades[student]="Fail"
 
print(student_grades)