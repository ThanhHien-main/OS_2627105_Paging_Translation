@'
# PAGING ADDRESS TRANSLATION

## 1. Introduction
This project simulates single-level **Paging Address Translation** in Operating Systems, converting Logical Addresses into Physical Addresses using a fixed page size ($P = 16$ bytes) and a valid/invalid bit check.

## 2. Project Structure
```text
OS_2627105_Paging_Translation/
|-- main.py             # Main 6-step address translation simulator
|-- verify.py           # Independent bitwise verification against main.py output
|-- input.json          # Page size, page table, and 11 test logical addresses
|-- pseudocode.md       # 6-step translation algorithm pseudocode
|-- flowchart.md        # Mermaid flowchart diagram
|-- test_cases.md       # Full test matrix (Expected vs Actual)
|-- README.md           # Documentation & reproduction guide
`-- results/
    |-- output.json     # Structured JSON translation output & trace
    `-- trace.txt       # Plain-text step-by-step execution trace