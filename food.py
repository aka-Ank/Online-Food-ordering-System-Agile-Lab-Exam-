def total(p, d=0):
    if p < 0 or not 0 <= d <= 100:
        raise ValueError("invalid price or discount")
    return round(p * (1 - d / 100), 2)



