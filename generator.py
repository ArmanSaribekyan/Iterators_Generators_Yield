import hashlib

def hash_generator(self):
    with open(self, "rb") as f:
        content = f.readlines()
        for line in content:
            my_hash = hashlib.md5(line)
            yield my_hash.hexdigest()

if __name__ == '__main__':
    generator = hash_generator('country_links.txt')
    for hash in generator:
        print(hash)