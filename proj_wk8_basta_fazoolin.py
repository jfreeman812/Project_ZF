class menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The {name} menu is available from {start_time} untill {end_time}.".format(name=self.name,
                                                                                          start_time=self.start_time,
                                                                                          end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        self.purchased_items = purchased_items
        price = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                price += self.items[purchased_item]
        return price


brunch = menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00,'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 15, 18)

dinner = menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, 17, 23)

kids = menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 19)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        self.time = time
        menus_available = []
        for menu in self.menus:
            if time in range(menu.start_time, menu.end_time):
                menus_available.append(menu.name)
        return menus_available

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

print(flagship_store)
print(new_installment)

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return self.name

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

take_a_arepa = Business("Take a' Arepa", arepas_place)

print(take_a_arepa)
print(first_business)    
