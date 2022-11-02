
clc
clear
format longG

fprintf('                           METODO ITERATIVO DE JACOBI\n\n\n')

a=input('Ingrese la matriz de coeficientes:\n ');
b=input('\nIngrese los t�rminos independientes:\n ');
x=input('\nIngrese el vector con las aproximacimaciones Iniciales:\n ');
iter=input('\nIngrese el n�mero m�ximo de iteraciones:\n ');
tol=input('\nIngrese la tolerancia:\n ');


cond=norm(a)*norm(a^-1);
disp('condicional=')
disp(cond)

determinante=det(a);
if determinante==0
disp('El determinante es cero, el problema no tiene soluci�n �nica')
return
end

n=length(b);
d=diag(diag(a));
l=d-tril(a);
u=d-triu(a);
fprintf('\n     SOLUCION:\n')
fprintf('\nLa matriz de transicion de jacobi:\n')
T=d^-1*(l+u);
disp(T)
re=max(abs(eig(T)))

if re>1
disp('Radio Espectral mayor que 1')
disp('el m�todo no converge')
return
end
fprintf('\nEl vector constante es::\n')
C=d^-1*b;
disp(C)
i=1;
err=tol+1;
z=["n","x1","x2","x3","Error"];

aux = [i,x(1),x(2),x(3),err];
z = [z;aux];

while err>tol & i<iter

  xi=T*x+C;
%disp(xi)
err=norm(xi-x);
%err=max(abs(xi-x));
%err=norm(xi-x)/norm(xi);
x=xi;

i=i+1;
aux = [i,x(1),x(2),x(3),err];
z = [z;aux];

end
disp(z)

fprintf('Vector solucion\n')
disp(x)


