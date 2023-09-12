def compute_average_score():
    print("**************************************************************************************")
    print("Aso Rock Secondary School, Abuja Nigeria")
    print("**************************************************************************************")

    class_name = input("Class: ")
    num_students = 0
    total_score = 0

    while True:
        score = float(input("Enter score for Student {}: ".format(num_students + 1)))

        if score < 0:
            break

        total_score += score
        num_students += 1

    if num_students > 0:
        average_score = total_score / num_students

        print("**************************************************************************************")
        print("Class:", class_name)
        print("Number of Students in class:", num_students)
        print("Total Score:", total_score)
        print("Average Score:", average_score)
        print("**************************************************************************************")
    else:
        print("No scores entered. Exiting...")
        print("**************************************************************************************")


compute_average_score()
