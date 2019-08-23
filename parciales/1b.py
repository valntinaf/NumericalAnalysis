import matplotlib.pyplot as plt

def sumaElementos(x, n):
  suma=0
  sumas=[]
  for i in range(n):
    for j in range(n):
      suma+=x[i][j]
      sumas.append(suma)
      print(suma)
  plt.plot(sumas)
  plt.ylabel('Suma')
  plt.show()

A=[[3,4,5],[1,9,12],[1,9,2]]
sumaElementos(A,3) 