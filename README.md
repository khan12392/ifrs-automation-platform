# IFRS Automation Platform

A modular Python platform that automates IFRS/IAS calculations, schedules, 
and journal entries — designed for finance teams that want to reduce manual 
effort, improve accuracy, and free up time for professional judgment.

Built with real UAE-listed company data (EMSTEEL, DFM, ADNOC Distribution, Depa PLC).

---

## 🎯 Purpose

Finance professionals spend significant time on repetitive IFRS calculations 
that follow fixed rules. This platform automates the calculation, schedule 
generation, and journal-entry preparation — while keeping professional 
judgment with the accountant.

**Goal:** Replace 20 hours of monthly manual IFRS work with 20 minutes of automation.

---

## 🏗️ Architecture

```
                    IFRS AUTOMATION PLATFORM
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    MODULE A              MODULE B              MODULE C
    GROUP REPORTING       FIN. INSTRUMENTS      ASSETS & LIABILITIES
    • IFRS 10             • IFRS 9              • IFRS 16
    • IFRS 3              • IFRS 13             • IAS 16
    • IAS 28              • IFRS 7              • IAS 38
    • IAS 21                                    • IAS 36
    • IFRS 12                                   • IAS 37
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                    MODULE D — PERFORMANCE
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    • IFRS 15             • IAS 12              • IAS 19
    • IFRS 2              • IAS 33              • IAS 23
                              │
                    JOURNAL ENTRY ENGINE
                              │
                    POWER BI CFO DASHBOARD
                              │
                    CONSOLIDATED FINANCIAL STATEMENTS
                              │
                             CFO
```

---

## 📊 Standards Coverage

| Module | Standards | Status |
|--------|-----------|--------|
| **A — Group Reporting** | IFRS 10, IFRS 3, IAS 28, IAS 21, IFRS 12 | 🚧 In Progress |
| **B — Financial Instruments** | IFRS 9, IFRS 13, IFRS 7 | ⏳ Planned |
| **C — Assets & Liabilities** | IFRS 16, IAS 16, IAS 38, IAS 36, IAS 37 | 🚧 In Progress |
| **D — Performance** | IFRS 15, IFRS 2, IAS 12, IAS 19, IAS 23, IAS 33 | ⏳ Planned |
| **E — Reporting** | IAS 1 / IFRS 18, Power BI | ⏳ Planned |

---

## 🛠️ Tools Used

- **Python** — pandas, numpy, openpyxl, matplotlib
- **SQL** — Data storage and querying
- **Power BI** — CFO dashboards
- **Git & GitHub** — Version control
- **AI/ML** — Document extraction, anomaly detection (Phase 5)

---

## 📁 Project Structure

```
ifrs-automation-platform/
├── src/                        # Python modules
│   ├── core/                   # Utilities & journal engine
│   ├── group_reporting/        # IFRS 10, IFRS 3, IAS 28, IAS 21
│   ├── financial_instruments/  # IFRS 9, IFRS 13, IFRS 7
│   ├── assets_liabilities/     # IFRS 16, IAS 16, IAS 38, IAS 36, IAS 37
│   ├── performance/            # IFRS 15, IFRS 2, IAS 12, IAS 19, IAS 23, IAS 33
│   ├── journal_engine/         # Auto journal entries
│   └── reporting/              # IFRS 18 / presentation
├── data/                       # Input data (CSV / Excel)
├── output/                     # Generated schedules & journal entries
├── dashboards/                 # Power BI dashboards
├── notebooks/                  # Jupyter demos
├── tests/                      # Unit tests
└── docs/                       # Documentation
```

---

## 🚀 Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| **Phase 1** | IFRS 16, IAS 16, IAS 21 | 🚧 In Progress |
| **Phase 2** | IFRS 10, IAS 28, IFRS 3 | ⏳ Planned |
| **Phase 3** | IFRS 9, IFRS 15, IAS 12, IAS 36 | ⏳ Planned |
| **Phase 4** | Power BI dashboard + Journal Engine | ⏳ Planned |
| **Phase 5** | AI document extraction + finance agent | ⏳ Planned |

---

## 💡 Example Workflow

```
INPUT (CSV / Excel)
    ↓
IFRS MODULE (e.g. ifrs16_leases.py)
    ↓
CALCULATIONS (Lease Liability + ROU Asset)
    ↓
JOURNAL ENTRIES (Auto-generated, balanced)
    ↓
CONSOLIDATED OUTPUT (P&L, BS, CF)
    ↓
POWER BI DASHBOARD (CFO view)
```

---

## 🎓 Skills Demonstrated

- **IFRS Knowledge** — IFRS 10, 9, 15, 16, IAS 36, 12, 21, 28, 16, 38, 37
- **Financial Analytics** — DCF, NPV, ratios, variance analysis
- **Data Analytics** — pandas, SQL, data cleaning, aggregation
- **AI Engineering** — Document extraction, anomaly detection, finance agents
- **Automation** — Python, journal entry engine
- **Reporting** — Power BI, Excel, audit-ready schedules

---

## 👤 Author

**Fahad Ali** — Senior Financial Analyst | IFRS Diploma (UK) | 
Power BI, Python, SQL | AI-Driven Finance Automation

- **LinkedIn:** [linkedin.com/in/fahad-ali-88b0351a2](https://www.linkedin.com/in/fahad-ali-88b0351a2)
- **GitHub:** [github.com/khan12392](https://github.com/khan12392)

---

## 📄 License

MIT — free to use, modify, and distribute.
