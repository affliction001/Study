from hero import Hero

hero1 = Hero('Berserk', 5, 'orc')
hero2 = Hero('Alexandros', 10, 'human')

hero1.show_hero()
hero2.move()
hero1.level_up()
hero1.set_health(10)
hero1.show_hero()
hero2.set_health(-200)
hero1.set_health(100)
hero1.show_hero()
hero2.show_hero()