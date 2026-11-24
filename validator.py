
from typing import Dict


class ValidationError(Exception):
    """Custom validation exception"""
    pass


def validate_integer(value, field_name="Value"):
    """
    Check whether a value is an integer.
    """

    if not isinstance(value, int):
        raise ValidationError(
            f"{field_name} must be an integer."
        )

    return True


def validate_non_negative(value, field_name="Value"):
    """
    Check whether a value is non-negative.
    """

    validate_integer(value, field_name)

    if value < 0:
        raise ValidationError(
            f"{field_name} cannot be negative."
        )

    return True


def validate_virtual_address(address):
    """
    Validate virtual address.
    """

    validate_non_negative(
        address,
        "Virtual Address"
    )

    return True


def validate_physical_address(address):
    """
    Validate physical address.
    """

    validate_non_negative(
        address,
        "Physical Address"
    )

    return True


def validate_page_size(page_size):
    """
    Validate page size.
    """

    validate_integer(
        page_size,
        "Page Size"
    )

    if page_size <= 0:
        raise ValidationError(
            "Page Size must be greater than 0."
        )

    return True


def validate_frame_number(frame_number, number_of_frames):
    """
    Validate frame number.
    """

    validate_non_negative(
        frame_number,
        "Frame Number"
    )

    validate_non_negative(
        number_of_frames,
        "Number Of Frames"
    )

    if frame_number >= number_of_frames:
        raise ValidationError(
            f"Frame Number {frame_number} "
            f"out of range [0, {number_of_frames - 1}]"
        )

    return True


def validate_page_number(page_number, number_of_pages):
    """
    Validate page number.
    """

    validate_non_negative(
        page_number,
        "Page Number"
    )

    validate_non_negative(
        number_of_pages,
        "Number Of Pages"
    )

    if page_number >= number_of_pages:
        raise ValidationError(
            f"Page Number {page_number} "
            f"out of range [0, {number_of_pages - 1}]"
        )

    return True


def validate_page_table(page_table: Dict):
    """
    Validate page table structure.
    Example:
    {
        0: 3,
        1: 7,
        2: 4
    }
    """

    if not isinstance(page_table, dict):
        raise ValidationError(
            "Page Table must be a dictionary."
        )

    for vpn, pfn in page_table.items():

        validate_non_negative(
            vpn,
            "Virtual Page Number"
        )

        validate_non_negative(
            pfn,
            "Physical Frame Number"
        )

    return True


def validate_offset(offset, page_size):
    """
    Validate page offset.
    """

    validate_non_negative(
        offset,
        "Offset"
    )

    if offset >= page_size:
        raise ValidationError(
            f"Offset must be less than Page Size ({page_size})."
        )

    return True


def validate_system