# Windowed-Sinc FIR Filter Design Skill

Exact linear-phase Finite Impulse Response (FIR) digital filter synthesis utilizing the windowed sinc method with Hamming window attenuation.

```mermaid
flowchart LR
    Params["Cutoff Frequency & Tap Count N"] --> Sinc["Sample Ideal Sinc Kernel h[n] = sin(2π f_c n) / π n"]
    Params --> Window["Compute Hamming Window w[n]"]
    Sinc --> Multiply["Tapering: h_w[n] = h[n] * w[n]"]
    Window --> Multiply
    Multiply --> Normalized["Normalized Linear-Phase Filter Kernel"]
```

## Features
- **100% Python Standard Library**: Analytical trigonometric kernel generation.
- **Strict Linear Phase**: Constant group delay across all passband frequencies.
