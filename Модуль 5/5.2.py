import json


class Model:
    atr1 = 'abc'
    atr2 = 'def'
    asdf = [1, 2, 3]

    def save(self):
        res = {i: getattr(self, i) for i in list(filter(lambda x: not x.startswith('_') and x != 'save', dir(self)))}
        with open('saving.json', 'w') as file:
            json.dump(res, file)
        return res


a = Model()
a.save()
