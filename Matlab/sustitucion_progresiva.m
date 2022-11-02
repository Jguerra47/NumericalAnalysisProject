function [x] = sustitucion_progresiva(L,b)
n = length(b);
x = zeros(n,1);
x(1) = b(1)/L(1,1);
for i=2:1:n
    temp = 0;
    for j=1:1:i-1
        temp = temp + L(i,j)*x(j);
    end
    x(i) = (b(i)-temp)/L(i,i);
end
end 