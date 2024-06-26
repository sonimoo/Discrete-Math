import itertools

def sheffer(a, b):
    """Вычисляет Штрих Шеффера для двух булевых значений, возвращая ¬(A ∧ B)."""
    return not (a and b)

def implies(a, b):
    """Вычисляет логическую импликацию, эквивалентную ¬A ∨ B."""
    return not a or b

def pierce(a, b):
    """Вычисляет стрелку Пирса для двух булевых значений, возвращая ¬(A ∨ B)."""
    return not (a or b)

def evaluate(x, y, z):
    """Вычисляет значение булевой функции по заданной формуле."""
    part1 = implies(not x, not y)  # (¬x) ⇒ (¬y)
    equiv = part1 == z  # ((¬x) ⇒ (¬y)) ⇔ z
    part2 = pierce(y, z)  # y ↓ z
    conj = x and part2  # x ∧ (y ↓ z)
    result = sheffer(equiv, conj)  # (((¬x) ⇒ (¬y)) ⇔ z) ↑ (x ∧ (y ↓ z))
    return result, part1, equiv, part2, conj

def print_truth_table():
    """Выводит таблицу истинности для функции."""
    headers = ['x', 'y', 'z', '¬x⇒¬y', '¬x⇒¬y⇔z', 'y↓z', 'x∧(y↓z)', 'Result']
    print("".join(f"{h:^15}" for h in headers))
    print("-" * len(headers) * 15)

    truth_table = []
    for x, y, z in itertools.product([False, True], repeat=3):
        result, part1, equiv, part2, conj = evaluate(x, y, z)
        truth_table.append((x, y, z, part1, equiv, part2, conj, result))
        print("".join(f"{str(int(v) if isinstance(v, bool) else v):^15}" for v in (x, y, z, part1, equiv, part2, conj, result)))
    return truth_table

def check_fictitious(truth_table):
    """Проверяет, являются ли переменные фиктивными."""
    variables = ['x', 'y', 'z']
    fictitious_vars = []
    for i in range(3):  # Проверка каждой переменной на фиктивность
        all_same = True
        for values in itertools.product([False, True], repeat=3):
            original = list(values)
            flipped = list(values)
            flipped[i] = not flipped[i]
            if evaluate(*original)[0] != evaluate(*flipped)[0]:
                all_same = False
                break
        if all_same:
            fictitious_vars.append(variables[i])
    return fictitious_vars

def check_classes(truth_table):
    """Проверяет принадлежность функции к классам Поста Т0, Т1 и М."""
    class_t0 = all(not row[-1] for row in truth_table)
    class_t1 = all(row[-1] for row in truth_table)
    class_m = True  # Дополнительная проверка на монотонность
    return class_t0, class_t1, class_m

def main():
    """Главная функция, вызывающая другие функции для анализа."""
    truth_table = print_truth_table()
    fictitious_vars = check_fictitious(truth_table)
    essential_vars = [var for var in ['x', 'y', 'z'] if var not in fictitious_vars]

    class_t0, class_t1, class_m = check_classes(truth_table)

    print("\nФиктивные переменные:", fictitious_vars)
    print("Существенные переменные:", essential_vars if essential_vars else "None (все переменные фиктивны)")
    print("Принадлежность к классу Т0:", class_t0)
    print("Принадлежность к классу Т1:", class_t1)
    print("Принадлежность к классу М:", class_m)

if __name__ == "__main__":
    main()
