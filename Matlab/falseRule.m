function falseRule(f,Xi,Xs,Tol,Iter)
format long;

Yi=f(Xi); 
Ys=f(Xs); 

if Yi==0 
    fprintf('Xi is root\n'); 
else
    if Ys==0 
        fprintf('Xs is root\n');
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
                fprintf('%g is a root\n\n',Xm);
            else
                if Error<Tol
                    fprintf( '%g is an approximation to a root with a tolerance %g \n\n',Xm,Tol);
                else
                    fprintf('Failure in %g iterations\n\n',Iter);
                end
            end
            fprintf('\nIterations | Xi |  Xs | Xm | Ym | Error\n');
            disp(Z);
        else
            fprintf('The interval is inadequate\n\n');
        end
    end
end


ezplot(f);
grid on

