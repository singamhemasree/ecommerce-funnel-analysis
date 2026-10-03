# E-Commerce Funnel Analysis

*Question:* Where do users drop off between viewing a product and buying it, and what should the product team test first?

## Key findings (Dec 2019, cosmetics store)
- 358K users viewed products, 83K added to cart (23.3%), 26K purchased (7.2% overall).
- Cart-to-purchase is about 35% for items under $20 but falls to 29.7% for items priced $50+.

## Recommendation
Show EMI options, delivery estimate and return policy on the cart page for $50+ items.

## How to test it
- Success metric: cart-to-purchase rate for $50+ items
- Guardrail metric: revenue per user
- Caveat: smaller sample in the $50+ band (3,776 cart users)

## Tools
SQL (DuckDB), Python (Plotly), Power BI

## Files
- dashboard/dashboard.pbix - Power BI dashboard
- funnel.py, price_band.py, export.py - analysis scripts
