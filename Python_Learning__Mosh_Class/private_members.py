
# In python unlike C# and Java we don't really have the concept of private member
class TagCloud:
    def __init__(self):
        self.__tags = {}

    # We encapsulating the complexity around the case-sensitivity of tag
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)
        # iterator object is an object that walks on the container and get one item at the time


cloud = TagCloud()
# print(cloud.__dict__)
# print(cloud._TagCloud__tags)


cloud.__tags
# cloud.add("python")
# cloud.add("Python")
# cloud.add("Python")
# print(cloud.__tags["PYTHON"])
