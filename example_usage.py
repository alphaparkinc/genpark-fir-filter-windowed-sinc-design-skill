"""Example designing FIR filter."""
from client import FIRFilterDesign

def main():
    coeffs = FIRFilterDesign.design_lowpass(num_taps=11, cutoff_ratio=0.25)
    print("FIR Coefficients (11-tap):", coeffs)

if __name__ == "__main__":
    main()
