function [x] = sustitution_regresiva(A,b)
    m = [A b];
    n = length(A);
    x = zeros(1,n);
    x(n) = m(n,n+1)/m(n,n);
    for i = n-1:-1:1
        summation = 0;
        for j = i+1:1:n
            summation = summation + m(i,j)*x(j);
        end
        x(i) = (m(i,j+1) - summation)/m(i,i);
    end
end