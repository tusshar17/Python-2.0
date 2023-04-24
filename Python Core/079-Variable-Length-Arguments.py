# Variable Length Arguments

def add(*nums):
    sum = 0
    for a in nums:
        sum += a

    print(sum)


add(5, 2, 4, 3)
add(5, 2)


def marks(student, *marks):
    total_marks = 0
    for a in marks:
        total_marks += a
    print(f'Total marks of {student} : {total_marks}')


marks('Rahul', 70, 80, 75)
marks('Raj', 80, 50)
