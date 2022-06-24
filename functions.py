from pprint import pprint as pp

from main import connect_sql


def get_casts(name_1: str, name_2: str):
    """
    Возвращаем список актеров, игравших в паре больше 2-х раз
    """
    casts_list = []
    cursor = connect_sql()
    query = f'''SELECT "cast", COUNT (*)
        FROM netflix
        WHERE "cast"  LIKE "%{name_1}%, %{name_2}%" OR "cast" LIKE "%{name_2}%, %{name_1}%"
        GROUP BY "cast"
        HAVING "cast" > 2
            '''
    cursor.execute(query, )
    executed_query = cursor.fetchall()
    results = executed_query
    for result in results:
        casts_list.append({
            "cast": result
        })
    return casts_list


def return_list_for_query(type_: str, year: int, genre: str):
    """Выбираем картину согласно передаваемого запроса по типу, году выпуска и жанру."""
    query_list = []
    cursor = connect_sql()
    query = f'''SELECT "type", release_year, listed_in, description
            FROM netflix
            WHERE "type" LIKE "%{type_}%" AND release_year = {year} AND listed_in LIKE "%{genre}%"
                '''
    cursor.execute(query, )
    executed_query = cursor.fetchall()
    results = executed_query
    for result in results:
        query_list.append({
            "type": result[0],
            "release_year": result[1],
            "listed_in": result[2],
            "description": result[3]
        })
    return query_list


# pp(return_list_for_query('movie', 2021, 'dramas'))
