
format long;

Xi=input ('\nIngrese el limite inferior: ');
Xs=input ('\nIngrese el limite superior: ');
Tol=input ('\nIngrese la tolerancia: ');
Iter=input ('\nIngrese iteraciones: ');
Fun=input ('\nIngrese la función: ');

Yi=f(Xi); 
Ys=f(Xs); 

if Yi==0 
    fprintf('Xi es raiz\n'); 
else
    if Ys==0 
        fprintf('Xs es raiz\n'); 
    else
        if Yi*Ys<0 
            Xm=(Xi)-((f(Xi)*(Xi-Xs))/(f(Xi)-f(Xs)));
            Ym=f(Xm); 
            Error=Tol+1; 
            Cont=1;
            Z=[Cont,Xi,Xs,Xm,Ym,Error];
            while Ym~=0 & Error>Tol & Cont<Iter 
            
                if Yi*Ym<0
                    Xs=Xm;
                    Ys=Ym;
                else
                    Xi=Xm;
                    Yi=Ym;
                end
                    Xaux=Xm;
                    Xm=(Xi)-((f(Xi)*(Xi-Xs))/(f(Xi)-f(Xs)));
                    Ym=f(Xm);
                    Error=abs(Xm-Xaux)/Xm;
                    Cont=Cont+1;
                    Z(Cont,1)=Cont;
                    Z(Cont,2)=Xi;
                    Z(Cont,3)=Xs;
                    Z(Cont,4)=Xm;
                    Z(Cont,5)=Ym;
                    Z(Cont,6)=Error;
            end
            if Ym==0
                fprintf('%g es raíz\n\n',Xm);
            else
                if Error<Tol
                    fprintf( '%g es una aproximacion a una raìz con una tolerancia %g \n\n',Xm,Tol);
                else
                    fprintf('Fracaso en %g iteraciones\n\n',Iter);
                end
            end
            fprintf('TABLA\n\nIteraciones | Xi |  Xs | Xm | Ym | Error\n');
            disp(Z);
        else
            fprintf('El intervalo es inadecuado\n\n');
        end
    end
end


ezplot(f);
grid on

