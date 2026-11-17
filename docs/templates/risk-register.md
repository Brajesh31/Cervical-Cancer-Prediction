# Research risk register

| ID | Risk | Impact | Evidence / trigger | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| R-01 | Target leakage from diagnosis features | High | Feature timing unclear | Define timepoint; audit features | [ ] | Open |
| R-02 | Missing sentinel misread | Medium | '?' may remain a string | Parse explicitly; report aggregate counts | [ ] | Open |
| R-03 | Sensitive output exposed | High | Saved tables or plots | Inspect and clear outputs | [ ] | Open |
| R-04 | Poor reproducibility | Medium | Unpinned deps / unseeded split | Record environment and seeds | [ ] | Open |
| R-05 | Medical overclaim | High | Result described as diagnosis or early detection | Safety review and careful language | [ ] | Open |
| R-06 | Dataset provenance uncertain | Medium | No checksum or transformation log | Verify source and lineage | [ ] | Open |

Add risks only with evidence or a clearly identified uncertainty.
