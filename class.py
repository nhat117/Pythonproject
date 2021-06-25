class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message in inside class")

myobj = MyClass()
print(myobj.variable)
myobj.function()