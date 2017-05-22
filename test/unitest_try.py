import unittest


class SimplisticTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = range(1, 10)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        self.assertTrue(True)

    def test_pass(self):
        self.assertTrue(True, 'test_pass failed.')

    def test_fail(self):
        self.assertTrue(False, 'test_fail failed.')

    def test_error(self):
        raise RuntimeError('Test error!')

    def test_fixture(self):
        print('in test_fixture()')
        self.assertEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
    unittest.main()
