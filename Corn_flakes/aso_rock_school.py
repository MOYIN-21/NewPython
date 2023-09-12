print("**************************************************************************************")
print("Aso Rock Secondary School, Abuja Nigeria")
print("**************************************************************************************")

class_name = "SSS 3"
num_students = 20

total_score = 0
for i in range(num_students):
    while True:
        try:
            score = int(input("Enter score for Student {} (out of 100): ".format(i+1)))
            if 0 <= score <= 100:
                break
            else:
                print("Invalid score! Score should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    total_score += score

average_score = total_score / num_students

print("**************************************************************************************")
print("Class:", class_name)
print("Number of Students in class:", num_students)
print("Total score:", total_score)
print("Average Score: {:.2f}".format(average_score))
print("**************************************************************************************")
