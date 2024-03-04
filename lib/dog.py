class Dog():
    def __init__(self, name, breed=None):
        self.name = name
        if breed is None:
           self.breed = "Mutt"
        else:
            self.breed = breed



