function [L,Coef]=lagrange(X,Y) 

n=length(X);
L=zeros(n);


for i=1:n   
    aux0=setdiff(X,X(i));
    aux=[1 -aux0(1)];
    for j=2:n-1
        aux=conv(aux,[1 -aux0(j)]);
    end
    L(i,:)=aux/polyval(aux,X(i));
end


Coef=Y*L;
end