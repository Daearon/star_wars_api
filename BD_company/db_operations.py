import sqlite3
from utils import *

conn = sqlite3.connect('roskomnadzor_department_Chelyabinsk.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS civil_servants(
   civil_servant_id INT PRIMARY KEY,
   fname TEXT,
   mname TEXT,
   lname TEXT,
   department TEXT,
   position TEXT, 
   telephone_number INT, 
   attorney TEXT, 
   electronic_signature TEXT);
""")
conn.commit()
civil_servants = [
    ("1", "Marina", "Ivanovna", "Olenina", "Outside", "Director", "83512452443", "Doesn't have", "Keep"),
    ("2", "Sergey", "Victorovich", "Simakov", "Outside", "Deputy Director", "83512452440", "Have one", "Keep"),
    ("3", "Marina", "Borisovna", "Gurova", "Media control",
     "Head of department", "83512452438", "Doesn't have", "Keep"),
    ("4", "Marina", "Andreevna", "Popova", "Media control",
     "Leading specialist expert", "83512452434", "Have one", "Keep"),
    ("5", "Mikhail", "Georgievich", "Laptev", "Media control",
     "Specialist of the first category", "83512452433", "Doesn't have", "Keep"),
    ("6", "Natalia", "Andreevna", "Osincova", "Media control",
     "Deputy head of department", "83512452437", "Have one", "Keep"),
    ("7", "Alexandr", "Vladislavovich", "Startsev", "Media control",
     "Specialist expert", "83512452432", "Have one", "Keep"),
    ("8", "Ruslan", "Tagirovich", "Muhamedyarov", "Media control",
     "Specialist expert", "83512452431", "Have one", "Keep"),
    ("9", "Anastasia", "Petrovna", "Mogilevets", "Media control",
     "Specialist of the first category", "83512452430", "Doesn't have", "Doesn't keeping"),
    ("10", "Sergey", "Analolevich", "Nebogatov", "Mail control",
     "Head of department", "83512452420", "Doesn't have", "Keep"),
    ("11", "Margarita", "Ivanovna", "Maile", "Mail control",
     "Leading specialist expert", "83512452421", "Have one", "Keep"),
    ("12", "Sergey", "Alekseevich", "Dvornikov", "Communications control",
     "Head of department", "83512452425", "Doesn't have", "Keep"),
    ("13", "Lidia", "Alexandrovna", "Dejneva", "Communications control",
     "Specialist expert", "83512452424", "Have one", "Keep"),
    ("14", "Irina", "Ivanovna", "Misalova", "Communications control",
     "Head of department", "83512452414", "Have one", "Keep"),
    ("15", "Ksenia", "Ivanovna", "Dvornikova", "Legal department",
     "Specialist expert", "83512452416", "Have one", "Keep"),
    ("16", "Marina", "Alekseevna", "Kern", "Personal data control",
     "Head of department", "83512452404", "Doesn't have", "Keep"),
    ("17", "Artur", "Petrovich", "Karpov", "Personal data control",
     "Leading specialist expert", "83512452406", "Have one", "Keep")
]
cur.executemany("INSERT OR IGNORE INTO civil_servants VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", civil_servants)
conn.commit()


def read_bd():
    user_choice = retrieve_integer("Enter '1' if you want to see information about a specific civil servant "
                                   "or enter '2' if you want to see information about all civil servant in "
                                   "Roskomnadzor's department in Chelyabinsk ")
    match user_choice:
        case 1:
            user_choice_about_specific_civil_servant = retrieve_integer("Enter number, e.g. '11'")
            sql_ask = "SELECT * FROM civil_servants where civil_servant_id = ?;"
            cur.execute(sql_ask, (user_choice_about_specific_civil_servant,))
            one_result = cur.fetchall()
            print(one_result)
        case 2:
            cur.execute("select * from civil_servants;")
            result = cur.fetchall()
            print("id   fname   mname   lname   department   position   telephone_number   attorney   electronic_signature   ");
            for row in result:
                print("%d     %s      %s       %s       %s       %s       %d       %s      %s" %
                      (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        case _:
            print("You entered incorrect number. Try again, please")


def add_in_bd():
    print("In order to add new data to the database, you need to follow the following instructions\n"
          "Enter your data in the following format according to the example: \n"
          "'1', 'Marina', 'Ivanovna', 'Olenina', 'Outside', 'Director', '83512452443', 'Doesn't have', 'Keep'\n"
          "The last two parameters are the presence of a power of attorney and an electronic signature\n")
    user_give_id = retrieve_integer("Enter id number for new civil servant. "
                                    "The current last id can be viewed by calling the database in the start menu. ")
    user_give_fname = input("Enter first name: ")
    user_give_mname = input("Enter middle name: ")
    user_give_lname = input("Enter last name: ")
    user_give_department = input("Enter department: ")
    user_give_position = input("Enter position: ")
    user_give_telephone_number = input("Enter telephone number: ")
    user_give_attorney = input("Enter power of attorney: ")
    user_give_signature = input("Enter electronic signature: ")
    new_civil_servant = tuple((user_give_id, user_give_fname, user_give_mname, user_give_lname, user_give_department,
                               user_give_position, user_give_telephone_number, user_give_attorney, user_give_signature))
    cur.execute("INSERT INTO civil_servants VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", new_civil_servant)
    conn.commit()
    print("All done. Thank you for your effort")


def except_from_bd():
    user_choice = retrieve_integer("Enter the ID of the civil servant you want to dismiss: ")
    sql_delete_query = """DELETE from civil_servants where civil_servant_id = ?"""
    cur.execute(sql_delete_query, (user_choice,))
    conn.commit()
    print("Thank you for your work, now that civil servant become a free man")


def make_update_bd():
    user_choice = retrieve_integer("Enter the ID of the civil servant who needs to issue an power of attorney: ")
    sql_update_query = """UPDATE civil_servants set attorney = "Have one" where civil_servant_id = ?"""
    cur.execute(sql_update_query, (user_choice,))
    conn.commit()
    print("Thank you for your work, now data is updated")