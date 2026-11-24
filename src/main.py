import json
import os


def load_input(filename):
    """Read input data from JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def translate_address(logical_address, page_size, page_table):
    """Translate logical address into physical address in 6 steps."""
    trace = []

    # Step 1: Split page number and offset
    if logical_address < 0:
        trace.append(f"Step 1: Logical Address = {logical_address} (Negative address)")
        trace.append("Step 2: INVALID - Logical address cannot be negative")
        return {
            "logical_address": logical_address,
            "status": "INVALID",
            "page_number": None,
            "offset": None,
            "frame_number": None,
            "physical_address": None,
            "trace": trace
        }

    page_number = logical_address // page_size
    offset = logical_address % page_size

    trace.append(f"Step 1: Logical Address = {logical_address}")
    trace.append(f"        Page Number = floor({logical_address} / {page_size}) = {page_number}")
    trace.append(f"        Offset = {logical_address} mod {page_size} = {offset}")

    # Step 2: Check page number bounds
    if page_number >= len(page_table):
        trace.append(f"Step 2: INVALID - Page {page_number} is outside page table (valid range: 0..{len(page_table)-1})")
        return {
            "logical_address": logical_address,
            "status": "INVALID",
            "page_number": page_number,
            "offset": offset,
            "frame_number": None,
            "physical_address": None,
            "trace": trace
        }

    trace.append(f"Step 2: Page {page_number} exists in page table")

    # Step 3: Check valid/invalid bit
    entry = page_table[page_number]
    if entry["valid"] == 0:
        trace.append(f"Step 3: PAGE FAULT - Page {page_number} has valid bit = 0")
        return {
            "logical_address": logical_address,
            "status": "PAGE FAULT",
            "page_number": page_number,
            "offset": offset,
            "frame_number": None,
            "physical_address": None,
            "trace": trace
        }

    trace.append("Step 3: Valid bit = 1")

    # Step 4: Get frame number
    frame_number = entry["frame"]
    trace.append(f"Step 4: Frame Number = {frame_number}")

    # Step 5: Calculate physical address
    physical_address = frame_number * page_size + offset
    trace.append(f"Step 5: PA = {frame_number} * {page_size} + {offset} = {physical_address}")

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
    data = load_input("input/input.json")
    page_size = data["page_size"]
    page_table = data["page_table"]
    logical_addresses = data["logical_addresses"]

    if page_size <= 0 or (page_size & (page_size - 1)) != 0:
        raise ValueError("Page size must be a positive power of 2")

    results = []
    trace_lines = [
        "=" * 55,
        "PAGING ADDRESS TRANSLATION SIMULATOR - EXECUTION TRACE",
        f"Page Size (P) = {page_size} bytes | Page Table Entries = {len(page_table)}",
        "=" * 55
    ]

    for address in logical_addresses:
        result = translate_address(address, page_size, page_table)
        results.append(result)

        trace_lines.append(f"\nLogical Address: {address}")
        trace_lines.append(f"Status: {result['status']}")
        if result["physical_address"] is not None:
            trace_lines.append(f"Physical Address: {result['physical_address']}")
        trace_lines.append("TRACE:")
        trace_lines.extend(result["trace"])

    output_text = "\n".join(trace_lines)
    print(output_text)

    os.makedirs("results", exist_ok=True)
    with open("results/output.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    with open("results/trace.txt", "w", encoding="utf-8") as f:
        f.write(output_text + "\n")

    print("\n" + "=" * 55)
    print("Saved results/output.json and results/trace.txt")
    print("=" * 55)


if __name__ == "__main__":
    main()
