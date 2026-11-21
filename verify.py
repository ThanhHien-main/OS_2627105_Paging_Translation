import json
import math


def bitwise_oracle(logical_address, page_size, page_table):
    """
    Independent verification using bitwise operations (shift & mask)
    instead of integer division/modulo logic used in main.py.
    """
    if logical_address < 0:
        return ("INVALID", None)

    offset_bits = int(math.log2(page_size))
    offset_mask = (1 << offset_bits) - 1

    page_idx = logical_address >> offset_bits
    offset_val = logical_address & offset_mask

    if page_idx >= len(page_table):
        return ("INVALID", None)

    if page_table[page_idx]["valid"] != 1:
        return ("PAGE FAULT", None)

    frame_val = page_table[page_idx]["frame"]
    physical_addr = (frame_val << offset_bits) | offset_val
    return ("SUCCESS", physical_addr)


def main():
    with open("input.json", "r", encoding="utf-8") as f:
        input_data = json.load(f)

    with open("results/output.json", "r", encoding="utf-8") as f:
        actual_results = json.load(f)

    page_size = input_data["page_size"]
    page_table = input_data["page_table"]
    actual_map = {
        item["logical_address"]: (item["status"], item["physical_address"])
        for item in actual_results
    }

    print("INDEPENDENT VERIFICATION (BITWISE ORACLE vs MAIN.PY OUTPUT)")
    print("-" * 72)

    all_passed = True
    for addr in input_data["logical_addresses"]:
        expected = bitwise_oracle(addr, page_size, page_table)
        actual = actual_map.get(addr, ("MISSING", None))
        passed = (expected == actual)
        if not passed:
            all_passed = False

        status_str = "PASS" if passed else "FAIL"
        print(
            f"LA = {addr:>3} | {status_str:<4} | "
            f"Expected (Bitwise): {str(expected):<22} | Actual (main.py): {actual}"
        )

    print("-" * 72)
    print("RESULT: ALL 11 TEST CASES PASSED" if all_passed else "RESULT: VERIFICATION FAILED")


if __name__ == "__main__":
    main()