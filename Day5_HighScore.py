"""
You are going to write a program that calculates the highest score from a List of scores.
Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
"""
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

l=len(student_scores)
maximum=0
student_scores.sort()
maximum=student_scores[l-1]

print(f"The highest score in the class is: {maximum}")
