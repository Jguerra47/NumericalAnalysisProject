l=input('Para trabajar con puntos presione 1, Para trabajar con una funcion presione 2: ') 
if l==1
    disp('Este programa calcula un polinomio que aproxima n puntos');
    n=input('Para cuántos puntos desea aproximar?  ');
    cont=1;
    A=zeros(n,n);
    while cont<n+1
        A(cont,1)=1;
        cont=cont+1;
    end 
    cont=1;
    while cont<=n
        fprintf('Punto número'); disp(cont)        
        A(cont,2)=input('Ingrese la componente X: ');
        Y(cont,1)=input('Ingrese la componente Y: ');
        cont=cont+1;
    end
    cont=1;
    while cont<n+1
          cont2=3;
          while cont2<=n
                A(cont,cont2)=(A(cont,2))^(cont2-1);
                cont2=cont2+1;
          end
          cont=cont+1;
    end
    AI=inv(A);
    R=AI*Y;
     syms x
 Px=0
 cont=0;
 while cont<n
     Ux=R(cont+1)*x^(cont)
     Px=Px+Ux 
     cont=cont+1     
 end
 ezplot(Px)
 title('Función Aproximada') 
 
end
%  .............................................................................................
if l==2
 disp('Este programa calcula un polinomio que aproxima una funcion');
syms x
y=input(' Escriba la funcion de X a aproximar ')
Ini=input('Ingrese el minimo valor de X: ')
Sep=input('Ingrese la separacion entre los valores de X: ')
Fin=input('Ingrese el máximo valor que tomará X: ')
Dom=[Ini:Sep:Fin];
n=length(Dom);
A=zeros(n,n);
cont=1
while cont<n+1
        A(cont,1)=1;
        cont=cont+1;
end 
    
 cont=1;
    while cont<=n
        fprintf('Punto número'); disp(cont)        
        A(cont,2)=Dom(cont);
        x=Dom(cont);
        Y(cont,1)=eval(y)
        cont=cont+1;
    end
 cont=1
    while cont<n+1
          cont2=3;
          while cont2<=n
                A(cont,cont2)=(A(cont,2))^(cont2-1);
                cont2=cont2+1;
          end
          cont=cont+1;
    end
 R=inv(A)*Y
 syms x
 Px=0
 cont=0;
 while cont<n
     Ux=R(cont+1)*x^(cont)
     Px=Px+Ux 
     cont=cont+1     
 end
 subplot(2,1,1)
 ezplot(y, [Ini Fin])
 title('Función a Aproximar')
 subplot(2,1,2)
 ezplot(Px,[Ini Fin])
 title('Función Aproximada') 
end




