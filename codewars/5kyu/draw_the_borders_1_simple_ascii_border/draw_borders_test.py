import unittest
from draw_borders import Solution
from ddt import ddt, data, unpack

@ddt
class Tester(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    @data(
        [{(1,1), (2,1)}, 
        {(0,0), (0,1), (0,2), (1,0),(1,2),(2,0),(2,2), (3,0),(3,1),(3,2)}],
    )
    @unpack
    def test_get_borders(self, shape, expected):
        ret = self.s.get_borders(shape)
        self.assertEqual(ret, expected)


    @data(
        [{(1,1),(1,2),(1,3),(1,4),(1,5), \
            (2,1),(3,1),(4,1),(5,1), \
            (2,5),(3,5),(4,5),(5,5), \
            (5,2), (5,3), (5,4), \
            (3,3)
        },
        {(1,1),(1,2),(1,3),(1,4),(1,5), \
            (2,1),(3,1),(4,1),(5,1), \
            (2,5),(3,5),(4,5),(5,5), \
            (5,2), (5,3), (5,4)
        }]
    )
    @unpack
    def test_remove_donu(self, borders, expected):
        ret = self.s.remove_donut(borders)
        self.assertEqual(ret, expected)

if __name__ == '__main__':
    unittest.main()
