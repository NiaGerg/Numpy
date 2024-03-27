import numpy as np
from tabulate import tabulate
import random
from operations import calculate_highest_average_score, math_scores, above_average_english
from info import first_names, last_names, subjects

students = [f"{random.choice(first_names)} {random.choice(last_names)}" for i in range(100)]

scores = np.random.randint(0, 101, size=(100, 5))

data = np.column_stack((np.array(students)[:, np.newaxis], scores))
data = np.row_stack(([[''] + subjects], data))

headers = [''] + subjects

print(tabulate(data, headers=headers))

student_with_highest_average = calculate_highest_average_score(students, scores)
highest_math, lowest_math = math_scores(students, scores, subjects)
students_above_average_english = above_average_english(students, scores, subjects)

print(f"\nყველაზე მაღალი საშუალო ქულის მქონე სტუდენტია: {student_with_highest_average}")
print(f"მათემატიკაში ყველაზე მაღალქულიანი სტუდენტია: {highest_math[0]}")
print(f"მათემატიკაში ყველაზე დაბალქულიანი სტუდენტია: {lowest_math[0]}")
print("\nყველა სტუდენტი რომლის ინგლისურის ქულაც მეტია საშუალო ინგლისურის ქულაზე:\n")
for student in students_above_average_english:
    print(student)
