import sqlite3 as sql
import time
import random
import bcrypt


def insertUser(username, hash, DoB, salt):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO users (username,password,dateOfBirth,salt) VALUES (?,?,?,?)",
        (username, hash, DoB, salt),
    )
    con.commit()
    con.close()


def retrieveUsers(username, password):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    # This statement is looking up where the password matches only

    cur.execute(
        "SELECT password FROM users WHERE username == ?",
        (username,),
    )

    if cur.fetchone() == None:
        con.close()
        return False
    else:
        hashed_password = cur.fetchone()[0]
        check_hash = bcrypt.checkpw(password.encode(), hashed_password)
        con.close()

        if check_hash:
            with open("visitor_log.txt", "r") as file:
                number = int(file.read().strip())
                number += 1

            with open("visitor_log.txt", "w") as file:
                file.write(str(number))

            return True

        return False


def insertFeedback(feedback):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO feedback (feedback) VALUES ('{feedback}')"
    )  # THIS LINE IS VULNERABLE
    con.commit()
    con.close()


def listFeedback():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM feedback").fetchall()
    con.close()
    f = open("templates/partials/success_feedback.html", "w")
    for row in data:
        f.write("<p>\n")
        f.write(f"{row[1]}\n")
        f.write("</p>\n")
    f.close()
