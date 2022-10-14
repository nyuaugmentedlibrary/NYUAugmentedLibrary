import sqlite3
from create_db import *


def addStudent(student_id, first, last, email):
    """
    addStudents handles the functionality for adding students to the "Students" table of the database.
    Args:
        student_id: String -> Student's NYU netID (ex. aqe123)
        first: String -> Student's first name
        last: String -> Student's last name
        email: String -> Student's email
    Returns:
        None
    """
    with sqlite3.connect('room_res.db') as conn:
        curr = conn.cursor()
        curr.execute(f"SELECT COUNT(*) FROM Students WHERE student_id={student_id}")
        count = curr.fetchall()
        if count == 0:
            try:
                curr.execute("""INSERT INTO Students(student_id, first, last, email) 
                             VALUES (?, ?, ?, ?);""", (student_id, first, last, email)
                             )
                conn.commit()
            except:
                print("addStudent -> Invalid command, check parameters.")


def addReservation(res_id, room_id, student_id, res_date, start_time, end_time):
    """
    Adds record of reservation to Reservations table
    Args:
        res_id: String ->
        room_id:
        student_id:
        res_date:
        start_time:
        end_time:
    Returns:
    """
    with sqlite3.connect('room_res.db') as conn:
        curr = conn.cursor()
        try:
            curr.execute("""INSERT INTO Reservations (res_id, room_id, student_id, res_date, start_time, end_time) "
                        VALUES (?,?,?,?,?,?);""", (res_id, room_id, student_id, res_date, start_time, end_time)
                         )
            conn.commit()
        except:
            print("addReservation -> Invalid command, check parameters.")

def cancelReservation(student_id):
    """
    Handles removal of reservation from Reservations table for the given student, indicated by their netID.
    NOTE: We do not remove them from the Students table, we can keep it for future reference or change this later if we decide to.
    """
    with sqlite3.connect('room_res.db') as conn:
        curr = conn.cursor()
        try:
            curr.execute("DELETE FROM Reservations WHERE student_id = %s", (student_id))
            conn.commit()
        except:
            print("cancelReservation -> Invalid command, check parameters.")

def deleteExpiredReservations():
    """
    Query the database and delete all reservations that have passed the date
    """
    with sqlite3.connect('room_res.db') as conn:
        curr = conn.cursor()
        try:
            curr.execute("DELETE FROM Reservations WHERE res_date < GETDATE()")
            conn.commit()
        except:
            print("deleteExpiredReservation -> Command failed.")

def returnAllReservations(date):
    """
    Returns all reservations for a given date, used by the front-end to indicate room availiabilities.
    :param date -> Formatted in "YYYY-MM-DD" for the date.
    """
    with sqlite3.connect('room_res.db') as conn:
        curr = conn.cursor()
        try:
            return curr.execute(f"SELECT * FROM Reservations WHERE res_date = {date}")
        except:
            print("returnAllReservations -> Invalid command, check parameters.")


def modifyExistingReservation(table, field, oldValue, newValue):
    """
    Handles all modifications necessary for database tables.  Examples of it's use can be to allow a user to modify their reservation
    time or the room they want to reserve.
    :param table -> Specifies the table we want to modify.
    :param field -> Specifies the field that we want to modify.
    :param oldValue -> Specifies the existing value in the field.
    :param newValue -> Specifies the new value we want to set in the field.
    """
    with sqlite3.connect('room_res.db') as conn:
        curr = conn.cursor()
        try:
            curr.execute("UPDATE {} SET {} = %s WHERE {} = %s".format(table, field, field), (newValue, oldValue))
            conn.commit()
        except:
            print("modifyExistingReservation -> Invalid command, check parameters.")


def printTables(label="None"):
    # Print Tables #
    # If you inserted into the tables correctly, the below code should print it out in list form.
    # Call this functions when you want to test.
    # Pass an optional label to make it easier to identify.
    with sqlite3.connect('room_res.db') as conn:
        curr = conn.cursor()
        print("==========================================")
        print("Current: " + label)
        print("Rooms Table:")
        print(curr.execute("SELECT * FROM Rooms;").fetchall())
        print("Reservations Table:")
        print(curr.execute("SELECT * FROM Reservations;").fetchall())
        print("Students Table:")
        print(curr.execute("SELECT * FROM Students;").fetchall())


def main():
    """
  This main function should be used for testing only.  We can assume that for the tests that the data will be given to us from the front-end.
  """
    studentOne = ("abc123", "Bob", "xyz987", "Test", "abc123@nyu.edu")
    studentOneRes = ("xyz987", "B445", "abc123", "2022-03-31", "07:00:00", "07:30:00")

    # ==================================================================================================================#
    #                                                 START OF TEST CODE                                                #
    # ==================================================================================================================#

    # V {Comment out if already inserted to prevent errors.} V #
    # Sample insertion for rooms table, this will be done later for each room.

    # V {Comment out if already inserted to prevent errors.} V #

    addReservation("bb001", "Bob", "TheBuilder", "Test", "abc123@nyu.edu")

    # ^ {Comment out if already inserted to prevent errors.} ^ #

    printTables("Completed Reservation")

    # ==================================================================================================================#
    #                                                 END OF TEST CODE                                                  #
    # ==================================================================================================================#


if __name__ == "__main__":
    main()
