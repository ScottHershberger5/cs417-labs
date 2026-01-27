# Scott Hershberger
# Class Lab 
# 1/27/26
# CS417

class Weapon:

    def __init__(self, name, damage):

        self.name = name

        self.damage = damage


    def attack_description(self):

        return f"attacks with {self.name} for {self.damage} damage"



class Character:

    def __init__(self, name, special_power):

        self.name = name

        self.special_power = special_power

        self.weapon = None


    def __str__(self):

        return f"I am {self.name}, a {self.__class__.__name__}"


    def equip_weapon(self, weapon):

        self.weapon = weapon


    def attack(self):

        if self.weapon:

            return f"{self.name} {self.weapon.attack_description()}!"

        return f"{self.name} attacks with bare hands for 5 damage!"


    def get_status(self):

        weapon_info = self.weapon.name if self.weapon else "unarmed"

        return f"{self.name} the {self.__class__.__name__} - Weapon: {weapon_info}"


    def summon_power(self):

        raise NotImplementedError("Subclasses must implement summon_power()")



class Warrior(Character):

    def __init__(self, name):

        super().__init__(name, "Berserker Rage")


    def summon_power(self):

        return f"{self.name} unleashes {self.special_power}! Attack power doubled!"



class Mage(Character):

    def __init__(self, name):

        super().__init__(name, "Arcane Blast")


    def summon_power(self):

        return f"{self.name} channels {self.special_power}! Enemies are stunned!"

class Ranger(Character):
    
    def __init__(self,name):
        
        super().__init__(name, "Arrow Storm")

    def summon_power(self):

        return f"{self.name} channels {self.special_power}! Arrows rain down on enemies!"

class Staff(Weapon):

    def __init__(self):
        super().__init__("Staff", 15)

class Hammer(Weapon):

    def __init__(self):
        super().__init__("Hammer", 30)

class Bow(Weapon):

    def __init__(self):
        super().__init__("Bow", 12)


army = [
    Ranger("Scott"),
    Warrior("Doug"),
    Mage("Ted")
]

bow = Bow()
hammer = Hammer()
staff = Staff()

arsenal = [
    bow,
    hammer,
    staff
]

weapon_index = 0

for character in army:
        weapon = arsenal[weapon_index]
        character.equip_weapon(weapon)
        weapon_index += 1
for character in army:
    print(character)
    print(character.get_status())
    print(character.summon_power())

print()
print(army[1].attack())
army[1].equip_weapon(arsenal[2])
print(army[1].attack())

""" the weapons are modeled as has-a composition because with composition, you can easily swap aspects of a class 
such as something like a weapon that every instance of a class has but is not the same for each. It is great for runtime
flexibility. If we used inheretance instead, we would have to initialize a new character everytime we wanted to switch the 
weapon, which is much more time consuming and less efficent. """

