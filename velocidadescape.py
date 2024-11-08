import math

g_m2s = 9.8
r_km = 3600

r_m = r_km*1000

v_escape = math.sqrt(2*g_m2s*r_m)

print(f"Velocidad de escape: {round(v_escape,1)}m/s")


