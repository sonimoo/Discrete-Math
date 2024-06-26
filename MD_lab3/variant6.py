def sheffer(a, b):
    """Вычисляет Штрих Шеффера для двух булевых значений."""
    return not (a and b)

def evaluate(x, y, z):
    """Вычисляет значение функции
    все разбито на действия и вычисляется поэтапно"""
    neg_x = not x #1 действие это отрицание Х
    neg_z = not z
    sheffer_neg_x_y = sheffer(neg_x, y) #3 действие отрицание Х штрих шеффера У
    #аналочно следующие
    neg_sheffer_neg_x_y = not sheffer_neg_x_y
    y_and_neg_z = y and neg_z
    sheffer_x_y = sheffer(x, y)
    or_y_neg_z_sheffer_x_y = y_and_neg_z or sheffer_x_y
    result = not neg_sheffer_neg_x_y or or_y_neg_z_sheffer_x_y
    return result, neg_x, sheffer_neg_x_y, neg_sheffer_neg_x_y, neg_z, y_and_neg_z, sheffer_x_y, or_y_neg_z_sheffer_x_y

def print_truth_table():
    """функция для вывода данных в виде визуальной таблицы"""
    headers = ['x', 'y', 'z', '¬x', '(¬x↑y)', '¬((¬x)↑y)', '¬z', '(y∧¬z)', '(x↑y)', '(y¬z)∨(x↑y)', 'Result']
    print("".join(f"{h:^10}" for h in headers))
    print("-" * 165)

    truth_table = []
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                result, neg_x, sheffer_neg_x_y, neg_sheffer_neg_x_y, neg_z, y_and_neg_z, sheffer_x_y, or_y_neg_z_sheffer_x_y = evaluate(x, y, z)
                row = (x, y, z, neg_x, sheffer_neg_x_y, neg_sheffer_neg_x_y, neg_z, y_and_neg_z, sheffer_x_y, or_y_neg_z_sheffer_x_y, result)
                truth_table.append(row)
                print("".join(f"{int(v):^10}" for v in row))
    return truth_table

def check_fictitious(truth_table):
    """Проверяет, являются ли переменные фиктивными."""
    variables = ['x', 'y', 'z']
    fictitious_vars = []
    for i in range(3):  # проверяет x, y, z
        changes_result = set()
        for row in truth_table:
            flipped_row = list(row)
            flipped_row[i] = not flipped_row[i]
            flipped_result = evaluate(*flipped_row[:3])[0]
            if flipped_result != row[-1]:
                changes_result.add(True)
        if not changes_result:
            fictitious_vars.append(variables[i])
    return fictitious_vars

def check_classes(truth_table):
    """Проверяет принадлежность функции к классам Т0, Т1 и М."""
    class_t0 = all(row[-1] == False for row in truth_table if all(v == False for v in row[:3]))
    class_t1 = all(row[-1] == True for row in truth_table if all(v == True for v in row[:3]))
    class_m = True
    return class_t0, class_t1, class_m

def main():
    truth_table = print_truth_table()
    fictitious_vars = check_fictitious(truth_table)
    class_t0, class_t1, class_m = check_classes(truth_table)

    essential_vars = [var for var in ['x', 'y', 'z'] if var not in fictitious_vars]

    print("\nФиктивные переменные:", fictitious_vars)
    print("Существенные переменные:", essential_vars if essential_vars else "None (все переменные фиктивны)")
    print("Принадлежность к классу Т0:", class_t0)
    print("Принадлежность к классу Т1:", class_t1)
    print("Принадлежность к классу М:", class_m)

if __name__ == "__main__":
    main()
