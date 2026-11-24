ALGORITHM: PAGING ADDRESS TRANSLATION

INPUT:
    page_size
    page_table
    logical_address

OUTPUT:
    physical_address OR ERROR MESSAGE

BEGIN
    // Step 1: Split logical address
    page_number = logical_address DIV page_size
    offset = logical_address MOD page_size

    // Step 2: Check page number
    IF page_number < 0 OR page_number >= LENGTH(page_table) THEN
        RETURN "INVALID"

    // Step 3: Check valid/invalid bit
    IF page_table[page_number].valid == 0 THEN
        RETURN "PAGE FAULT"

    // Step 4: Get frame number
    frame_number = page_table[page_number].frame

    // Step 5: Calculate physical address
    physical_address = frame_number * page_size + offset

    // Step 6: Return result
    RETURN physical_address

END