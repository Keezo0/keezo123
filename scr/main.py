import structure

def summ(a: int, b: int) -> int:
    return a + b

tom = structure.Employee("Tom", 45, "01.03.2022")
michael = structure.Employee("Michael", 20, "14.08.2024")

if __name__ == "__main__":
    print(tom.print_employee())
    print(michael.print_employee())