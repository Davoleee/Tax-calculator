TAX_BRACKETS = {
    0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)],  # Single
    1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)],  # Married Joint
    2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)],  # Married Separate
    3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]   # Head of Household
}

STATUS_LABELS = {
    0: "Single",
    1: "Married Filing Jointly or Qualifying Widow(er)",
    2: "Married Filing Separately",
    3: "Head of Household"
}

def compute_tax(status: int, income: float) -> float:
    """Compute tax based on filing status and income."""
    if status not in TAX_BRACKETS:
        raise ValueError("Invalid filing status.")
    if income < 0:
        raise ValueError("Income cannot be negative.")

    tax = 0.0
    prev_limit = 0
    for limit, rate in TAX_BRACKETS[status]:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            break
    return tax

def main():
    print("=== 2009 Federal Income Tax Calculator ===")
    for k, v in STATUS_LABELS.items():
        print(f"{k} - {v}")

    try:
        status = int(input("Enter filing status (0-3): "))
        income = float(input("Enter taxable income: "))
        tax = compute_tax(status, income)
        print(f"\nFiling Status: {STATUS_LABELS[status]}")
        print(f"Taxable Income: ${income:,.2f}")
        print(f"Calculated Tax: ${tax:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
