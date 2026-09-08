import mysql.connector
from datetime import date

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hanuman&@3036",
    database="college_attendence"
)

cursor = db.cursor()


def mark_attendance():

    student_id = int(input("Enter Student ID: "))
    subject_id = int(input("Enter Subject ID: "))
    period = int(input("Enter Period (1-6): "))

    status = input("Enter attendance (P/A): ").upper()

    if status == "P":
        status = "Present"
    elif status == "A":
        status = "Absent"
    else:
        print("Invalid attendance!")
        return

    today = date.today()

    sql = """
    INSERT INTO attendance
    (student_id, subject_iD, attendance_date, period, status)
    VALUES ( %s, %s, %s, %s, %s)
    """

    values = (
        student_id,
        subject_id,
        today,
        period,
        status
    )

    try:
        cursor.execute(sql, values)
        db.commit()
        print("Attendance marked successfully!")

    except mysql.connector.Error as error:
        print("Error:", error)


def view_attendance():

    student_id = int(input("Enter Student ID: "))

    sql = """
    SELECT
        attendance.attendance_date,
        attendance.period,
        subjects.subject_name,
        attendance.status
    FROM attendance
    JOIN subjects
    ON attendance.subject_id = subjects.subject_id
    WHERE attendance.student_id = %s
    ORDER BY attendance.attendance_date, attendance.period
    """

    cursor.execute(sql, (student_id,))

    records = cursor.fetchall()

    print("\nAttendance Report")
    print("-" * 60)

    for record in records:
        print(record)


def attendance_percentage():

    student_id = int(input("Enter Student ID: "))

    sql = """
    SELECT
        COUNT(*) AS total_classes,
        SUM(status = 'Present') AS present_classes
    FROM attendance
    WHERE student_id = %s
    """

    cursor.execute(sql, (student_id,))

    result = cursor.fetchone()

    total = result[0]
    present = result[1] or 0

    if total == 0:
        print("No attendance records found.")
        return

    percentage = (present / total) * 100

    print("Total Classes :", total)
    print("Present       :", present)
    print("Attendance    :", round(percentage, 2), "%")


while True:

    print("\n===== COLLEGE ATTENDANCE SYSTEM =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Attendance Percentage")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()

    elif choice == "2":
        view_attendance()

    elif choice == "3":
        attendance_percentage()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

cursor.close()
db.close()