class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"Gender: {self.gender} \nAge: {self.age} \nFirst name: {self.first_name} \nLast name: {self.last_name}"

class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{super().__str__()} \nRecord book: {self.record_book}"

class Group:

    def __init__(self, number: int) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        self.group.discard(last_name)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self) -> str:
        all_students = '\n\n'.join(str(st) for st in self.group)
        return f'Number:{self.number}\n\n{all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
