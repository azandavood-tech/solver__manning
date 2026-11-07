
import math as m

def interpolate_h(Q, b, m_bank, S, **kwargs):
    # Get Manning's roughness coefficient
    for key, value in kwargs.items():

        if key == "D90":
            k_st = 26 / value ** (1 / 6)
            n_m = 1 / k_st

        elif key == "k_st":
            n_m = 1 / value
            k_st=value

        elif key == "n_m":
            n_m = value
            k_st=1/n_m
        else:
            raise ValueError(f"Unknown parameter: {key}")

    # Initial values
    h = kwargs.get("h_initial", 1.0)
    eps = 1.0
    iteration = 0

    # Newton-Raphson iteration
    while eps > 10 ** -3:
        if iteration > 100:
            print(f"Maximum number of iterations: {iteration}")
            break

        # Wetted area and wetted perimeter
        A = h * (b + h * m_bank)
        P = b + 2 * h * m.sqrt(m_bank ** 2 + 1)

        # Calculate discharge
        Qk = A ** (5 / 3) * m.sqrt(S) / (n_m * P ** (2 / 3))

        # Calculate relative error
        eps = abs(Q - Qk) / Q

        # Derivatives of A and P
        dA_dh = b + 2 * m_bank * h
        dP_dh = 2 * m.sqrt(m_bank ** 2 + 1)

        # Objective function
        F = n_m * Q * P ** (2 / 3) - A ** (5 / 3) * m.sqrt(S)

        # Derivative of objective function
        dF_dh = (
            (2 / 3) * n_m * Q * P ** (-1 / 3) * dP_dh
            - (5 / 3) * A ** (2 / 3) * m.sqrt(S) * dA_dh
        )

        # Avoid division by zero
        if abs(dF_dh) < 1e-12:
            print("Warning: Derivative is too small.")
            break

        # Update water depth
        h = abs(h - F / dF_dh)

        iteration += 1

    return h, eps, Qk, k_st


if __name__ == '__main__':
    # Input parameters
    Q = 10.5        # discharge in (m3/s)
    b = 5.0         # bottom channel width (m)
    m_bank = 2.5    # bank slope
    #k_st0 = 20.0       # Strickler value
    #n_m = .05  # Manning's n
    D90=.08
    S_0 = 0.005     # channel slope

    # Call the solver with positional S argument passed correctly
    h_n, eps, Qk,k_st = interpolate_h(Q, b, m_bank, S_0, D90=D90)

    #h_n, eps, Qk,k_st = interpolate_h(Q, b, m_bank, S_0, k_st=k_st0)
    print(f"kst: {k_st:.2f}")
    print(f"Calculated water depth h: {h_n:.3f} m")
    print(f"Discharge Qk: {Qk:.4f} m3/s with error: {eps:.5f}")
