# Título: Cálculo Hipoteca
# Autor: Jaime Sepúlveda
# [Bootcamp Data Science - Coding Dojo]

TITULO = " Cálculo de Pago Hipoteca "
p = 400000
r = 3 / 100
n = 360

v1 = (r * (1 + r) ** n)
v2 = (1 + r) ** n - 1
v3 = (v1 / v2)
pmensual = p * v3

print("\n\n")
print(TITULO.center(50, "="))
print(f"Capital       US$    :  {p:,.2f}")
print(f"Tasa                 :  {r}")
print(f"Nro de Cuota Mensual :  {n}")
print(f"Pago Mensual  US$    :  {pmensual:,.2f}")
print ("=" * 50)
print("\n\n")