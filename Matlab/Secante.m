function Secante(f,X0,X1,Tol,Iter)

format long;

yo=f(Xo);

if yo==0
    fprintf('xo is a root\n');
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
    fprintf('%g is a root\n\n',X1);
    else
        if e<Tol
            fprintf( '%g is an approximation to a root with a tolerance %g \n',X1,Tol)
        else
            if d==0
                fprintf('denominator is zero, FAILURE\n\n');
            else
                fprintf('Failure in %g iterations\n\n',Iter);
            end
        end
    end
end
fprintf('\nIterations |  Xn |   y1  |  Error\n');
disp(Z1);
disp(Z);

fplot(f,[-1 15]);

grid on
