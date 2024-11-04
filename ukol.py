import math

# Lokalita
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient


# Nemovitosti
class Property:
    def __init__(self, locality):
        self.locality = locality


# Pozemek
class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        # Definice koeficientů pro jednotlivé typy pozemků
        estate_type_coefficients = {
            "land": 0.85,
            "building site": 9,
            "forrest": 0.35,
            "garden": 2
        }
        # Výpočet daně
        tax = self.area * estate_type_coefficients[self.estate_type] * self.locality.locality_coefficient
        return math.ceil(tax)


# Residence
class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        # Výpočet základní daně pro obytné nemovitosti
        tax = self.area * self.locality.locality_coefficient * 15
        # Pokud je nemovitost komerční, daň se násobí dvěma
        if self.commercial:
            tax *= 2
        return math.ceil(tax)

# Daňového přiznání (Bonus)
class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []

    def add_property(self, property):
        #Přidá nemovitost do seznamu property_list
        self.property_list.append(property)

    def calculate_tax(self):
        #Vypočítá celkovou daň ze všech nemovitostí v seznamu property_list
        total_tax = sum(property.calculate_tax() for property in self.property_list)
        return total_tax


manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)
land_estate = Estate(locality=manetin, estate_type="land", area=900)
house_residence = Residence(locality=manetin, area=120)
office_residence = Residence(locality=brno, area=90, commercial=True)

# Vytvoření daňového přiznání
tax_report = TaxReport("Jan Novák")
tax_report.add_property(land_estate)
tax_report.add_property(house_residence)
tax_report.add_property(office_residence)

print(f"Daň za zemědělský pozemek: {land_estate.calculate_tax()}")
print(f"Daň za dům: {house_residence.calculate_tax()}")
print(f"Daň za kancelář: {office_residence.calculate_tax()}")

# Výpočet celkové daně
total_tax = tax_report.calculate_tax()
print(f"Celková daň pro {tax_report.name}: {total_tax}")