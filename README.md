# PAGING ADDRESS TRANSLATION

## 1. Introduction
This project simulates Paging Address Translation in Operating Systems.

The program converts Logical Addresses into Physical Addresses using a Page Table.

## 2. Technologies
- Programming Language: Python
- Input Format: JSON
- Development Environment: Visual Studio Code

## 3. Project Structure

```text
Paging_Address_Translation/
│
├── main.py
├── verify.py
├── input.json
├── pseudocode.md
├── flowchart.md
├── test_cases.md
├── README.md
└── results/
    └── output.json
```

## 4. How to Run

Requirements:
- Python 3.x

Run the simulation:

```bash
python main.py
```

Run independent verification:

```bash
python verify.py
```

## 5. Main Features

- Split Logical Address into Page Number and Offset.
- Check Page Number validity.
- Check Valid/Invalid bit.
- Retrieve Frame Number.
- Calculate Physical Address.
- Detect INVALID and PAGE FAULT.
- Display execution trace.
- Export results to JSON.

## 6. Physical Address Formula

Physical Address = Frame Number * Page Size + Offset

## 7. Test Cases

The project includes 8 test cases covering:
- Valid address translation.
- Invalid page number.
- Page fault.

## 8. Conclusion

This project demonstrates the Paging Address Translation mechanism and helps understand how the Operating System translates logical addresses into physical addresses.