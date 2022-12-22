class CompanyDatabaseError(Exception):
  pass


class Employee: 
  pay_raise_amount = 1.3 #const

  def __init__(self, first_name, last_name, pay, performace_score) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.pay = pay
    self.performace_score = performace_score

  @property
  def fullName(self):
    return f"{self.first_name} {self.last_name}"

  @property
  def email(self):
    return f"{self.first_name}{self.last_name}@servalit.com".lower()

  def raise_pay(self):
    self.pay = int(self.pay * self.pay_raise_amount)
    return self.pay

  def can_be_promoted(self):
    return True if self.performace_score > 70 else False


class Manager(Employee):

  pay_raise_amount = 1.6 #const

  def __init__(self, first_name, last_name, pay, performace_score, employees = []) -> None:
    super().__init__(first_name, last_name, pay, performace_score)
    self.employees = employees

  def list_employees(self):
    if len(self.employees) == 0:
      raise CompanyDatabaseError(f"There is no employees in db")
    else:
      for employee in self.employees:
        print(f"{employee.fullName} -- {employee.email}")


  def add_employee(self, employee):
    if type(employee) is not Employee:
      raise TypeError("Please provide correct instance of employee")
    else:
      if employee in self.employees:
        raise CompanyDatabaseError(f"Employee with {employee.fullName} alredy exists in company database")
      else:
        self.employees.append(employee)

  def remove_employee(self, employee):
    if self.employees == []:
      raise CompanyDatabaseError(f"This manager has no employees under him in hierarcy")
    else: 
      if employee in self.employees:
        self.employees.remove(employee)
      else:
        raise CompanyDatabaseError(f"Employee {employee.fullName} does not exist in db")
