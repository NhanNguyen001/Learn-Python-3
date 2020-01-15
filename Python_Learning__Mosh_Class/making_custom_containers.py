class TagCloud:
    def __init__(self):
        self.tags = {}

    # We encapsulating the complexity around the case-sensitivity of tag
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)
        # iterator object is an object that walks on the container and get one item at the time


cloud = TagCloud()
cloud["python"] = 10
print(cloud.tags)
print(len(cloud))
cloud.add("python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)
