class Student:
    def _init_(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def pass_fail(self):
        average = self.calculate_average()
        if average >= 60:
            return 'Pass'
        else:
            return 'Fail'

    def display_report(self):
        average = self.calculate_average()
        grade = self.calculate_grade()
        status = self.pass_fail()
        print(f"Student Name: {self.name}")
        print(f"Scores: {self.scores}")
        print(f"Average Score: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")

def main():
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))
    scores = []
    for i in range(num_subjects):
        score = float(input(f"Enter score for subject {i+1}: "))
        scores.append(score)

    student = Student(name, scores)
    student.display_report()

