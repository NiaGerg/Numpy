import numpy as np


def calculate_highest_average_score(students, scores):
    average_scores = np.mean(scores, axis=1)
    highest_average_index = np.argmax(average_scores)
    student_with_highest_average = students[highest_average_index]
    return student_with_highest_average



def math_scores(students, scores, subjects):
    highest_math_score_index = np.argmax(scores[:, subjects.index('Math')])
    lowest_math_score_index = np.argmin(scores[:, subjects.index('Math')])
    student_with_highest_math_score = students[highest_math_score_index]
    student_with_lowest_math_score = students[lowest_math_score_index]
    highest_math_score = scores[highest_math_score_index, subjects.index('Math')]
    lowest_math_score = scores[lowest_math_score_index, subjects.index('Math')]
    return (student_with_highest_math_score, highest_math_score), (student_with_lowest_math_score, lowest_math_score)


def above_average_english(students, scores, subjects):
    english_index = subjects.index('English')
    average_english_score = np.mean(scores[:, english_index])
    students_above_average = []
    for i in range(len(students)):
        if scores[i, english_index] > average_english_score:
            students_above_average.append(students[i])
    return students_above_average
