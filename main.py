from controller.impl.student_controller_impl import StudentControllerImpl

if __name__ == '__main__':
    print("1 - search by average mark\n"
          "2 - search by number of group\n"
          "3 - search by mark and subject\n"
          "4 - delete by average mark\n"
          "5 - delete by number of group\n"
          "6 - delete by mark and subject")

    choice = int(input())

    student_controller = StudentControllerImpl()

    if choice == 1:
        print("type the average mark ")
        avg_mark = int(input())
        print(student_controller.find_student_by_average_mark(avg_mark))
    elif choice == 2:
        print("type group number ")
        group_number = input()
        print(student_controller.find_student_by_group(group_number))
    elif choice == 3:
        print("type mark ")
        mark = int(input())
        print("type subject ")
        subject = input()
        print(student_controller.find_student_by_mark_and_subject(mark, subject))
    elif choice == 4:
        print("type the average mark ")
        avg_mark = int(input())
        print(student_controller.delete_student_by_average_mark(avg_mark))
    elif choice == 5:
        print("type mark ")
        mark = int(input())
        print("type subject ")
        subject = input()
        print(student_controller.delete_student_by_mark_and_subject(mark, subject))
    elif choice == 6:
        print("type group number ")
        group_number = input()
        print(student_controller.delete_student_by_group(group_number))
