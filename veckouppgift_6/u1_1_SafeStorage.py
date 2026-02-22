""" 
Vad gör följande kod?

 - 1) Creates a class called SafeStorage with a private attribute __data, and two methods: get() to retrieve the value of __data
    , and put(data) to set the value of __data.
 - 2) An instance of SafeStorage is created and assigned to the variable safe.
 - 3) The put method is called on the safe instance with the argument "Anakonda", which sets the __data attribute to "Anakonda".
 - 4) The get method is called on the safe instance, and the value of __data ("Anakonda") is retrieved and assigned to the variable x.
 - 5) The put method is called again on the safe instance with the argument "Boaorm", which updates the __data attribute to "Boaorm".
 - 6) The get method is called again on the safe instance, and the updated value of __data ("Boaorm") is retrieved and assigned to the variable y.
 - 7) Finally, the values of x and y are printed, resulting in the output: "Anakonda Boaorm".
"""
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)
