import numpy as np

def calculate_lift_coefficient(alpha_deg, cl_alpha=0.1):
    """Calcula el coeficiente de sustentacion (CL) en régimen subsónico."""
    alpha_rad = np.radians(alpha_deg)
    return cl_alpha * alpha_deg

if __name__ == "__main__":
    print(f"CL a 5 grados: {calculate_lift_coefficient(5)}")
