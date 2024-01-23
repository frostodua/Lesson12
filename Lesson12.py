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
    def region(self):
        return self.__region
    def country(self):
        return self.__country
    def city_population(self):
        return self.__city_population
    def postal_code(self):
        return self.__postal_code
    def phone_code(self):
        return self.__phone_code

    @city_population.setter
    def city_population(self, city_population):
        if 0 < city_population:
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



