import sqlite3
from pprint import pprint as pp


def connect_sql():
    """Подключаемся к базе данных"""
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        return cursor


def get_movie_by_title(name: str):
    """Получаем информацию по названию, сортируя и выводя самый свежий"""
    cursor = connect_sql()
    query = '''SELECT title, country, release_year, listed_in, description
    FROM netflix
    WHERE title = ?
    ORDER BY release_year DESC
    LIMIT 1
        '''
    cursor.execute(query, (name,))
    executed_query = cursor.fetchall()
    result = executed_query
    return {
        "title": result[0][0],
        "country": result[0][1],
        "release_year": result[0][2],
        "genre": result[0][3],
        "description": result[0][4]
    }


def release_diapason(year_from: int, year_before: int):
    """Поиск произведений в заданном промежутке"""
    list_film = []
    cursor = connect_sql()
    query = '''SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN ? AND ?
        ORDER BY release_year DESC
        LIMIT 100
            '''
    cursor.execute(query, (year_from, year_before))
    executed_query = cursor.fetchall()
    results = executed_query
    for result in results:
        list_film.append({"title": result[0],
                          "release_year": result[1]
                          })
    return list_film


def return_list_title_for_rating(category: str):
    """Подбираем произведения согласно заданной категории: детские, для семейного просмотра, фильмы для взрослых :)"""
    cursor = connect_sql()
    rating_film = []
    query = '''SELECT title, rating, description
            FROM netflix
            WHERE rating = ? OR rating = ? OR rating = ?
            '''
    if category.lower() == 'children':
        rating = ('G', ' ', ' ')
    elif category.lower() == 'family':
        rating = ('G', 'PG', 'PG-13')
    elif category.lower() == 'adult':
        rating = ('R', 'NC-17', ' ')
    else:
        return 'Данной категории не существует'
    cursor.execute(query, rating)
    executed_query = cursor.fetchall()
    results = executed_query
    for result in results:
        rating_film.append({
                            "title": result[0],
                            "rating": result[1],
                            "description": result[2]
                            })
    return rating_film


def return_genre(genre):
    """Подбор по жанру"""
    list_genre = []
    cursor = connect_sql()
    query = f'''SELECT title, description
                FROM netflix
                WHERE "type" = \'Movie\' AND listed_in LIKE "%{genre}%"
                ORDER BY release_year DESC
                LIMIT 10
                             '''
    cursor.execute(query, )
    executed_query = cursor.fetchall()
    results = executed_query
    for result in results:
        list_genre.append({
                        "title": result[0],
                        "description": result[1],
                        })
    return list_genre


#pp(return_genre('dramas'))
