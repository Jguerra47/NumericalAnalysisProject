function [A] = intSimpson38(a,b,n,f)
f = inline(f);
deltaX = (b-a)/n;
A = 0;
iterations = [];
for i=0:1:n
    xi = a + i*deltaX;
    fxi = f(xi);
    if( i > 0 && i<n)
        if(mod(i,3) == 0 )
            fxi = 2 * fxi;
        else
            fxi = 3 * fxi;
        end
    end
    A = A + fxi;
    iterations = [iterations;[(i+1),xi,fxi,A]];
end
disp('    Counter    Xi         Fxi     A');
disp(iterations);
A = A * (3*deltaX/8);
A
end