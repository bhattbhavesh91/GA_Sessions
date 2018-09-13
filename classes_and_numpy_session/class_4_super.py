class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value + 10

class Child(Parent):
    def get_value(self):
    	self.value = super(Child,self).get_value()
        return self.value + 1

c = Child()
print (c.get_value())
