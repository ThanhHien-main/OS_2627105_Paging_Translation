import json
import os


def load_input(filename):
    """Read input data from JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def translate_address(logical_address, page_size, page_table):
    """Translate logical address into physical address."""

    trace = []

    # Step 1: Split page number and offset
    page_number = logical_address // page_size
    offset = logical_address % page_size

    trace.append(f"Step 1: Logical Address = {logical_address}")
    trace.append(f"        Page Number = {page_number}")
    trace.append(f"        Offset = {offset}")

    # Step 2: Check page number
    if page_number < 0 or page_number >= len(page_table):
        trace.append("Step 2: INVALID - Page number is outside page table")
        return {
            "logical_address": logical_address,
            "status": "INVALID",
            "physical_address": None,
            "trace": trace
        }

    trace.append(f"Step 2: Page {page_number} exists in page table")

    # Step 3: Check valid/invalid bit
    entry = page_table[page_number]

    if entry["valid"] == 0:
        trace.append("Step 3: PAGE FAULT - Invalid page")
        return {
            "logical_address": logical_address,
            "status": "PAGE FAULT",
            "physical_address": None,
            "trace": trace
        }

    trace.append("Step 3: Valid bit = 1")

    # Step 4: Get frame number
    frame_number = entry["frame"]
    trace.append(f"Step 4: Frame Number = {frame_number}")

    # Step 5: Calculate physical address
    physical_address = frame_number * page_size + offset
    trace.append(
        f"Step 5: PA = {frame_number} * {page_size} + {offset} = {physical_address}"
    )

    # Step 6: Return result
    trace.append(f"Step 6: SUCCESS - Physical Address = {physical_address}")

    return {
        "logical_address": logical_address,
        "status": "SUCCESS",
        "page_number": page_number,
        "offset": offset,
        "frame_number": frame_number,
        "physical_address": physical_address,
        "trace": trace
    }


def main():
    data = load_input("input.json")

    page_size = data["page_size"]
    page_table = data["page_table"]
    logical_addresses = data["logical_addresses"]

    if page_size <= 0:
        raise ValueError("Page size must be positive")

    results = []

    print("=" * 55)
    print("PAGING ADDRESS TRANSLATION SIMULATOR")
    print("=" * 55)

    for address in logical_addresses:
        result = translate_address(address, page_size, page_table)
        results.append(result)

        print(f"\nLogical Address: {address}")
        print(f"Status: {result['status']}")

        if result["physical_address"] is not None:
            print(f"Physical Address: {result['physical_address']}")

        print("\nTRACE:")
        for step in result["trace"]:
            print(step)

    os.makedirs("results", exist_ok=True)

    with open("results/output.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    print("\n" + "=" * 55)
    print("Results saved to results/output.json")
    print("=" * 55)


if __name__ == "__main__":
    main()