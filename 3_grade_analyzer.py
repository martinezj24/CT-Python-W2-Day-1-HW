#Task 1: Code a function to calculate the average grade

def average_grades(grades):
    if not grades:
        return 0
    total = sum(grades)
    average = total / len(grades)
    return average

grades = [85, 90, 50, 65, 99, 88]
class_grades = average_grades(grades)
print('Average grade: ', class_grades)

#Task 2: Implement a function to find the highest and lowest grade.

def find_high_and_low_grades(grades):
    if not grades:
        return '', ''  # When list is empty function will return empty string
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade

highest, lowest = find_high_and_low_grades(grades)
print('Highest grade: ', highest)
print('Lowest grade: ', lowest)
