# определение класса Car, который представляет информацию о машине
class Car:
    # инициализация экземпляра класса с его атрибутами
    def __init__(self, id, name, manufacturer, is_petrol, tank_volume):
        self.id = id  # уникальный идентификатор машины
        self.name = name  # название модели машины
        self.manufacturer = manufacturer  # производитель машины
        self.is_petrol = is_petrol  # логическое значение, указывающее, является ли машина бензиновой
        self.tank_volume = tank_volume  # объем топливного бака в литрах
        
# создание записей о машинах Toyota Camry
car1 = Car(1, "Toyota Camry", "Toyota", True, 60)  # первая запись о Toyota Camry
car2 = Car(2, "Toyota Camry", "Toyota", True, 65)  # вторая запись о Toyota Camry с другим объемом бака
car3 = Car(3, "Toyota Camry", "Toyota", False, 55)  # третья запись о Toyota Camry с альтернативным топливом

# вывод информации о машинах Toyota Camry
print("Car 1:")
print(f"ID: {car1.id}")  # вывод уникального идентификатора первой машины
print(f"Name: {car1.name}")  # вывод названия первой машины
print(f"Manufacturer: {car1.manufacturer}")  # вывод производителя первой машины
print(f"Is Petrol: {car1.is_petrol}")  # вывод информации о типе топлива первой машины
print(f"Tank Volume: {car1.tank_volume} liters\n")  # вывод объема бака первой машины

print("Car 2:")
print(f"ID: {car2.id}")  # вывод уникального идентификатора второй машины
print(f"Name: {car2.name}")  # вывод названия второй машины
print(f"Manufacturer: {car2.manufacturer}")  # вывод производителя второй машины
print(f"Is Petrol: {car2.is_petrol}")  # вывод информации о типе топлива второй машины
print(f"Tank Volume: {car2.tank_volume} liters\n")  # вывод объема бака второй машины

print("Car 3:")
print(f"ID: {car3.id}")  # вывод уникального идентификатора третьей машины
print(f"Name: {car3.name}")  # вывод названия третьей машины
print(f"Manufacturer: {car3.manufacturer}")  # вывод производителя третьей машины
print(f"Is Petrol: {car3.is_petrol}")  # вывод информации о типе топлива третьей машины
print(f"Tank Volume: {car3.tank_volume} liters\n")  # вывод объема бака третьей машины
