class BloomFilter:
    def __init__(self, filter_length, data_set):
        self.filter_length = filter_length
        self.data_set = data_set
        self.filter = self.create_filter()

    def calculate_hash(self, number):
        return number % self.filter_length

    def create_filter(self):
        bloom_filter = [False] * self.filter_length
        for data_set_id in self.data_set:
            bloom_filter[self.calculate_hash(data_set_id)] = True
        return bloom_filter

    def is_in_filter(self, number):
        return self.filter[self.calculate_hash(number)]
