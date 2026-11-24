import json
import unittest

from src.main import translate_address
from tests.verify import bitwise_oracle
from src.validator import (
    ValidationError,
    validate_page_size,
    validate_page_table,
    validate_system,
)


class TestPagingTranslation(unittest.TestCase):

    def setUp(self):
        with open("input/input.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.page_size = self.data["page_size"]
        self.page_table = self.data["page_table"]

    def test_system_input_validation(self):
        self.assertTrue(validate_system(self.data))

    def test_invalid_page_size(self):
        with self.assertRaises(ValidationError):
            validate_page_size(0)
        with self.assertRaises(ValidationError):
            validate_page_size(10)  # Not a power of 2

    def test_invalid_page_table_entry(self):
        bad_table = [{"frame": 1, "valid": 2}]
        with self.assertRaises(ValidationError):
            validate_page_table(bad_table)

    def test_boundary_zero_address(self):
        res = translate_address(0, self.page_size, self.page_table)
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["physical_address"], 80)

    def test_boundary_max_offset(self):
        res = translate_address(15, self.page_size, self.page_table)
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["physical_address"], 95)

    def test_valid_translation_example(self):
        res = translate_address(37, self.page_size, self.page_table)
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["page_number"], 2)
        self.assertEqual(res["offset"], 5)
        self.assertEqual(res["frame_number"], 7)
        self.assertEqual(res["physical_address"], 117)

    def test_page_fault_invalid_bit(self):
        res = translate_address(48, self.page_size, self.page_table)
        self.assertEqual(res["status"], "PAGE FAULT")
        self.assertIsNone(res["physical_address"])

    def test_out_of_bounds_page_number(self):
        res = translate_address(80, self.page_size, self.page_table)
        self.assertEqual(res["status"], "INVALID")
        self.assertIsNone(res["physical_address"])

    def test_negative_logical_address(self):
        res = translate_address(-5, self.page_size, self.page_table)
        self.assertEqual(res["status"], "INVALID")
        self.assertIsNone(res["physical_address"])

    def test_cross_check_all_with_bitwise_oracle(self):
        for addr in self.data["logical_addresses"]:
            main_res = translate_address(addr, self.page_size, self.page_table)
            expected_status, expected_pa = bitwise_oracle(
                addr, self.page_size, self.page_table
            )
            self.assertEqual(main_res["status"], expected_status)
            self.assertEqual(main_res["physical_address"], expected_pa)


if __name__ == "__main__":
    unittest.main(verbosity=2)

