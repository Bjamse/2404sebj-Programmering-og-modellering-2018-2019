A_t = 2.00   # Tankens tverrsnittareal (m^2)
h = 4.00     # Vannivået når forsøket starter (m)
q_ut = -0.05 # Væskestrøm ut (m^3/s)

V0 = A_t * h
print("Volumet ved tiden t = 0 s er {} m^3".format(V0))

t = 0  # telleverk for tiden vi simulerer over
dt = 5 # tidsskrittet for simuleringen
V = V0 # initialbetingelse
while V > 0:
    V = q_ut * t + V0
    print("V({}) = {}".format(t, V))
    t += dt