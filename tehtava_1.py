import numpy as np

# Tehtävät 1.1

# 1. Muunna asteiksi
a = 2.493
b = 0.911
print(np.degrees(a))
print(np.degrees(b))

# 2. Muunna radiaaneiksi
c = 137.7
d = 62.3
print(np.radians(c))
print(np.radians(d))

# 3. Laadi taulukko, josta esittää seuraavat kulmat radiaaneina
e = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
for i in e:
    print(np.radians(i))

# Tehtävät 2.2.1
# 1. Suorakulmaisen kolmion kateetit ovat 1,6 m ja 2,3 m. Kuinka pitkä on hypotenuusa?
f = 1.6
g = 2.3
h = np.hypot(f, g)
print(f"Hypotenuusan pituus on {h} metriä")