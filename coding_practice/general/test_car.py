import unittest
from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('Ford', 'Fiesta', '2008')

    def test_car_name(self):
        self.assertEqual(self.car.car_name, '2008 Ford Fiesta')

        self.car.model = 'Taurus'

        self.assertEqual(self.car.car_name, '2008 Ford Taurus')

    def test_car_name_no_year(self):
        self.assertEqual(self.car.car_name_no_year, 'Ford Fiesta')

        self.car.model = 'Taurus'

        self.assertEqual(self.car.car_name_no_year, 'Ford Taurus')


if __name__ == '__main__':
    unittest.main()
