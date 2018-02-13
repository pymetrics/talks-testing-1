class Animal:
    def __init__(self, name=None, sound=None):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f'The {self.name} says "{self.sound}"'
