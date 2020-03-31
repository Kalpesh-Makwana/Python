def rebase(base_a, digits, base_b):
    if base_a < 2 or base_b < 2:
        raise ValueError("Bases must be at least 2")

    if not all(0 <= i < base_a for i in digits):
        raise ValueError('All digits must be between 0 and "base_a"')

    number = sum(base_a ** i * n for i, n in enumerate(digits[::-1]))

    result = []
    while number:
        number, digit = divmod(number, base_b)
        result.append(digit)

    return result[::-1]
