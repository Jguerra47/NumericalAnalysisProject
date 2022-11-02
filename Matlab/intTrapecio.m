function [A] = intTrapeze(a,b,f,n)
f = inline(f);
deltaX = (b-a)/n;
A = 0;
iterations = [];
for i = 0:1:n
    xi = a + i*deltaX;
    fxi = f(xi);
    if( i > 0 && i<n)
        fxi = 2 * fxi;
    end
    fxi
    A = A + fxi;
    iterations = [iterations;[(i+1),xi,fxi,A]];
end
disp('    Counter    Xi         Fxi     A');
disp(iterations);
A = A * (deltaX/2);
A
end