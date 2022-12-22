import unittest
from company.app.company import Employee, Manager, CompanyDatabaseError

class TestManagerClass(unittest.TestCase):

  #Inicijalna podesavanja za test - izvrsava se prije svakog testa
  def setUp(self) -> None:
    #Keriranje zaposlenih
    self.employee_2 = Employee("Milan", "Brujic", 2500, 61)
    self.employee_3 = Employee("Dejan", "Pavic", 2500, 61)

    #Keriranje menadzera
    self.manager_1 = Manager("Marko", "Petricevic", 3000, 82, [self.employee_2])
    self.manager_2 = Manager("Mirjana", "Jambrek", 2500, 100)

  #Test za povjeru informacija o zaposlenom koji je podredjen menadzeru
  def test_manager_has_employee(self):
    number_of_employees = len(self.manager_1.employees)

    self.assertEqual(number_of_employees, 1)
    self.assertEqual(self.manager_1.employees, [self.employee_2])
    self.assertEqual(self.manager_1.employees[0].fullName, "Milan Brujic")
    self.assertEqual(self.manager_1.employees[0].email, "milanbrujic@servalit.com")

  #Test za provjeru add_employee() metode kada je employee koji se dodaje vec podredjen tom menadzeru 
  def test_manager_add_employee_that_already_exists(self):
    
    with self.assertRaises(CompanyDatabaseError):
      self.manager_1.add_employee(self.employee_2)

    # Nije dobra praksa?
    self.manager_1.add_employee(self.employee_3)
    with self.assertRaises(CompanyDatabaseError):
      self.manager_1.add_employee(self.employee_3)

  ##Test za provjeru add_employee() kada jos ne proslijedi instanca klase Employee
  def test_manager_add_employee_wrong_type(self):

    with self.assertRaises(TypeError):
      self.manager_1.add_employee("Nikola")
    with self.assertRaises(TypeError):
      self.manager_1.add_employee(11)

  ##Test za provjeru add_employee() metode
  def test_manager_add_employee(self):

    self.manager_1.add_employee(self.employee_3)
    self.assertEqual(self.manager_1.employees, [self.employee_2, self.employee_3])

  ##Test za provjeru remove_employee() metode kada se pokusava ukloniti zaposleni koji nije podredjen menadzeru
  def test_manager_remove_employee_when_employee_not_there(self):

    with self.assertRaises(CompanyDatabaseError):
      self.manager_1.remove_employee(self.employee_3)

  ##Test za provjeru remove_employee() metode
  def test_manager_remove_employee(self):

    self.manager_1.remove_employee(self.employee_2)
    self.assertEqual(self.manager_1.employees, [])

  ##Test za provjeru list_employees() metode
  def test_manager_list_employees(self):
    employees = self.manager_1.list_employees()

    self.assertEqual(employees, ["Milan Brujic -- milanbrujic@servalit.com"])

  ##Test za provjeru list_employees() metode kada menadzer nema podredjenih
  def test_manager_list_employees_when_list_is_empty(self):

    with self.assertRaises(CompanyDatabaseError):
      self.manager_2.list_employees()

  ##Isti testovi kao i u test_employee_class.py fajlu samo primjenjni na menadzere
  def test_manager_fullName(self):
    mng_1_full_name = self.manager_1.fullName
    mng_2_full_name = self.manager_2.fullName

    self.assertEqual(mng_1_full_name, "Marko Petricevic")
    self.assertEqual(mng_2_full_name, "Mirjana Jambrek")

  #Test za property polje email - koji se sastoji od drugih polja
  def test_manager_email(self):
    mng_1_email = self.manager_1.email
    mng_2_email = self.manager_2.email

    self.assertEqual(mng_1_email, "markopetricevic@servalit.com")
    self.assertEqual(mng_2_email, "mirjanajambrek@servalit.com")

  #Test za metodu raise_pay() koja uvecava platu zaposlenog za odredjenu konstantu(1.3)
  def test_manager_apply_raise(self):
    mng_1_raise = self.manager_1.raise_pay()
    mng_2_raise = self.manager_2.raise_pay()

    self.assertEqual(mng_1_raise, 4800) # 1.3 x 3000
    self.assertEqual(mng_2_raise, 4000) # 1.3 x 2500

  #Test za metodu can_be_promoted() koja na osnovu polja performace_score vraca true ili false
  def test_manager_can_be_promoted(self):
    mng_1_promotion = self.manager_1.can_be_promoted()
    mng_2_promotion = self.manager_2.can_be_promoted()

    self.assertEqual(mng_1_promotion, True)
    self.assertEqual(mng_2_promotion, True)



if __name__ == "__main__":
  unittest.main()   