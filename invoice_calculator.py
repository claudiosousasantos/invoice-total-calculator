def calculate_invoice_total(service_fees, vat_rate):
    subtotal = sum(service_fees)
    total = subtotal + (subtotal * vat_rate)
    return total

# Example: services billed to a client
services = [150.00, 89.90, 45.00]  # e.g., consulting, support, hosting fees
vat = 0.20  # 20% VAT

invoice_total = calculate_invoice_total(services, vat)
print(f"The total invoice amount (including VAT) is: ${invoice_total:.2f}")