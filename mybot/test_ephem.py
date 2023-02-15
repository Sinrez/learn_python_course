import ephem
import datetime
# python3 test_ephem.py

# mars = ephem.Mars('2000/01/01')
# const = ephem.constellation(mars)
# print(const)

today = datetime.datetime.now()
planet = getattr(ephem, 'Mars')(today.strftime('%Y/%m/%d'))
# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-getattr/
ephem_answer = ephem.constellation(planet)
print(*ephem_answer)
print(ephem_answer[1])