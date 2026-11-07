# Manning's Equation Solver Using the Newton–Raphson Method

## 1. Project Overview

This project presents a Python-based numerical solver for calculating the normal water depth in trapezoidal open channels using Manning's equation and the Newton–Raphson iterative method.

The program determines the unknown water depth for a given discharge, channel geometry, bed slope, and hydraulic roughness.

## 2. Project Objectives

- Calculate water depth in trapezoidal open channels.
- Apply Manning's equation to calculate discharge.
- Implement the Newton–Raphson method to solve nonlinear equations.
- Determine hydraulic roughness using different input parameters.
- Evaluate numerical convergence using relative discharge error.

## 3. Mathematical Formulation

### 3.1. Trapezoidal Channel Geometry

**Cross-sectional area:**

```text
A = h * (b + m * h)
```

**Wetted perimeter:**

```text
P = b + 2 * h * sqrt(m^2 + 1)
```

**Hydraulic radius:**

```text
Rh = A / P
```

### 3.2. Manning's Equation

```text
Q = (1/n) * A * Rh^(2/3) * sqrt(S)
```

Alternatively, using the Strickler coefficient:

```text
Q = kst * A * Rh^(2/3) * sqrt(S)
```

### 3.3. Roughness Conversion

The program accepts three possible roughness inputs:

- Manning coefficient (n)
- Strickler coefficient (kst)
- Sediment diameter (D90)

The relationship used for sediment diameter is:

```text
kst = 26 / D90^(1/6)
```

The relationship between Manning and Strickler coefficients is:

```text
n = 1 / kst
```

### 3.4. Newton–Raphson Method

The nonlinear objective function is:

```text
F(h) = n * Q * P^(2/3) - A^(5/3) * sqrt(S)
```

**Geometrical derivatives:**

```text
dA/dh = b + 2 * m * h
```

```text
dP/dh = 2 * sqrt(m^2 + 1)
```

**Derivative of the objective function:**

```text
F'(h) = (2/3) * n * Q * P^(-1/3) * dP/dh
        - (5/3) * A^(2/3) * sqrt(S) * dA/dh
```

**Newton–Raphson iteration:**

```text
h_new = h_old - F(h_old) / F'(h_old)
```

**Relative discharge error:**

```text
epsilon = abs(Q - Qk) / Q
```

The iteration continues until the relative discharge error reaches the prescribed tolerance.

## 4. Input Parameters

| Parameter | Description | Unit |
|---|---|---|
| Q | Discharge | m3/s |
| b | Bottom channel width | m |
| m_bank | Channel side slope (H:V) | - |
| S | Channel bed slope | - |
| D90 | Sediment diameter | m |
| kst | Strickler coefficient | m^(1/3)/s |
| n | Manning roughness coefficient | s/m^(1/3) |
| h_initial | Initial water depth | m |

## 5. Numerical Algorithm

1. Read the hydraulic input parameters.
2. Determine the roughness coefficient.
3. Assume an initial water depth.
4. Calculate the flow area and wetted perimeter.
5. Calculate discharge using Manning's equation.
6. Evaluate the objective function and its derivative.
7. Update water depth using Newton–Raphson.
8. Calculate the relative discharge error.
9. Repeat until convergence or the maximum iteration limit is reached.
10. Return the calculated water depth and discharge error.

## 6. Example Application

The following hydraulic parameters are used in the example:

| Parameter | Value |
|---|---:|
| Discharge (Q) | 10.5 m3/s |
| Bottom width (b) | 5.0 m |
| Side slope (m_bank) | 2.5 |
| Bed slope (S) | 0.005 |
| Sediment diameter (D90) | 0.08 m |

The program calculates the corresponding normal water depth using the Newton–Raphson method.

## 7. Project Files

- `README.md`: Project description and mathematical background.
- `Manning_Newton_Raphson_Report.pdf`: Detailed mathematical formulation, algorithm, flowchart and numerical example.

## 8. Requirements

- Python 3.12 or newer.
- Standard Python math library.
- PyCharm or another Python IDE.

No external Python packages are required.

## 9. How to Run

1. Download or clone the repository.
2. Open the project in PyCharm.
3. Select a suitable Python interpreter.
4. Run `manning_solver.py`.
5. Review the calculated water depth and relative discharge error.

## 10. Documentation

For further mathematical details, numerical formulations, the Newton–Raphson flowchart and numerical example, see:

[Manning Newton–Raphson Technical Report](Manning_Newton_Raphson_Report.pdf)

## 11. Author

**Davood Azan**

Computational Hydraulics | Open-Channel Flow | Numerical Methods

## 12. License

This project is intended for educational and engineering research purposes.