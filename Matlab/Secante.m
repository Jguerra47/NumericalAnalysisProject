format long;

Xo=input('ingrese xo\n');
X1=input('\ningrese x1\n');
Tol=input('\ningrese la tolerancia\n');
Iter=input('\ningrese el número de iteraciones\n');
Fun=input('\ningrese la función entre comillas simples\n');
yo=f(Xo);

if yo==0
    fprintf('xo es raiz\n');
else
    y1=f(X1);
    d=(y1-yo);
    e=Tol+1;
    cont=0;
    Z1= [cont,X1, y1, e];
    Z= [cont,X1, y1, e];
    while y1~=0 & e>Tol & cont<Iter & d~=0
    
        X2= X1-((y1*(X1-Xo))/(d));
        %e=abs((X2-X1)/X2);
        e=abs(X2-X1);
        Xo=X1;
        yo=y1;
        y1=f(X2);
        X1=X2;
        d=(y1-yo);
        cont=cont+1;
        Z(cont,1)=cont;
        Z(cont,2)=X1;
        Z(cont,3)=y1;
        Z(cont,4)=e;
    end

    if y1==0
    fprintf('%g es raíz\n\n',X1);
    else
        if e<Tol
            fprintf( '%g es una aproximacion a una raìz con una tolerancia %g \n',X1,Tol)
        else
            if d==0
                fprintf('el denominador es cero, FRACASO\n\n');
            else
                fprintf('Fracaso en %g iteraciones\n\n',Iter);
            end
        end
    end
end
fprintf('TABLA\n\ninteraciones |  Xn |   y1  |  Error\n');
disp(Z1);
disp(Z);

fplot(f,[-1 15]);

grid on
