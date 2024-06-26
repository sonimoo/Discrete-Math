def implication(A, B):
    return not A or B


def print_truth_table():
    print("P Q R | (((P → Q) → (R → Q)) → (R → P)) → (P → Q)")
    print("-" * 45)
    for P in [True, False]:
        for Q in [True, False]:
            for R in [True, False]:

                result = implication(
                            implication(
                                implication(implication(P, Q), implication(R, Q)),
                                implication(R, P)
                            ),
                            implication(P, Q)
                         )
                print(f"{int(P)} {int(Q)} {int(R)} | {int(result)}")


print_truth_table()
