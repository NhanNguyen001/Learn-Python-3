class Text(str):
    def duplicate(self):
        return self + self

# text = Text('Python')
# print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print('Append called()')
        super().append(object)


list = TrackableList()
print(list)
list.append('1')
print(list)
