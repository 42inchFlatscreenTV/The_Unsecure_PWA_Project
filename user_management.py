import sqlite3 as sql
import time
import random


def insertUser(username, password, DoB):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username == ? AND password == ?", (username))
    con.commit()
    con.close()


def retrieveUsers(username, password):
    con = sql.connect("database_files/database.db")
    cur = con.cursor()
    # This statement is looking up where the password matches only

    cur.execute(
        "SELECT * FROM users WHERE username == ? AND password == ?",
        (username, password),
    )
    # THIS LINE IS VULNERABLE
    if cur.fetchone() == None:
        con.close()
        return False
    else:
        # cur.execute(
        # "SELECT * FROM users WHERE username == ? AND password == ?",
        # (username, password),)  # THIS LINE IS VULNERABLE

        # Plain text log of visitor count as requested by Unsecure PWA management
        with open("visitor_log.txt", "r") as file:
            number = int(file.read().strip())
            number += 1

        with open("visitor_log.txt", "w") as file:
            file.write(str(number))
        # Simulate response time of heavy app for testing purposes
        time.sleep(random.randint(80, 90) / 1000)
        # if cur.fetchone() == None:
        # con.close()
        # return False
        # else:
        con.close()
        return True


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
