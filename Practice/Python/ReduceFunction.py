from fractions import gcd
def product(fracs):
    nume=1
    deno=1
    for i in range(len(fracs)):
        nume=nume*fracs[i].numerator
        deno=deno*fracs[i].denominator
    k=reduce(gcd, [nume,deno])
    nume=nume/k
    deno=deno/k
    t=Fraction(nume, deno)
    return t.numerator, t.denominator
