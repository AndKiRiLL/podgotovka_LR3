# 1 

#my_car.go()

# 2 --------------------------------------------------------------------------------------------------------------------
'''
class Book:

    def __init__(self, title, author, name_publisher):
        self.title = title
        self.author = author
        self.name_publisher = name_publisher

    def get_title(self):
        return f'Title: {self.title}'

    def get_author(self):
        return f'Author: {self.author}'

    def get_name_publisher(self):
        return f'Name publisher: {self.name_publisher}'

    def set_title(self, new_title):
        self.title = new_title
        print(f'Установлен новый заголовок: {self.title}')

    def set_author(self, new_author):
        self.author = new_author
        print(f'Установлен новый автор: {self.author}')

    def set_name_publisher(self, new_publicher):
        self.name_publisher = new_publicher
        print(f'Установлен новый издатель: {self.name_publisher}')

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Name_publisher: {self.name_publisher}'

b = Book('Золотая рыбка', 'А. С. Пушкин', 'Москва Сказки')
print(b)

b.set_title('Metro 2033')
b.set_author('Д. А. Глуховский')
b.set_name_publisher('Moscow')

print(b.get_title())
print(b.get_author())
print(b.get_name_publisher())
'''

# 3 --------------------------------------------------------------------------------------------------------------------
'''
class Pet:

    def __init__(self, name='', animal_type='', age=0):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self, new_name):
        self.name = new_name
        print(f'Установлено имя: {self.name}')

    def set_animal_type(self, new_type):
        self.animal_type = new_type
        print(f'Установлен новый тип животного: {self.animal_type}')

    def set_age(self, new_age):
        self.age = new_age
        print(f'Установлен новый возраст: {self.age}')

    def get_name(self):
        return f'Name: {self.name}'

    def get_animal_type(self):
        return f'Animal_Type: {self.animal_type}'

    def get_age(self):
        return f'Age: {self.age}'

p = Pet()

p.set_name('Мурзик')
p.set_animal_type('Кот')
p.set_age(2)

print(p.get_name())
print(p.get_animal_type())
print(p.get_age())
'''

# 4 --------------------------------------------------------------------------------------------------------------------
''' 
class Car:

    def __init__(self, _year_model, rttake):
        self._year_model = _year_model
        self._make = rttake
        self._speed = 0

    def accelerate(self):
        self._speed += 5

    def break_(self):
        self._speed -= 5

    def get_speed(self):
        return self._speed

car = Car(2023, 'BMW')

for i in range(5):
    car.accelerate()
    print(f'Speed: {car.get_speed()}')

for i in range(5):
    car.break_()
    print(f'Speed: {car.get_speed()}')
'''

# 5 --------------------------------------------------------------------------------------------------------------------
'''
class Information:

    def __init__(self, name, adres, age, phone_number):
        self.__name = name
        self.__adres = adres
        self.__age = age
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_adres(self):
        return self.__adres

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def set_name(self, new_name):
        self.__name = new_name

    def set_adres(self, new_adres):
        self.__adres = new_adres

    def set_age(self, new_age):
        self.__age = new_age

    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

i1 = Information('Андриянов Кирилл', 'Южный парк', 17, '+7 905 396 10 44')
i1.set_adres('Пирамида')
print(i1.get_name())
print(i1.get_adres())
print(f'Лет: {i1.get_age()}')
print(i1.get_phone_number())

print()
i2 = Information('Андриянов Евгений', 'Волгоградская обл.', 41, '+7 909 432 53 28')
i2.set_phone_number('8 909 432 53 28')

print(i2.get_name())
print(i2.get_adres())
print(f'Лет: {i2.get_age()}')

print()
i3 = Information('Андриянова Ольга', 'Волгоградская обл.', 40, '+7 919 274 62 19')
i3.set_adres('Новониколаевский посёлок')

print(i3.get_name())
print(i3.get_adres())
print(f'Лет: {i3.get_age()}')
print(i3.get_phone_number())
'''

# 6 --------------------------------------------------------------------------------------------------------------------
'''
class Employee:

    def __init__(self, name, id, department, job_title):
        self.name = name
        self.id = id
        self.department = department
        self.job_title = job_title

    def __str__(self):
        return f'Имя: {self.name}, id: {self.id}, отдел: {self.department}, должность: {self.job_title}'


e1 = Employee('Сьюзан Мейерс', 47899, 'Бухгалтерия', 'Вице-президент')
print(e1)

e2 = Employee('Марк Джоунс', 39119, 'ИТ', 'Программист')
print(e2)

e3 = Employee('Джой Роджерс', 81774, 'Производственный', 'Инженер')
print(e3)
'''

# 7 --------------------------------------------------------------------------------------------------------------------
'''
class RetailItem:

    def __init__(self, options='', counts=0, price=0):
        self.options = options
        self.counts = counts
        self.price = price

    def __str__(self):
        return f'Описание: {self.options}, Количество на складе: {self.counts}, Цена: {self.price}'


ri1 = RetailItem('Пиджак', 12, 59.95)
print(ri1)
ri2 = RetailItem('Дизайнерские джинсы', 40, 34.95)
print(ri2)
ri3 = RetailItem('Рубашка', 20, 24.95)
print(ri3)
'''

# 8 --------------------------------------------------------------------------------------------------------------------
'''
class Patient:
    def __init__(self, full_name=[], full_adres=[], phone_number='', name_and_fast_phone=[]):
        self.full_name = full_name
        self.full_adres = full_adres
        self.phone_number = phone_number
        self.name_and_fast_phone = name_and_fast_phone

    def __str__(self):
        return f'Полное имя: {self.full_name}, Полный адрес: {self.full_adres}, Телефонный номер: {self.phone_number}, Имя и номер для срочной связи: {self.name_and_fast_phone}'

    def get_full_name(self):
        return self.full_name

    def get_full_adres(self):
        return self.full_adres

    def get_phone_number(self):
        return self.phone_number

    def get_name_and_fast_phone(self):
        return self.name_and_fast_phone

    def set_full_name(self, new_full_name):
        self.full_name = new_full_name

    def set_full_adres(self, new_full_adres):
        self.full_adres = new_full_adres

    def set_phone_number(self, new_number):
        self.phone_number = new_number

    def set_name_and_fast_phone(self, new_name_and_number):
        self.name_and_fast_phone = new_name_and_number

class Procedure:

    def __init__(self, name_pro='', date_pro='', name_doctor='', price=0):
        self.name_pro = name_pro
        self.date_pro = date_pro
        self.name_doctor = name_doctor
        self.price = price

    def __str__(self):
        return f'Название процедуры: {self.name_pro}, Дата процедуры: {self.date_pro}, Имя врача: {self.name_doctor}, Цена процедуры: {self.price} руб'

    def get_name_procedure(self):
        return self.name_pro

    def get_date_procedure(self):
        return self.date_pro

    def get_name_doctor(self):
        return self.name_doctor

    def get_price(self):
        return self.price

    def set_name_procedure(self, new):
        self.name_pro = new

    def set_date_procedure(self, new):
        self.date_pro = new

    def set_name_doctor(self, new):
        self.name_doctor = new

    def set_price(self, new):
        self.price = new


p = Patient(['Андриянов', 'Кирилл', 'Евгеньевич'], ['ул. Степная 172', 'Волгоград', 'Волгоградская обл.', 403909], 89053961044, ['Кирилл', 89053961044])
print(p)

print()

pro1 = Procedure('Врачебный осмотр', 'Сегодняшняя', 'Ирвин', 250.00)
print(pro1)
pro2 = Procedure('Рентгеноскопия', 'Сегодняшняя', 'Джемисон', 500.00)
print(pro2)
pro3 = Procedure('Анализ крови', 'Сегодняшняя', 'Смит', 200.00)
print(pro3)

print(f'Общая стоимость процедур: {pro1.price + pro2.price + pro3.price} руб')
'''

# 9 --------------------------------------------------------------------------------------------------------------------
'''
class Employee:

    def __init__(self, id, name, department, position):
        self.id = id
        self.name = name
        self.department = department
        self.position = position

    def info(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')
        print(f'Department: {self.department}')
        print(f'Position: {self.position}')


def find_employee(employees):
    employee_id = input('Введите id: ')

    if employee_id in employees:
        employees[employee_id].info()

    else:
        print('Класс не введён.')

def add_employee(employees):
    employee_id = input('Введите id: ')

    if employee_id in employees:
        print('Сотрудник уже существует')
    else:
        name = input('Введите имя сотрудника: ')
        department = input('Введите отдел сотрудника: ')
        position = input('Введите должность сотрудника: ')

        employee = Employee(employee_id, name, department, position)

        employees[employee_id] = employee

        print('Сотрудник внесён в базу данных.')


def update_employee(employees):
    employee_id = input('Введите id сотрудника: ')

    if employee_id in employees:
        name = input('Введите новое имя для сотрудника: ')
        department = input('Введите отдел для сотрудника: ')
        position = input('Введите должность для сотрудника: ')

        employee = employees[employee_id]

        employee.name = name
        employee.department = department
        employee.position = position
        print('Данные сотрудника обновлены.')
    else:
        print('Такого сотрудника нету в базе данных.')

def remove_employee(employees):
    employee_id = input('Введите ID сотрудника: ')

    if employee_id in employees:
        del employees[employee_id]
        print('Сотрудник удалён.')
    else:
        print('Сотрудник не найден')


def main():

    employees = {}

    while True:
        print('Меню:')
        print('1. Найти сотрудника')
        print('2. Добавить сотрудника')
        print('3. Обновить сотрудника')
        print('4. Удалить сотрудника')
        print('5. Exit')

        choose = input('Введите нужное действие: ')

        if choose == '1':
            find_employee(employees)
        elif choose == '2':
            add_employee(employees)
        elif choose == '3':
            update_employee(employees)
        elif choose == '4':
            remove_employee(employees)
        elif choose == '5':
            break
        else:
            print('Не правильный выбор')


if __name__ == '__main__':
    main()
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Прежде добавьте сотрудника, а уже после можно совершить поиск по id и прочии функции. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''

# 10 -------------------------------------------------------------------------------------------------------------------
'''
class RetailItem:
    def __init__(self, number, options, counts, price):
        self.number = number
        self.options = options
        self.counts = counts
        self.price = price

    def info(self):
        print(f'Товар № {self.number}\nОписание товара: {self.options}\nКоличество на складе: {self.counts}\nЦена: {self.price}\n')
class CashRegister:
    def __init__(self):
        self.items = []

    def purchase_item(self, retail_item):
        self.items.append(retail_item)

    def get_total(self):
        total_cost = sum(item.price for item in self.items)
        return total_cost

    def show_items(self):
        for item in self.items:
            item.info()

    def clear(self):
        self.items = []


cr = CashRegister()

i1 = RetailItem(1,"Пиджак", 12, 59.95)
i2 = RetailItem(2,"Дизайнерские джинсы", 40, 34.95)
i3 = RetailItem(3,"Рубашка", 20, 24.95)

cr.purchase_item(i1)
cr.purchase_item(i2)
cr.purchase_item(i3)

print("Выбранные товары:\n")
cr.show_items()

total_cost = round(cr.get_total(), 2)
print(f"Общая стоимость: {total_cost}")

cr.clear()
'''

# 11 -------------------------------------------------------------------------------------------------------------------
class Question:
    def __init__(self, question, p1, p2, p3, p4, correct_answer):
        self.question = question
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.correct_answer = correct_answer

    def display_question(self):
        print(f'{self.question}\n1: {self.p1}\n2: {self.p2}\n3: {self.p3}\n4: {self.p4}')

    def get_correct_answer(self):
        return self.correct_answer

    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer

ques1 = Question("Вопрос 1: Какая самая большая планета в Солнечной системе?", "Юпитер", "Марс", "Земля", "Венера", 1)
ques2 = Question("Вопрос 2: Кто написал 'Мёртвые души'?", "Достоевский", "Шекспир", "Толстой", "Гоголь", 4)
ques3 = Question("Вопрос 3: Какая самая маленькая планета в Солнечной системе?", "Марс", "Меркурий", "Венера", "Сатурн", 2)
ques4 = Question("Вопрос 4: Сколько сторон у квадрата?", "2", "3", "4", "5", 3)
ques5 = Question("Вопрос 5: В каком году отменили крепостное право?", "1776", "1789", "1801", "1861", 4)
ques6 = Question("Вопрос 6: Кто был автором картины 'Мона Лиза'?", "Микеланджело", "Леонардо да Винчи", "Ван Гог", "Пикассо", 2)
ques7 = Question("Вопрос 7: Сколько материков на Земле?", "5", "6", "7", "8", 2)
ques8 = Question("Вопрос 8: Сколько химических элементов в таблице Менделеева?", "96", "54", "132", "118", 4)
ques9 = Question("Вопрос 9: Сколько углов в шестиугольной пирамиде?", "6", "7", "8", "5", 2)
ques10 = Question("Вопрос 10: Сколько костей в человеческом скелете?", "150", "206", "250", "300", 2)

quiz_questions = [ques1, ques2, ques3, ques4, ques5, ques6, ques7, ques8, ques9, ques10]
def start_test():
    pl1_score = 0
    pl2_score = 0

    for i in range(5):
        print(f"\nВопрос {i + 1} для игрока 1:")
        quiz_questions[i].display_question()
        pl1_answer = int(input("Введите номер правильного ответа (1-4): "))
        if pl1_answer == quiz_questions[i].get_correct_answer():
            pl1_score += 1

        print(f"\nВопрос {i + 1} для игрока 2:")
        quiz_questions[i + 5].display_question()
        pl2_answer = int(input("Введите номер правильного ответа (1-4): "))
        if pl2_answer == quiz_questions[i + 5].get_correct_answer():
            pl2_score += 1

    print(f'Результаты:\nПервый игрок: {pl1_score} очков\nВторой игрок: {pl2_score} очков')

    if pl1_score > pl2_score:
        print('Первый игрок победил!!!')
    elif pl1_score < pl2_score:
        print('Второй игрок победил!!!')
    else:
        print('Ничья!')

start_test()




