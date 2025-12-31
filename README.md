# Loot-Loader

## Overview

**Loot-Loader** is a **market data ingestion, analysis, and execution framework** for equities, designed to operate using **long-term structural context** combined with **short- and mid-term market signals**.

The system supports **automated equity trades at market price** under tightly controlled conditions.

Loot-Loader is published as a **reference implementation**.  
It is **not a turnkey trading product** and is **not runnable without private infrastructure, credentials, and configuration**.

---

## What Loot-Loader Does

- Ingests historical **minute-level and daily market data**
- Computes and stores enriched indicators, including:
  - EMA200 and EMA200 angle
  - Volatility-normalized statistical bands
  - High–Low Equilibrium Value (HLEV) structures
- Maintains a **time-consistent historical database**
- Evaluates symbols using **weighted signal logic**
- Generates explainable BUY / SELL / HOLD decisions
- **Executes equity trades at market price** when all conditions are met
- Logs trades and decision context for later review

---

## Execution Scope

Loot-Loader includes **equity execution logic**, but execution is:

- Limited to **market orders**
- Bound to a **single authenticated account**
- Dependent on **external OAuth2 authentication**
- Governed by **risk and capital constraints**
- Not exposed as a reusable or distributable interface

This repository does **not** provide a “plug-and-play” trading system.

---

## What Loot-Loader Does *Not* Do

- ❌ Execute options, futures, or derivatives
- ❌ Provide multi-account or multi-user support
- ❌ Expose broker credentials or secrets
- ❌ Offer configuration suitable for third-party use
- ❌ Guarantee profitability or performance

---

## Relationship to LLLongTerm

Loot-Loader integrates insights derived from **LLLongTerm**, a separate research module focused on long-horizon market structure.

- **LLLongTerm** answers:  
  *“Where are we in the 20–25 year market structure?”*

- **Loot-Loader** answers:  
  *“Given current conditions, should an equity trade be executed now?”*

The systems are intentionally separated to preserve clarity, safety, and modularity.

---

## Architecture (High Level)

