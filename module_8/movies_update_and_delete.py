import mysql.connector


def show_films(cursor, title):
    cursor.execute('''SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id''')

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name : {}\n".format(film[0], film[1], film[2], film[3]))


def main():

    db = mysql.connector.connect(
        user="movies_user",
        password="popcorn",
        host="localhost",
        database="movies"
    )

    cursor = db.cursor()

    show_films(cursor, "Displaying Films")

    newFilm = "INSERT INTO film(film_name, film_director, film_releaseDate, film_runtime, studio_id, genre_id) VALUES ('Minions: The Rise of Gru', 'Kyle Balda', '2022', '87', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'), (SELECT genre_id FROM genre WHERE genre_name = 'SciFi') );"

    db.commit()
    cursor.execute(newFilm)
    show_films(cursor, "Displaying Films After Insertion")


    updateFilm = "UPDATE film SET genre_id = (SELECT genre_id from genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien';"

    db.commit()
    cursor.execute(updateFilm)
    show_films(cursor, "Displaying Films After Update- Changed Alien to Horror")


    deleteFilm = "DELETE from film WHERE film_name = 'Gladiator';"

    db.commit()
    cursor.execute(deleteFilm)
    show_films(cursor, "Displaying Films After Deletion")

main()