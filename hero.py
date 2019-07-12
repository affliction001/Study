class Hero:
    """Class to create Hero for our Game"""
    def __init__(self, name, level, race):
        """Initiate out Hero"""
        self.__name = name
        self.__level = level
        self.__race = race
        self.__health = 100

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_race(self):
        return self.__race

    def get_health(self):
        return self.__health

    def show_hero(self):
        """Print all parameter of Hero"""
        description = (self.get_name() +
                       '\n\tLevel is: ' + str(self.get_level()) +
                       '\n\tRace is: ' + self.get_race() +
                       '\n\tHealth is: ' + str(self.get_health())).title()
        print(description)

    def level_up(self):
        """Upgrade level of Hero"""
        self.__level += 1
        print("Hero " + str(self.get_level()) + " is level up.")

    def move(self):
        """Start moving Hero"""
        print('Hero ' + self.get_name() + ' start moving.')

    def set_health(self, hp):
        new_health = self.get_health() + hp
        if (new_health <= 0):
            self.__health = "DEAD"
        elif (new_health >= 150):
            self.__health = 150
        else:
            self.__health = new_health
