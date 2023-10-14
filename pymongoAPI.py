from pymongo import MongoClient


class MyBD:

    def __init__(self):
        client = MongoClient('mongodb', 27017)
        db = client['Incidents_collector']
        self.problems_collection = db['problems']

    def add_data(self, headers, body):
        data = {**headers, **body}
        h = hash(frozenset(data))
        data['hash'] = h
        self.problems_collection.insert_one(data)
        return h

    def get_data_by_hash(self, h):
        return self.get_data({'hash': int(h)})

    def get_data(self, elements: dict):
        results = self.problems_collection.find(elements, {'_id': 0, 'hash': 0})
        return [r for r in results]
