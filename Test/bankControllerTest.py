from Scripts.bank.bankController import BankController
import unittest

INFO01 = "info01"
INFO02 = "info02"
DESCRIPTION01 = "test 01"
DESCRIPTION02 = "test 02"

class bankControllerTest(unittest.TestCase):

    def setUp(self):
        BankController.create_database(None)

    def test_insert(self):
        BankController.insert(None, INFO01, DESCRIPTION01)
        info = BankController.getNames(None)
        description = BankController.getDescription(None, INFO01)
        self.assertEqual(INFO01, info[0])
        self.assertEqual(DESCRIPTION01, description)

    def test_update(self):
        BankController.insert(None, INFO01, DESCRIPTION01)
        info = BankController.getNames(None)
        description = BankController.getDescription(None, INFO01)
        self.assertEqual(INFO01, info[0])
        self.assertEqual(DESCRIPTION01, description)
        BankController.update(None, INFO01, DESCRIPTION02)
        description = BankController.getDescription(None, INFO01)
        self.assertEqual(DESCRIPTION02, description)

    def test_delete(self):
        BankController.insert(None, INFO01, DESCRIPTION01)
        info = BankController.getNames(None)
        description = BankController.getDescription(None, INFO01)
        self.assertEqual(INFO01, info[0])
        self.assertEqual(DESCRIPTION01, description)
        BankController.delete(None, INFO01)
        description = BankController.getDescription(None, INFO01)
        self.assertEqual("", description)

    def test_getNames(self):
        BankController.insert(None, INFO01, DESCRIPTION01)
        BankController.insert(None, INFO02, DESCRIPTION02)
        info02 = BankController.getNames(None)[0]
        info01 = BankController.getNames(None)[1]
        self.assertEqual(INFO02, info02)
        self.assertEqual(INFO01, info01)

    def test_getDescription(self):
        BankController.insert(None, INFO01, DESCRIPTION01)
        BankController.insert(None, INFO02, DESCRIPTION02)
        description01 = BankController.getDescription(None, INFO01)
        description02 = BankController.getDescription(None, INFO02)
        self.assertEqual(DESCRIPTION01, description01)
        self.assertEqual(DESCRIPTION02, description02)

if __name__ == '__main__':
    unittest.main()
