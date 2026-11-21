# TEST CASES - PAGING ADDRESS TRANSLATION

Page Size = 16 bytes

| Test | Logical Address | Page Number | Offset | Expected Result |
|---|---:|---:|---:|---|
| TC01 | 0 | 0 | 0 | SUCCESS - PA = 80 |
| TC02 | 15 | 0 | 15 | SUCCESS - PA = 95 |
| TC03 | 16 | 1 | 0 | SUCCESS - PA = 32 |
| TC04 | 37 | 2 | 5 | SUCCESS - PA = 117 |
| TC05 | 64 | 4 | 0 | SUCCESS - PA = 144 |
| TC06 | 79 | 4 | 15 | SUCCESS - PA = 159 |
| TC07 | 48 | 3 | 0 | PAGE FAULT |
| TC08 | 80 | 5 | 0 | INVALID |

## Test Results

- TC01: PASS
- TC02: PASS
- TC03: PASS
- TC04: PASS
- TC05: PASS
- TC06: PASS
- TC07: PASS
- TC08: PASS

## Conclusion

The test cases cover valid address translation,
invalid page number, and page fault conditions.