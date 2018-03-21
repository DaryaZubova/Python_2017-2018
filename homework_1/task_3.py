class UniqObject:

    instance = None

    class __UniqObject:
        def __init__(self, name):
            self.name = name

    def __new__(self, name):
        if UniqObject.instance is None:
            UniqObject.instance = UniqObject.__UniqObject(name)
        else:
            UniqObject.instance.name = name

        return UniqObject.instance


a = UniqObject('test1')
print(a)

b = UniqObject('test2')
print(b)

print((a.name, b.name))
