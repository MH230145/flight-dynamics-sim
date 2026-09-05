import numpy as np

def calculate_lift_coefficient(alpha_deg, cl_alpha=0.1):
    """Calcula el coeficiente de sustentacion (CL) en régimen subsónico."""
    alpha_rad = np.radians(alpha_deg)
    return cl_alpha * alpha_deg

def prandtl_glauert_correction(cl_0, mach):
    """Aplica la corrección de compresibilidad de Prandtl-Glauert para evitar la divergencia cerca del Mach crítico."""
    if mach >= 1.0:
        raise ValueError("El modelo de Prandtl-Glauert solo es válido para Mach subsónico (M < 1.0).")
    beta = np.sqrt(1 - mach**2)
    return cl_0 / beta

if __name__ == "__main__":
    cl_inc = calculate_lift_coefficient(5)
    mach_test = 0.6
    cl_comp = prandtl_glauert_correction(cl_inc, mach_test)
    print(f"CL incompresible a 5 grados: {cl_inc}")
    print(f"CL corregido por Prandtl-Glauert (M={mach_test}): {cl_comp:.4f}")