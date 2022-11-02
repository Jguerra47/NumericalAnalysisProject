
clc
clear
format long


fprintf('                           METODO ITERATIVO DE GAUSS SEIDEL CON RELAJACION\n\n\n');

a=input('Ingrese la matriz de coeficientes:\n ');
b=input('\nIngrese los t�rminos independientes:\n ');
x=input('\nIngrese el vector con las aproximacimaciones Iniciales:\n ');
iter=input('\nIngrese el n�mero m�ximo de iteraciones:\n ');
tol=input('\nIngrese la tolerancia:\n ');
w=input('\nIngrese el landa de la relajacion:\n ');

k=norm(a)*norm(a^-1);%
disp('condicional=')
disp(k)
determinante=det(a);
if determinante==0
disp('El determinante es cero, el problema no tiene soluci�n �nica')
end

n=length(b);
d=diag(diag(a));
l=d-tril(a);
u=d-triu(a);
fprintf('\n     SOLUCION:\n')
fprintf('\nLa matriz de transicion de gauss seidel:\n')
Tw=((d-w*l)^-1)*((1-w)*d+w*u);
disp(Tw)
re=max(abs(eig(T)))

if re>1
disp('Radio Espectral mayor que 1')
disp('el m�todo no converge')

return
end
fprintf('\nEl vector constante es::\n')
Cw=w*(d-w*l)^-1*b;
disp(Cw)
i=0;

err=tol+1;
z=[i,x(1),x(2),x(3),err];

while err>tol & i<iter
  
xi=Tw*x+Cw;

err=max(sqrt((xi(1)-x(1))^2+(xi(2)-x(2))^2+(xi(3)-x(3))^2));
%err=norm(Xmejor-x);
%err=max(abs(xi-x));
%err=norm(xi-x)/norm(xi);
x=xi;

i=i+1;
z(i,1)=i; 
z(i,2)=x(1); 
z(i,3)=x(2); 
z(i,4)=x(3);
z(i,5)=err;
end
fprintf('\nTABLA:\n\n    n                  x1                  x2                  x3                 Error\n\n   ') 
disp(z)