class animal:
    def speak(self):
     print("animal speaks")
class dog(animal):
     def speak(self):
       print("dog barks")
a=animal()
d=dog()
a.speak()
d.speak()
