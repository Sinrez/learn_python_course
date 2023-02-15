import ephem
# python3 test_ephem.py

mars = ephem.Mars('2000/01/01')
const = ephem.constellation(mars)
print(const)