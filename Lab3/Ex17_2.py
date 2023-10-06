

class Kangaroo:
    def __init__(self):
        self.pouch_content = []

    def put_in_pouch(self, var):
        self.pouch_content.append(var)

    def __str__(self):
        return f'The pouch content is {self.pouch_content} and class {Kangaroo}'


kanga = roo = Kangaroo()

kanga.put_in_pouch('kanga')
kanga.put_in_pouch('roo')

print(str(kanga))
