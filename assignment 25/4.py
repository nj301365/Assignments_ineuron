class Profile:
    platform = "MyApp"  # class variable

    def __init__(self, name, email, age):
        self.name = name
        self.__email = email
        self.__age = age

    @classmethod
    def get_platform(cls):
        return cls.platform

print(Profile.get_platform())  # MyApp
