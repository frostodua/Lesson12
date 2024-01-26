# Завдання 1:
# Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону,
# назву країни, кількість жителів міста, поштовий індекс міста, телефонний код міста.
# Реалізуйте доступ до окремих полів (Інкапсуляція).
#
# Завдання 2:
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте доступ до окремих полів (Інкапсуляція).

# Завдання 1:
# Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону,
# назву країни, кількість жителів міста, поштовий індекс міста, телефонний код міста.
# Реалізуйте доступ до окремих полів (Інкапсуляція).

class City:
    __name: str = "no name"
    __region: str = "no region"
    __country: str = "no country"
    __city_population: int = 0
    __postal_code: int = 0
    __phone_code: int = 0
    def __init__(self, name, region, country, city_population, postal_code, phone_code):
        self.__name = name
        self.__region = region
        self.__country = country
        self.city_population = city_population
        self.__postal_code = postal_code
        self.__phone_code = phone_code

    @property
    def name(self):
        return self.__name

    @property
    def region(self):
        return self.__region

    @property
    def country(self):
        return self.__country

    @property
    def city_population(self):
        return self.__city_population

    @property
    def postal_code(self):
        return self.__postal_code

    @property
    def phone_code(self):
        return self.__phone_code

    @city_population.setter
    def city_population(self, city_population):
        if city_population > 0:
            self.__city_population = city_population
        else:
            print("Incorrect number!")
    def show_info(self):
        print(f"Name: {self.__name}\nRegion: {self.__region}\nCountry: {self.__country}\nCity population: {self.__city_population}\nPostal code: {self.__postal_code}\nPhone code: {self.__phone_code} ")

Odesa = City("Odesa", "Odesa City", "Ukraine", 1010000, 65000, 380)
Odesa.show_info()
print()

# Завдання 2:
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте доступ до окремих полів (Інкапсуляція).

class Country:
    __name_country = "no name"
    __continent = "no continent"
    __population = 0
    __phone_code = 0
    __capital = "no capital"
    __cities = list()

    def __init__(self, name_country: str, continent: str, population: int, phone_code: int, capital: str, cities: list[City] = None):
        self.__name_country = name_country
        self.__continent = continent
        self.population = population
        self.__phone_code = phone_code
        self.__capital = capital
        self.cities = cities

    @property
    def name_country(self):
        return self.__name_country

    @property
    def continent(self):
        return self.__continent

    @property
    def population(self):
        return self.__population

    @property
    def phone_code(self):
        return self.__phone_code

    @property
    def capital(self):
        return self.__capital

    @property
    def cities(self):
        return self.__cities

    @population.setter
    def population(self, population):
        if population > 0:
            self.__population = population
        else:
            print("Incorrect number!")

    @cities.setter
    def cities(self, cities):
        if cities is not None:
            self.__cities = cities
        else:
            print("Incorrect data!")

    def show_info(self):
        print(f"Name: {self.__name_country}\nСontinent: {self.__continent}\nPopulation: {self.__population}\nPhone_code: {self.__phone_code}\nCapital: {self.__capital}")
        print("Cities:")
        for city in self.__cities:
            city.show_info()



Kyiv = City("Kyiv", "Kyiv city", "Ukraine", 2884000, 1000, 380)
Odesa = City("Odesa", "Odesa city", "Ukraine", 1010000, 65009, 380)

cities = [Kyiv, Odesa]
Ukraine = Country("Ukraine", "Eurasia", 37419084, 380, "Kyiv", cities)
Ukraine.show_info()