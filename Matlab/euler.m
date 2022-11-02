function [ yo ] = euler( y )

xo=input('Ingrese el limite inferior del intervalo: ');
xf=input('Ingrese el limite superior del intervalo: ');
yo=input(sprintf('Ingrese el valor inicial de y(%.2f): ',xo));
n=input('Ingrese el numero de puntos: ');
h=(xf-xo)/n;

while xo<=xf
    yo=yo+h*subs(y,xo);
    xo=xo+h;
end
end
