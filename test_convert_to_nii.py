import unittest

import convert_to_nii


class TestConvertToNiiMethods(unittest.TestCase):

    def test_main(self):
        data_root = 'data/unit_test/'
        self.assertTrue(convert_to_nii.main(data_root=data_root))


if __name__ == '__main__':
    unittest.main()
