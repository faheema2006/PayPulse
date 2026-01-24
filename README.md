# PayPulse – Digital Payment Failure Intelligence

PayPulse is an end-to-end analytics project that detects, analyzes, and visualizes digital payment failures using Python and Power BI.

## Project Structure
- generate_transactions.py → Generates synthetic transaction data
- features.py → KPI generation (bank, mode, city)
- analysis.py → Analysis logic
- data/ → Generated CSV datasets
- PayPulse_Dashboard.pbix → Power BI dashboard

## Tech Stack
- Python 3.11
- Pandas
- Power BI

## Key Insights
- Failure rate by payment mode
- Peak failure hours
- Bank and city risk analysis
- Failure reasons and financial impact

## How to Run
1. Run `generate_transactions.py`
2. Run `features.py`
3. Refresh Power BI dashboard
