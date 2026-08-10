# Invoice Total Calculator

A simple Python script that calculates the total invoice amount, including VAT, from a list of service fees.

## How it works
- Takes a list of service fees and sums them for the subtotal
- Applies a VAT rate to the subtotal
- Returns the final total (subtotal + VAT)

## How to run
```bash
python invoice_calculator.py
```
The script uses a sample set of services (consulting, support, hosting) and a 20% VAT rate. Edit the `services` and `vat` variables to test different values.

## What I learned
- Writing a reusable function with parameters (`service_fees`, `vat_rate`)
- Using Python's built-in `sum()` on a list
- Formatting currency output with f-strings (`:.2f`)
