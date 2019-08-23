# t Tiempo
# v Velocidad
# ev Error de la Velocidad
# et Error del Tiempo
t=5;
v=4;
ev=0.1;
et=0.1;
dist=v*t;
vi=v-ev;
ti=t-et;
print('V\tT\tD\tEa\tEr')
while vi<=v+ev:
  d=round(vi*ti,2)
  ea=round(abs(d-dist),2)
  er=round(ea/dist*100,2)
  print(repr(vi).rjust(3), repr(ti).rjust(4), repr(d).rjust(8), repr(ea).ljust(4,'0'), repr(er).ljust(4,'0'))
  ti+=et
  if ti>t+et:
    ti=t-et
    vi+=ev
