import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    cursor = db.cursor()

    cursor.execute("SELECT * from studio")

    all_studio = cursor.fetchall()

    print("***Displaying Studio Records***")

    for all in all_studio:
        print("Studio ID: {}\nStudio Name: {}\n".format(all[0], all[1]))

    cursor.execute("SELECT * from genre")

    all_genre = cursor.fetchall()

    print("***Displaying Genre Records***")

    for all in all_genre:
        print("Genre ID: {}\nGenre Name: {}\n".format(all[0], all[1]))

    cursor.execute("SELECT film_name,film_runtime from film WHERE film_runtime < 120 ")

    runtime = cursor.fetchall()

    print("***Displaying Film Runtime Records***")

    for run in runtime:
        print("Film Name: {}\nFilm Runtime: {}\n".format(run[0], run[1]))

    cursor.execute("SELECT film_name, film_director from film ORDER BY film_director")

    director_order = cursor.fetchall()

    print("***Displaying Director Records in Order***")

    for order in director_order:
        print("Film Name: {}\nDirector Name: {}\n".format(order[0], order[1]))
