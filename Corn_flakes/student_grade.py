scores = []
student_scores = []


def display_class_summary(scores, num_subjects):
    print("=========================================================================================================")

    print(f"CLASS SUMMARY - {num_subjects} SUBJECTS")
    print("=========================================================================================================")
    print("STUDENT\t\t", end="")

    for sub in range(1, num_subjects + 1):
        print(f"SUB{sub}\t", end="")

        print("TOT\t\tAVE\t\tPOS")
        print(
            "=========================================================================================================")

    sorted_scores = sorted([(sum(student), i) for i, student in enumerate(scores)], reverse=True)
    sorted_positions = {student[1]: pos for pos, student in enumerate(sorted_scores, start=1)}

    for i in range(len(scores)):
        total = sum(scores[i])
        average = total / num_subjects
        pos = sorted_positions[i]
        print(f"Student {i + 1}", end="\t")
    for score in scores[i]:
        print(f"{score}\t\t", end="")
        print(f"{total}\t\t{average:.2f}\t\t{pos}")
        print(
            "=========================================================================================================")


def display_subject_summary(scores):
    print("SUBJECT SUMMARY")

    for j in range(len(scores[0])):
        highest = -1
        lowest = 101
        total = 0
        passes = 0
        failures = 0
        highest_student = -1
        lowest_student = -1

    for i in range(len(scores)):
        score = scores[i][j]
        total += score

    if score >= 50:
        passes += 1
    else:
        failures += 1

    if score > highest:
        highest = score
    highest_student = i

    if score < lowest:
        lowest = score
    lowest_student = i

    average = total / len(scores)

    print(f"Subject {j + 1}")
    print(f"Highest scoring student is: Student {highest_student + 1} scoring {highest}")
    print(f"Lowest scoring student is: Student {lowest_student + 1} scoring {lowest}")
    print(f"Total score is: {total}")
    print(f"Average score is: {average:.2f}")
    print(f"Number of passes: {passes}")
    print(f"Number of failures: {failures}\n")


def display_hardest_and_easiest_subjects(scores):
    hardest_subject = -1

    easiest_subject = -1
    min_failures = len(scores) + 1
    max_passes = -1

    for j in range(len(scores[0])):
        failures = 0
    passes = 0

    for i in range(len(scores)):
        score = scores[i][j]

    if score < 50:
        failures += 1
    else:
        passes += 1

    if failures < min_failures:
        hardest_subject = j
    min_failures = failures

    if passes > max_passes:
        easiest_subject = j
    max_passes = passes

    print(f"The hardest subject is Subject {hardest_subject + 1} with {min_failures} failures")
    print(f"The easiest subject is Subject {easiest_subject + 1} with {max_passes} passes")


def print_subjects(num_subjects):
    for i in range(1, num_subjects + 1):
        print(f"Subject {i}")


def display_overall_scores(scores):
    best_student = -1

    worst_student = -1
    max_total = -1
    min_total = len(scores[0]) * 101
    total_scores = 0

    for i in range(len(scores)):
        total = sum(scores[i])
    total_scores += total

    if total > max_total:
        best_student = i
    max_total = total

    if total < min_total:
        worst_student = i
    min_total = total

    print("CLASS SUMMARY")
    print(f"Best Graduating Student is: Student {best_student + 1} scoring {max_total}")
    print(f"Worst Graduating Student is: Student {worst_student + 1} scoring {min_total}")
    print("**************************************************************************************")

    class_average = total_scores / (len(scores) * len(scores[0]))
    print("==========================================")
    print(f"Class total score is: {total_scores}")
    print(f"Class average score is: {class_average:.2f}")
    print("==========================================")


def main():
    global scores
    global student_scores
    num_students = int(input("How many students do you have? "))

    num_subjects = int(input("How many subjects do they offer? "))
    print("saving>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Saved Successfully")

    for counter in range(num_students):
        print(f"Entering scores for Student {counter + 1}")

    for count in range(num_subjects):
        score = int(input(f"Enter score for subject {count + 1}: "))
    student_scores.append(score)
    scores.append(student_scores)

    display_class_summary(scores, num_subjects)
    display_subject_summary(scores)
    display_hardest_and_easiest_subjects(scores)
    display_overall_scores(scores)


if __name__ == "__main__":
    main()
