import itertools


def implies(a, b):
    return not a or b


def main():
    # Определение переменных
    variables = ['P', 'Q', 'R']
    combinations = list(itertools.product([False, True], repeat=3))

    # Заголовок таблицы
    headers = ['P', 'Q', 'R', '(P → Q)', '(R → Q)', '((P → Q) → (R → Q))', '(R → P)',
               '(((P→Q)→(R→Q))→(R→P))', 'Result']
    print("".join(f"{h:^20}" for h in headers))
    print("-" * len(headers) * 20)

    # Расчет и вывод результатов
    for P, Q, R in combinations:
        # Вычисление всех частей выражения
        p_implies_q = implies(P, Q)
        r_implies_q = implies(R, Q)
        inner_expression = implies(p_implies_q, r_implies_q)
        r_implies_p = implies(R, P)
        middle_expression = implies(inner_expression, r_implies_p)
        expression_value = implies(middle_expression, implies(P, Q))

        # Вывод строки таблицы
        values = [P, Q, R, p_implies_q, r_implies_q, inner_expression, r_implies_p,
                  middle_expression, expression_value]
        print("".join(f"{str(int(v) if isinstance(v, bool) else v):^20}" for v in values))

main()
