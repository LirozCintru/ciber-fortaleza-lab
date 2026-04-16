def check_temp(t):
    """
    Certifica que la temperatura de almacenamiento sea óptima (2°C a 8°C).
    """
    if t < 2 or t > 8:
        return False
    return True
