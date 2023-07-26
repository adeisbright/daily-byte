'''
https://docs.google.com/document/d/1FGWzPFE8R8IEQMIb38fqv8eZr7RusO0qIWxBuAsMiAw/edit
'''


class my_enumerate(object):
    def __init__(self, iterable_item, index=0):
        self.iterable_item = iterable_item
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable_item):
            # Raise an Error since the index is out of bound 
            raise StopIteration
        current_index = self.index
        current_value = self.iterable_item[self.index]
        self.index += 1
        return current_index, current_value


for i, value in my_enumerate(['first', 'second', 'third']):
    print('{}. {}'.format(i+1, value))
