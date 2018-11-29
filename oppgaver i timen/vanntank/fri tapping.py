import math  # vi trenger dette biblioteket senere


def euler(h, dh, dt):
    '''Regner ut ny høyde i tanken vet tiden t+dt,
    gitt høyden og stigningstallet dh ved tiden t.'''
    return h + dh * dt


def stigning(A_h, A_t, h):
    '''Regner ut stigningen i punktet h.
    Parameteren k er en global konstant.'''
    return -(A_h / A_t) * k * math.sqrt(h)


def hastighet(h):
    '''Regner ut hastigheten til væskestrømmen ut av tanken
    når væskehøyden er h. Parameteren k er en global konstant.'''
    if h > 0.0:
        return k * math.sqrt(h)
    else:
        return 0.0


A_t = 2.00  # Tankens tverrsnittareal (m^2)
A_h = 0.002  # Hullets tverrsnittareal (m^2)
h = 4.00  # Vannivået når forsøket starter (m)
g = 9.81

V0 = A_t * h
print("Volumet ved tiden t = 0 s er {} m^3".format(V0))

C = 1
k = C * math.sqrt(2 * g)
print("Konstanten k er {}".format(k))
