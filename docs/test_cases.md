@'
# TEST CASES - PAGING ADDRESS TRANSLATION

- **Page Size ($P$):** 16 bytes ($2^4$ bytes)
- **Page Table Entries:** 5 entries (Page 0 to Page 4)
  - Page 0 $\rightarrow$ Frame 5 (`valid = 1`)
  - Page 1 $\rightarrow$ Frame 2 (`valid = 1`)
  - Page 2 $\rightarrow$ Frame 7 (`valid = 1`)
  - Page 3 $\rightarrow$ Frame 1 (`valid = 0` - Invalid / Not in RAM)
  - Page 4 $\rightarrow$ Frame 9 (`valid = 1`)

| Test ID | Category | Logical Address | Page Number | Offset | Expected Result | Actual Result | Status |
|---|---|---:|---:|---:|---|---|---|
| TC01 | Boundary (`LA = 0`, `offset = 0`) | 0 | 0 | 0 | `SUCCESS` (PA = 80) | `SUCCESS` (PA = 80) | PASS |
| TC02 | Boundary (`offset = P - 1`) | 15 | 0 | 15 | `SUCCESS` (PA = 95) | `SUCCESS` (PA = 95) | PASS |
| TC03 | Valid Page 1 (`offset = 0`) | 16 | 1 | 0 | `SUCCESS` (PA = 32) | `SUCCESS` (PA = 32) | PASS |
| TC04 | Valid Page 1 (Normal) | 20 | 1 | 4 | `SUCCESS` (PA = 36) | `SUCCESS` (PA = 36) | PASS |
| TC05 | Valid Page 2 (Prompt Example) | 37 | 2 | 5 | `SUCCESS` (PA = 117) | `SUCCESS` (PA = 117) | PASS |
| TC06 | Invalid Entry (`valid = 0`, `offset = 0`) | 48 | 3 | 0 | `PAGE FAULT` | `PAGE FAULT` | PASS |
| TC07 | Invalid Entry (`valid = 0`) | 50 | 3 | 2 | `PAGE FAULT` | `PAGE FAULT` | PASS |
| TC08 | Valid Page 4 (`offset = 0`) | 64 | 4 | 0 | `SUCCESS` (PA = 144) | `SUCCESS` (PA = 144) | PASS |
| TC09 | Valid Page 4 (`offset = P - 1`) | 79 | 4 | 15 | `SUCCESS` (PA = 159) | `SUCCESS` (PA = 159) | PASS |
| TC10 | Out of Page Table Bounds | 80 | 5 | 0 | `INVALID` | `INVALID` | PASS |
| TC11 | Negative Logical Address | -5 | N/A | N/A | `INVALID` | `INVALID` | PASS |
'@ | Set-Content -Path "test_cases.md" -Encoding UTF8