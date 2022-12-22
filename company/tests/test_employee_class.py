import unittest
from company.app.company import Employee


class TestEmployeeClass(unittest.TestCase):

  #Inicijalna podesavanja za test - izvrsava se prije svakog testa
  def setUp(self) -> None:
    self.employee_1 = Employee("Marko", "Petricevic", 3000, 82)
    self.employee_2 = Employee("Milan", "Brujic", 2500, 61)

  #Test za property polje fullName - koji se sastoji od drugih polja
  def test_employee_fullName(self):
    emp_1_full_name = self.employee_1.fullName
    emp_2_full_name = self.employee_2.fullName

    self.assertEqual(emp_1_full_name, "Marko Petricevic")
    self.assertEqual(emp_2_full_name, "Milan Brujic")

  #Test za property polje email - koji se sastoji od drugih polja
  def test_employee_email(self):
    emp_1_email = self.employee_1.email
    emp_2_email = self.employee_2.email

    self.assertEqual(emp_1_email, "markopetricevic@servalit.com")
    self.assertEqual(emp_2_email, "milanbrujic@servalit.com")

  #Test za metodu raise_pay() koja uvecava platu zaposlenog za odredjenu konstantu(1.3)
  def test_employee_apply_raise(self):
    emp_1_raise = self.employee_1.raise_pay()
    emp_2_raise = self.employee_2.raise_pay()

    self.assertEqual(emp_1_raise, 3900) # 1.3 x 3000
    self.assertEqual(emp_2_raise, 3250) # 1.3 x 2500

  #Test za metodu can_be_promoted() koja na osnovu polja performace_score vraca true ili false
  def test_employee_can_be_promoted(self):
    emp_1_promotion = self.employee_1.can_be_promoted()
    emp_2_promotion = self.employee_2.can_be_promoted()

    self.assertEqual(emp_1_promotion, True)
    self.assertEqual(emp_2_promotion, False)


if __name__ == "__main__":
  unittest.main()