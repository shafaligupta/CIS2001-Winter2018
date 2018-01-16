first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print('Hello ' + first_name + ' ' + last_name + '!')
#anything after this gets ignored by python

#using int will only work with integers, no decimal places
hourly_wage = int(input("How much do you earn per hour?"))

hourly_wage = float(input("How much do you earn per hour?"))
print('You make: ', hourly_wage * 40 , 'per week' )

#() for tuples, [] for lists, {} for dictionaries
students_names = [ 'Mohamed', 'Jenny', 'Allen', 'Christie', 'Shafali' ]

for student in students_names:
    print(student)

for index in range( len(students_names) ):
    print(students_names[index])

students_names.insert(2, "Bob")
students_names.remove('Jenny')
print(students_names)

if 'Eric' in students_names:
    print("Eric is here")
elif 'Jenny' in students_names:
    print("Jenny is here and Eric is not")
else:
    print("Eric and Jenny have left the building")

grades = {
    'Mohamed' : 'A',
    'Jenny' : 'A',
    'Allen' : 'A',
    'Christie' : 'A',
    'Shafali' : 'A'
}

if 'Mohamed' in grades:
    print(grades['Mohamed'])
else:
    print("Not an A student")

sorted_names = sorted(list(grades.keys()))

for student in sorted_names:
    print(student, ' grade: ', grades[student])

for student, grade in grades.items():
    print(student, grade)

favorite_number = int(input("What is your favorite number?"))

if favorite_number == 42:
    print("You have the answer")
else:
    print("go read hitch hikers guide to the galaxy")

print( 5 % 2 )

primes = []

for number in range(2,1000):
    is_prime = True
    divisor = 2
    while is_prime and divisor < number:
        if number % divisor == 0:
            is_prime = False
        divisor += 1
        # divisor = divisor + 1
    if is_prime:
        print(number)
        primes.append(number)

# list/string slicing
print(primes[::-1])

alphabet = 'abcdefghijklmnopqrstuvwsxyz'
print( alphabet[::2])

