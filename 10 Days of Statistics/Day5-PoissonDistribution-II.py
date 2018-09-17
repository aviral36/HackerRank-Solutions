mean_A = 0.88
# operating cost = 160+40X^2
mean_B = 1.55
# operating cost = 128+40Y^2

#in poisson, mean = variance
"""E(operating cost of A) = E(160) + 40*E(X^2)
                          = 160 + 40*(Var(X) + (E(X))^2)
                          = 160 + 40*(mean_A + (mean_A)^2)
    Similarly for B
"""
Expectation_A = 160 + 40*(mean_A + (mean_A)**2)
Expectation_B = 128 + 40*(mean_B + (mean_B)**2)
print(round(Expectation_A,3))
print(round(Expectation_B,3))
