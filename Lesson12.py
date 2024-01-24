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
        self.__city_population = city_population
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
        print(f"Name: {self.__name} ")
        print(f"Region: {self.__region}")
        print(f"Country: {self.__country}")
        print(f"City population: {self.__city_population}")
        print(f"Postal code: {self.__postal_code}")
        print(f"Phone code: {self.__phone_code}")

Odesa = City("Odesa", "Odesa City", "Ukraine", 1010000, 65000, 380)
Odesa.show_info()

# Завдання 2:
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте доступ до окремих полів (Інкапсуляція).

class Country:
    __name_country: str = "no name"
    __continent: str = "no continent"
    __population: int = 0
    __phone_code: int = 0
    __capital: str = "no capital"
    __cities: str = "no cities"
    def __init__(self, name_country, continent, population, phone_code, capital, cities):
        self.__name_country = name_country
        self.__continent = continent
        self.__population = population
        self.__phone_code = phone_code
        self.__capital = capital
        self.__cities = cities

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
    def show_info(self):
        print(f"Name: {self.__name_country} ")
        print(f"Сontinent: {self.__continent}")
        print(f"Population: {self.__population}")
        print(f"Phone_code: {self.__phone_code}")
        print(f"Capital: {self.__capital}")
        print(f"Cities: {self.__cities}")

Ukraine = Country("Ukraine", "Eurasia", 37419084, 380, Kyiv, Odesa)
# https://www.worldometers.info/world-population/ukraine-population/
Ukraine.show_info()