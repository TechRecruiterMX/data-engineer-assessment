# Data Engineer Technical Assessment

## Overview

This repository contains a technical assessment designed to evaluate Data Engineering skills across:

- SQL
- Advanced SQL concepts
- Python programming
- Data manipulation
- Data pipeline concepts
- Data warehouse fundamentals

The goal of this assessment is to understand your approach to solving real-world data engineering problems, including data quality, transformations, scalability, and reliability.

---

# Assessment Structure

The assessment contains three main sections:

## 1. SQL Assessment

Location:

```
sql/
```

This section evaluates your ability to work with relational data.

Topics covered:

- SQL queries
- Joins
- Aggregations
- Common Table Expressions (CTEs)
- Window Functions
- Ranking
- Running totals
- Analytical queries


Complete your answers in:

```
sql/answers.sql
```

---

# 2. Python Data Engineering Assessment

Location:

```
python/
```

This section evaluates Python skills used in real Data Engineering workflows.

The challenge focuses on building parts of a data processing pipeline.

Topics covered:

- Data ingestion
- Handling malformed data
- Data validation
- Data transformation
- Deduplication strategies
- Late-arriving data handling
- Time-based processing
- Streaming concepts
- Memory-aware processing


Complete the implementation in:

```
python/challenge.py
```

---

## Running Tests

Install dependencies:

```bash
pip install pytest
```

Run the Python tests:

```bash
python -m pytest python/test_challenge.py -v
```

Your implementation should pass all provided tests.

---

# 3. Data Warehouse Design Assessment

Location:

```
warehouse/
```

This section evaluates your understanding of designing scalable analytical systems.

Topics covered:

- Fact tables
- Dimension tables
- Data modeling
- Grain definition
- Slowly Changing Dimensions
- Incremental data loading
- Data quality
- Scalability considerations


Complete your answers in:

```
warehouse/design.md
```

---

# General Instructions

- Do not modify function names or signatures.
- Keep your code clean and readable.
- Handle edge cases appropriately.
- Add comments when assumptions are made.
- Explain your reasoning when appropriate.
- You may use documentation or references.

The goal is not only correctness, but understanding your engineering decisions.

---

# Expected Evaluation Areas

| Area | Focus |
|---|---|
| SQL | Querying, analytics, window functions |
| Python | Data processing, pipeline logic, code quality |
| Data Engineering | Scalability, reliability, architecture |
| Warehouse Design | Modeling and analytical systems |

---

# Submission

Before submitting:

Ensure the following files are completed:

```
sql/answers.sql

python/challenge.py

warehouse/design.md
```

Commit your changes and share the repository.

Be prepared to discuss:

- Your implementation choices
- Tradeoffs
- Scaling considerations
- Production design decisions

---

Good luck!
