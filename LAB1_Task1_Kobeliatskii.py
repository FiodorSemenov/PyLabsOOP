class Library:
    def __init__(self, name: str, capacity: int):
        """
        Создание и подготовка к работе объекта "Библиотека".

        :param name: Название библиотеки.
        :param capacity: Вместимость библиотеки (должна быть положительной).
        :raises ValueError: Если вместимость меньше или равна 0.

        Пример:
        >>> library = Library("Городская библиотека", 5)  # инициализация экземпляра класса
        """
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительной.")
        self.name = name
        self.capacity = capacity
        self.books = []

    def add_book(self, book_title: str) -> None:
        """
        Добавление книги в библиотеку.

        :param book_title: Название книги.
        :raises ValueError: Если библиотека заполнена.

        >>> library = Library("Городская библиотека", 2)
        >>> library.add_book("Преступление и наказание")
        >>> library.add_book("Мастер и Маргарита")
        >>> library.books
        ['Преступление и наказание', 'Мастер и Маргарита']
        """
        if len(self.books) >= self.capacity:
            raise ValueError("Библиотека заполнена.")
        self.books.append(book_title)

    def get_book_count(self) -> int:
        """
        Получение количества книг в библиотеке.

        :return: Количество книг.
        :rtype: int

        >>> library = Library("Городская библиотека", 5)
        >>> library.add_book("Мастер и Маргарита")
        >>> library.get_book_count()
        1
        """
        return len(self.books)


class Student:
    def __init__(self, name: str, grade: int, gpa: float):
        """
        Инициализация учащегося.

        :param name: Имя учащегося.
        :param grade: Класс учащегося (должен быть от 1 до 11).
        :param gpa: Средний балл (должен быть от 0.0 до 5.0).
        :raises ValueError: Если класс вне диапазона 1-11 или GPA вне диапазона 0.0-5.0.
        """
        if grade < 1 or grade > 11:
            raise ValueError("Класс должен быть от 1 до 11.")
        if gpa < 0.0 or gpa > 5.0:
            raise ValueError("Средний балл должен быть от 0.0 до 5.0.")
        self.name = name
        self.grade = grade
        self.gpa = gpa

    def update_gpa(self, new_gpa: float) -> None:
        """
        Обновление среднего балла.

        :param new_gpa: Новый средний балл (должен быть от 0.0 до 5.0).
        :raises ValueError: Если новый GPA вне диапазона 0.0-5.0.

        >>> student = Student("Анна", 10, 3.5)
        >>> student.update_gpa(3.8)
        >>> student.gpa
        3.8
        """
        if new_gpa < 0.0 or new_gpa > 5.0:
            raise ValueError("Средний балл должен быть от 0.0 до 5.0.")
        self.gpa = new_gpa

    def get_info(self) -> str:
        """
        Получение информации об учащемся.

        :return: Информация об учащемся.
        :rtype: str

        >>> student = Student("Анна", 10, 3.5)
        >>> student.get_info()
        'Учащийся: Анна, Класс: 10, Средний балл: 3.5'
        """
        return f"Учащийся: {self.name}, Класс: {self.grade}, Средний балл: {self.gpa}"


class Worker:
    def __init__(self, name: str, position: str, salary: float):
        """
        Инициализация работника.

        :param name: Имя работника.
        :param position: Должность работника.
        :param salary: Зарплата работника (должна быть положительной).
        :raises ValueError: Если зарплата меньше или равна 0.
        """
        if salary <= 0:
            raise ValueError("Зарплата должна быть положительной.")
        self.name = name
        self.position = position
        self.salary = salary

    def promote(self, new_position: str, salary_increase: float) -> None:
        """
        Повышение в должности работника.

        :param new_position: Новая должность.
        :param salary_increase: Увеличение зарплаты (должно быть положительным).
        :raises ValueError: Если увеличение зарплаты меньше или равно 0.

        >>> worker = Worker("Иван", "Менеджер", 50000)
        >>> worker.promote("Директор", 10000)
        >>> worker.position
        'Директор'
        >>> worker.salary
        60000
        """
        if salary_increase <= 0:
            raise ValueError("Увеличение зарплаты должно быть положительным.")
        self.position = new_position
        self.salary += salary_increase

    def get_info(self) -> str:
        """
        Получение информации о работнике.

        :return: Информация о работнике.
        :rtype: str

        >>> worker = Worker("Иван", "Менеджер", 50000)
        >>> worker.get_info()
        'Работник: Иван, Должность: Менеджер, Зарплата: 50000'
        """
        return f"Работник: {self.name}, Должность: {self.position}, Зарплата: {self.salary}"

    def update_salary(self, new_salary: float) -> None:
        """
        Обновление зарплаты работника.

        :param new_salary: Новая зарплата (должна быть положительной).
        :raises ValueError: Если новая зарплата меньше или равна 0.

        >>> worker = Worker("Иван", "Менеджер", 50000)
        >>> worker.update_salary(55000)
        >>> worker.salary
        55000
        """
        if new_salary <= 0:
            raise ValueError("Новая зарплата должна быть положительной.")
        self.salary = new_salary
