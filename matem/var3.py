def impl(a, b):
    return not a or b


headers = ['P', 'Q', 'R', '(P → Q)', '(R → Q)', '((P → Q) → (R → Q))', '(R → P)',
           '(((P→Q)→(R→Q))→(R→P))', 'Result']
print("".join(f"{h:^20}" for h in headers))
print("-" * 180)

for P in [False, True]:
    for Q in [False, True]:
        for R in [False, True]:

            p_impl_q = impl(P, Q)
            r_impl_q = impl(R, Q)
            bracket1 = impl(p_impl_q, r_impl_q)
            r_impl_p = impl(R, P)
            bracket2 = impl(bracket1, r_impl_p)
            bracket3 = impl(bracket2, impl(P, Q))

            values = [P, Q, R, p_impl_q, r_impl_q, bracket1, r_impl_p,
                      bracket2, bracket3]
            print("".join(f"{str(int(v) if isinstance(v, bool) else v):^20}" for v in values))


