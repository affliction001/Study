from hero import Hero


class SuperHero(Hero):
    """ Class to create SuperHero """
    def __init__(self, name, level, race, magic_level):
        """ Initiate our SuperHero """
        super().__init__(name, level, race)
        self.__magic_level = magic_level
        self.__mana = 100

    def get_magic_level(self):
        return self.__magic_level

    def get_mana(self):
        return self.__mana

    def set_mana(self, mp):
        value = self.get_mana() + mp
        if (value <= 0):
            self.__mana = 0
        elif (value >= 100):
            self.__mana = 100
        else:
            self.__mana = value

    def show_hero(self):
        """Print all parameter of Hero"""
        description = (self.get_name() +
                       '\n\tLevel is: ' + str(self.get_level()) +
                       '\n\tRace is: ' + self.get_race() +
                       '\n\tHealth is: ' + str(self.get_health()) +
                       '\n\tMagic level is: ' + self.get_magic_level() +
                       '\n\tMana is: ' + str(self.get_mana())).title()
        print(description)
