def impl(a, b):
    return not a or b


def and_op(a, b):
    return a and b


headers = ['P', 'Q', 'R', '(Q∧R)', '(P→(Q∧R))', '(R→Q)', '(P∧(R→Q))', '((P→(Q∧R))→(P∧(R→Q)))']
print("".join(f"{h:^10}" for h in headers))
print("-" * len("".join(f"{h:^10}" for h in headers)))

for P in [False, True]:
    for Q in [False, True]:
        for R in [False, True]:

            q_and_r = and_op(Q, R)
            p_impl_q_and_r = impl(P, q_and_r)
            r_impl_q = impl(R, Q)
            p_and_r_impl_q = and_op(P, r_impl_q)
            result = impl(p_impl_q_and_r, p_and_r_impl_q)

            values = [P, Q, R, q_and_r, p_impl_q_and_r, r_impl_q, p_and_r_impl_q, result]
            print("".join(f"{str(int(v) if isinstance(v, bool) else v):^10}" for v in values))
