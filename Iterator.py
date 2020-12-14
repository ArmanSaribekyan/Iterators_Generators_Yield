import json
from pprint import pprint

class Iterator:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        with open("countries.json", encoding="utf-8") as f:
            json_data = json.load(f)
            return (json_data[self.start - 1]['name']['common'].replace(' ', '_'))



if __name__ == '__main__':
    wiki = 'https://en.wikipedia.org/wiki/'
    with open('countries.json', encoding='utf8') as f:
        json_data = json.load(f)
    countries = Iterator(1, (len(json_data) + 1))
    with open('country_links.txt', 'a', encoding='utf8') as result_file:
        for country in countries:
            result_file.write(f'{country} - {wiki}{country}\n')
