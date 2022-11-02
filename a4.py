#!/user/bin/python
import psycopg2
import getpass
from configparser import ConfigParser

def connect():
    conn = None
    passwordarg = getpass.getpass()
    try:
        params = config()
        params.update({"password": passwordarg})
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        b = True

        while(b):
            displayMenu()
            inp = int(input())
            if inp == 1:
                cur.execute(open("a4.q1", "r").read())
                highestPaid = cur.fetchall()
                print("Highest paid player in the NBA")
                for entry in highestPaid:
                    print("Name:", entry[0])
                    print("Salary:", entry[1])
            elif inp == 2:
                cur.execute(open("a4.q2", "r").read())
                entries = cur.fetchall()
                print("Players who played for the 76ers for more than 5 years")
                for entry in entries:
                    print("Name:", entry[0])
                    print("Years:", entry[1])
            elif inp == 3:
                cur.execute(open("a4.q3", "r").read())
                entries = cur.fetchall()
                print("Players with a career over 20 years in the NBA: ")
                for entry in entries:
                    print("Name:", entry[0])
                    print("Years Played:", entry[1])
                    print("First Season:", entry[2])
            elif inp == 0:
                b=False
            else:
                print("Incorrect input")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')


def config(filename='a4.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    dbCreds = {}

    if (parser.has_section(section)):
        params = parser.items(section)
        for param in params:
            dbCreds[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in the {1} file".format(section, filename))
    
    return dbCreds

def displayMenu():
    print("Each number below executes a different query")
    print("1 - Highest paid player")
    print("2 - Sixers players for more than 5 seasons")
    print("3 - Players with career over 20 years")
    print("0 - Exit")


if __name__ == '__main__':
    connect()