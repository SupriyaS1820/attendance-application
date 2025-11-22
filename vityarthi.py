# Student Attendance Percentage & Eligibility Calculator

def get_int_input(message):
    """Number input safely lene ke liye simple function."""
    while True:
        value = input(message)
        try:
            value = int(value)
            if value < 0:
                print("Value can't be.enter again.")
            else:
                return value
        except ValueError:
            print("Please enter a valid whole number (e.g. 10, 25, 100).")


def main():
    print("========================================")
    print("      STUDENT ATTENDANCE CALCULATOR     ")
    print("========================================")

    total_classes = get_int_input("Total classes conducted: ")
    while total_classes == 0:
        print("Total classes can't be zero atleast one.")
        total_classes = get_int_input("Total classes conducted: ")

    attended_classes = get_int_input("Classes attended: ")
    while attended_classes > total_classes:
        print("Attended classes can't be more than total classes.")
        attended_classes = get_int_input("Classes attended: ")

    print("\nMinimum required attendance normally 75% hoti hai.")
    required_percent = get_int_input("Enter required attendance percentage (e.g. 75): ")

    attendance_percent = (attended_classes / total_classes) * 100

    print("\n------------ RESULT ------------")
    print(f"Total Classes       : {total_classes}")
    print(f"Attended Classes    : {attended_classes}")
    print(f"Attendance Percent  : {attendance_percent:.2f}%")
    print(f"Required Percentage : {required_percent}%")

    if attendance_percent >= required_percent:
        print("\nStatus: ✅ You are ELIGIBLE as per attendance requirement.")
        extra_needed = 0
    else:
        print("\nStatus: ❌ You are NOT ELIGIBLE yet.")

        extra_needed = 0
        curr_attended = attended_classes
        curr_total = total_classes

        while (curr_attended / curr_total) * 100 < required_percent:
            extra_needed += 1
            curr_attended += 1
            curr_total += 1

        print(f"You need to attend at least {extra_needed} more classes consecutively")
        print("to reach the required attendance percentage.")

    print("\n--------------------------------")
    if extra_needed == 0 and attendance_percent >= required_percent:
        print("Good job! you have correct attendance to attend examination.")
    elif extra_needed > 0:
        print("Try your best not to miss the next class")
    print("========================================")


if __name__ == "__main__":
    main()
