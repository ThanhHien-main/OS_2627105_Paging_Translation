
import unittest

from validator import (
    validate_virtual_address,
    validate_page_size,
    ValidationError
)

from verify import (
    verify_translation,
    VerificationError
)


class TestPagingTranslation(unittest.TestCase):

    def setUp(self):

        self.page_size = 256

        self.page_table = {
            0: 2,
            1: 5,
            2: 1,
            3: 7,
            4: 3
        }

    def test_validate_virtual_address(self):

        self.assertTrue(
            validate_virtual_address(1024)
        )

    def test_negative_virtual_address(self):

        with self.assertRaises(
            ValidationError
        ):
            validate_virtual_address(-1)

    def test_valid_page_size(self):

        self.assertTrue(
            validate_page_size(256)
        )

    def test_invalid_page_size(self):

        with self.assertRaises(
            ValidationError
        ):
            validate_page_size(0)

    def test_page_number_calculation(self):

        address = 1025

        page_number = (
            address // self.page_size
        )

        self.assertEqual(
            page_number,
            4
        )

    def test_offset_calculation(self):

        address = 1025

        offset = (
            address % self.page_size
        )

        self.assertEqual(
            offset,
            1
        )

    def test_frame_lookup(self):

        self.assertEqual(
            self.page_table[4],
            3
        )

    def test_physical_address(self):

        address = 1025

        page_number = (
            address // self.page_size
        )

        offset = (
            address % self.page_size
        )

        frame_number = (
            self.page_table[page_number]
        )

        physical_address = (
            frame_number *
            self.page_size +
            offset
        )

        self.assertEqual(
            physical_address,
            769
        )

    def test_translation_verification(self):

        address = 1025

        page_number = (
            address // self.page_size
        )

        offset = (
            address % self.page_size
        )

        frame_number = (
            self.page_table[page_number]
        )

        physical_address = (
            frame_number *
            self.page_size +
            offset
        )

        self.assertTrue(
            verify_translation(
                address,
                self.page_size,
                self.page_table,
                page_number,
                offset,
                frame_number,
                physical_address
            )
        )

    def test_wrong_frame(self):

        address = 1025

        page_number = 4

        offset = 1

        wrong_frame = 99

        physical_address = (
            wrong_frame *
            self.page_size +
            offset
        )

        with self.assertRaises(
            VerificationError
        ):
            verify_translation(
                address,
                self.page_size,
                self.page_table,
                page_number,
                offset,
                wrong_frame,
                physical_address
            )


if __name__ == "__main__":
    unittest.main()