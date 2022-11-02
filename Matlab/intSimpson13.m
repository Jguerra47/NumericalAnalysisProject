    function [A] = intSimpson13(a,b,n,f)
    f = inline(f);
    deltaX = (b-a)/n;
    A = 0;
    
    %Test if n is par
    iterations = [];
    for i=0:1:n
        xi = a + i*deltaX;
        fxi = f(xi);
        if( i > 0 && i<n)
            if(mod(i,2) == 0 )
                fxi = 2 * fxi;
            else
                fxi = 4 * fxi;
            end
        end
        A = A + fxi;
        iterations = [iterations;[(i+1),xi,fxi,A]];
    end
    disp('    Counter    Xi         Fxi     A');
    disp(iterations);
    A = A * (deltaX/3);
    A
    
    end
