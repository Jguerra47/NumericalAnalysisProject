function Coef=difdivididas(X,Y)

n=length(X);
D=zeros(n);


D(:,1)=Y';
for i=2:n
    aux0=D(i-1:n,i-1);
    aux=diff(aux0);
    aux2=X(i:n)-X(1:n-i+1);
    D(i:n,i)=aux./aux2';
end


Coef=diag(D)';
end