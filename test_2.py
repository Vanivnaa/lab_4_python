from models.hockeygoods import HockeyGoods
from models.enums.sort import SortOrder
from models.enums.type import Type 
from models.manage import HockeyClubManage
from models.skates import Skates
from models.stick import Stick
from models.protectiveequipment import ProtectiveEquipment, Protection
import main
import unittest

class TestHockeyClubManage(unittest.TestCase):
    def setUp(self):
        self.skates = Skates("Skates", 1500, 1148, "TECNOPRO", "China", "black", Type.FIELD_PLAYER, "pvc leather", 2, 39)
        self.stick = Stick("Stick", 1752, 500, "FISHER", "Germany", "yellow", Type.FIELD_PLAYER, "carbon fiber, fiberglass", 166, 85, 135)
        self.helmet = ProtectiveEquipment("Helmet", 1248, 600, "Bauer", "Poland", "white", Type.GOALKEEPER, "plastic", "Adult", 1)
        self.manage = HockeyClubManage([self.skates, self.stick, self.helmet])
        

    def test_search_by_type(self):
        self.assertListEqual(self.manage.search_by_type(Type.FIELD_PLAYER), [self.skates, self.stick])

    def test_sort_by_price(self):
        self.assertEqual(self.manage.sort_by_price(SortOrder.ASC), [self.helmet, self.skates, self.stick])
        self.assertEqual(self.manage.sort_by_price(SortOrder.DESC), [self.stick, self.skates, self.helmet])

    def test_sort_by_country(self):
        self.assertEqual(self.manage.sort_by_country(SortOrder.ASC), [self.skates, self.stick, self.helmet])
        self.assertEqual(self.manage.sort_by_country(SortOrder.DESC), [self.helmet, self.stick, self.skates])

if __name__ == '__main__':
    unittest.main()


