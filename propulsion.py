def calculate_net_thrust(mass_flow, v_exit, v_inlet, p_exit, p_ambient, nozzle_area):
    momentum_thrust = mass_flow * (v_exit - v_inlet)
    pressure_thrust = (p_exit - p_ambient) * nozzle_area
    return momentum_thrust + pressure_thrust

def calculate_sfc(fuel_flow_rate, net_thrust):
    return fuel_flow_rate / net_thrust
