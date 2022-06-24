from flask import Flask, jsonify
import main

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


@app.route('/movie/<title>')
# Вывод произведения по его названию
def get_movie(title):
    return main.get_movie_by_title(title)


@app.route('/movie/<int:year_from>/to/<int:year_before>')
# Отображение произведений в заданном диапазоне по дате релиза
def list_of_title_on_year(year_from, year_before):
    return jsonify(main.release_diapason(year_from, year_before))


@app.route('/movie/rating/<rating>')
# Отображение произведений по заданной категории
def get_rating(rating):
    return jsonify(main.return_list_title_for_rating(rating))


@app.route('/movie/genre/<genre>')
# Отображение произведений по жанру
def get_genre(genre):
    return jsonify(main.return_genre(genre))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
