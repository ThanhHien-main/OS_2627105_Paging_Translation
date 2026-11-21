import json


def independent_check(address, page_size, page_table):
    page = address // page_size
    offset = address % page_size

    if page >= len(page_table):
        return "INVALID", None

    entry = page_table[page]

    if entry["valid"] == 0:
        return "PAGE FAULT", None

    physical_address = entry["frame"] * page_size + offset

    return "SUCCESS", physical_address


def main():
    with open("input.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    page_size = data["page_size"]
    page_table = data["page_table"]

    expected = {
        0: ("SUCCESS", 80),
        15: ("SUCCESS", 95),
        16: ("SUCCESS", 32),
        37: ("SUCCESS", 117),
        64: ("SUCCESS", 144),
        79: ("SUCCESS", 159),
        48: ("PAGE FAULT", None),
        80: ("INVALID", None)
    }

    print("INDEPENDENT VERIFICATION")
    print("-" * 50)

    all_passed = True

    for address, expected_result in expected.items():
        actual = independent_check(
            address, page_size, page_table
        )

        status = "PASS" if actual == expected_result else "FAIL"

        if status == "FAIL":
            all_passed = False

        print(
            f"Address {address}: {status} | "
            f"Expected: {expected_result} | Actual: {actual}"
        )

    print("-" * 50)
    print("ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED")


if __name__ == "__main__":
    main()