#!/usr/bin/python

import sqlite3
import json


def create():
    conn = sqlite3.connect('room_res.db')
    curr = conn.cursor()

    # Creating the Rooms table
    curr.execute("""CREATE TABLE Rooms (
                    room_id TEXT PRIMARY KEY NOT NULL,
                    min_ppl INT DEFAULT 1,
                    max_ppl INT DEFAULT 1,
                    monitor BOOL
                    );
                """)

    # Creating the Students Table
    curr.execute("""CREATE TABLE Students (
                    student_id TEXT PRIMARY KEY NOT NULL,
                    first TEXT NOT NULL,
                    last TEXT NOT NULL,
                    email TEXT NOT NULL
                    );
                """)

    # Creating the Reservations table
    curr.execute("""CREATE TABLE Reservations (
                    res_id TEXT PRIMARY KEY NOT NULL,
                    room_id TEXT NOT NULL,
                    student_id TEXT NOT NULL,
                    res_date DATE,
                    start_time TIME,
                    end_time TIME,
                    FOREIGN KEY (res_id) REFERENCES Students (res_id),
                    FOREIGN KEY (room_id) REFERENCES Rooms (room_id),
                    FOREIGN KEY (student_id) REFERENCES Students(student_id)
                    );
                """)

    conn.commit()
    conn.close()

def populate_rooms(file):
    # Populating Rooms table
    conn = sqlite3.connect('room_res.db')
    curr = conn.cursor()
    with open(file, "r") as f:
        rooms = json.load(f)
        for room in rooms:
            min_cap = rooms[room]["min_cap"]
            max_cap = rooms[room]["max_cap"]
            monitor = rooms[room]["monitor"]
            sql = '''INSERT INTO Rooms(room_id,min_ppl,max_ppl, monitor)
                     VALUES(?,?,?,?);'''
            curr.execute(sql, (room, min_cap, max_cap, monitor))
    conn.commit()
    conn.close()

def main():
  create()
  populate_rooms("rooms.json")


if __name__ == "__main__":
  main()
