Blo = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

def get_all_canfies_of_under_10(students):
    total_candies = 0
    for student in students:
        if student['age'] < 10 :
            total_candies += student ['candies']
    return total_candies

print(get_all_canfies_of_under_10(Blo))
