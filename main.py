

from flask import Flask
from flask import request

from pymongoAPI import MyBD


app = Flask(__name__)
bd = MyBD()


@app.route('/problems', methods=['POST'])
def problems():
    """ Хранение данных -> хеш"""
    return {'hash': bd.add_data(request.headers, request.json)}


@app.route('/find', methods=['POST'])
def find():
    """Поиск по заголовку или body -> данные"""
    return {'data': bd.get_data(request.json)}


@app.route('/find2', methods=['GET'])
def find2():
    """Получаем все записи по hash -> данные"""
    try:
        data = bd.get_data_by_hash(request.args.get('h'))
        return {'data': data}
    except ValueError:
        return {'Error': 'Неправильный тип хэша'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
