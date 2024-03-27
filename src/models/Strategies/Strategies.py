class Strategies:
    def to_csv(self, data, name="default.csv", path='data/'):
        data.to_csv(path + name)