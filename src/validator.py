from typing import Dict, List, Any


class ValidationError(Exception):
    """Custom validation exception for Paging input data."""
    pass


def validate_integer(value: Any, field_name: str = "Value") -> bool:
    """Check whether a value is an integer (excluding bool)."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValidationError(f"{field_name} must be an integer.")
    return True


def validate_non_negative(value: Any, field_name: str = "Value") -> bool:
    """Check whether a value is a non-negative integer."""
    validate_integer(value, field_name)
    if value < 0:
        raise ValidationError(f"{field_name} cannot be negative.")
    return True


def validate_page_size(page_size: Any) -> bool:
    """Validate that page_size is a positive power of 2."""
    validate_integer(page_size, "Page Size")
    if page_size <= 0 or (page_size & (page_size - 1)) != 0:
        raise ValidationError("Page Size must be a positive power of 2 (e.g., 16).")
    return True


def validate_page_table(page_table: List[Dict[str, int]]) -> bool:
    """
    Validate single-level page table structure matching input.json:
    [{"frame": 5, "valid": 1}, ...]
    """
    if not isinstance(page_table, list) or len(page_table) == 0:
        raise ValidationError("Page Table must be a non-empty list of entries.")

    for idx, entry in enumerate(page_table):
        if not isinstance(entry, dict):
            raise ValidationError(f"Page Table entry {idx} must be a dictionary.")
        if "frame" not in entry or "valid" not in entry:
            raise ValidationError(f"Page Table entry {idx} must contain 'frame' and 'valid' keys.")
        validate_non_negative(entry["frame"], f"Frame Number at page {idx}")
        if entry["valid"] not in (0, 1):
            raise ValidationError(f"Valid bit at page {idx} must be 0 or 1.")

    return True


def validate_system(data: Dict[str, Any]) -> bool:
    """Validate the entire input configuration dictionary."""
    if not isinstance(data, dict):
        raise ValidationError("Input configuration must be a JSON object.")

    for key in ("page_size", "page_table", "logical_addresses"):
        if key not in data:
            raise ValidationError(f"Missing required field: '{key}'.")

    validate_page_size(data["page_size"])
    validate_page_table(data["page_table"])

    if not isinstance(data["logical_addresses"], list):
        raise ValidationError("'logical_addresses' must be a list.")

    for idx, addr in enumerate(data["logical_addresses"]):
        validate_integer(addr, f"Logical Address at index {idx}")

    return True


if __name__ == "__main__":
    import json
    with open("input/input.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    if validate_system(config):
        print("VALIDATION PASSED: input.json structure and constraints are valid.")
