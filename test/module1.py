from dataclasses import dataclass
import typing as t


@dataclass
class Student:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Student(name={self.name}, age={self.age})"

    def get_year_born(self) -> int:
        """
        Return the year the student was born.
        """
        return 2022

    def get_marks(self, subject: str) -> int:
        """
        Return the marks of the student in a subject.
        """
        return 100


@dataclass
class Teacher:
    name: str
    age: int

    def __str__(self) -> str:
        return f"Teacher(name={self.name}, age={self.age})"

    def get_salary(self) -> int:
        """
        Return the salary of the teacher.
        """
        return 1000

    def get_subjects_taught(self) -> list:
        """
        Return the subjects taught by the teacher.
        """
        return ["Maths", "Science"]


@dataclass
class School:
    students: t.List[Student]
    teachers: t.List[Teacher]

    def get_students(self, teacher: Teacher) -> t.List[Student]:
        """
        Return the students of a teacher.

        Parameters
        ----------
        teacher (Teacher): The teacher object.

        Returns
        -------
        list: The list of students.
        """
        return self.students

    def get_teachers(self, student: Student) -> t.List[Teacher]:
        """
        Return the teachers of a student.
        Parameters:
        student (Student): The student object.
        Returns:
        list: The list of teachers.
        """
        return self.teachers
