# Order Service Refactor Workspace

This repository simulates a simplified but realistic legacy order service used in an enterprise environment.

---

## Context

The service is currently in production and supports:
- Order pricing
- Tax calculation
- Early-stage discount logic (incomplete)

---

## Known Engineering Issues

- Discount system is incomplete and not fully tested
- Limited unit test coverage
- Business logic spread across modules
- No validation layer for inputs
- Feature flags are hardcoded in application logic

---

## Engineering Priorities

Teams have requested:

1. Implement missing discount logic
2. Increase test coverage for pricing and discounts
3. Improve separation of concerns
4. Ensure safe refactoring without breaking existing behavior
5. Prepare system for future pricing rule expansion

---

## Why this repo exists

We are evaluating whether an AI engineering agent (Devin) can:

- Work safely inside an existing codebase
- Extend incomplete features
- Add meaningful test coverage
- Refactor without breaking behavior
- Operate like a senior engineer, not a code generator
