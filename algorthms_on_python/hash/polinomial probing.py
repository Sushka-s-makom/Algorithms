def insert_poly(table, key, value):
    size = len(table)
    h = hash(key) % size

    for i in range(size):
        # Формула: h + i^2
        idx = (h + i ** 2) % size

        if table[idx] is None or table[idx][0] == key:
            table[idx] = (key, value)
            return True

    return False  # Таблица полна


# Использование:
poly_table = [None] * 10
insert_poly(poly_table, "Gemini", "AI")
insert_poly(poly_table, "OpenAI", "GPT")

print(poly_table)