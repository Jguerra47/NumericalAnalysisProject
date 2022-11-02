function Coef=trazlin(X,Y)


n=length(X);
m=2*(n-1);
A=zeros(m); 
b=zeros(m,1);
Coef=zeros(n-1,2);


for i=1:length(X)-1
    A(i+1,[2*i-1 2*i])=[X(i+1) 1];
    b(i+1)=Y(i+1);
end
A(1,[1 2])=[X(1) 1];
b(1)=Y(1);

for i=2:length(X)-1
    A(length(X)-1+i,2*i-3:2*i)=[X(i) 1 -X(i) -1];
    b(length(X)-1+i)=0;
end   


Saux=A\b;

for i=1:length(X)-1
    Coef(i,:)=Saux([2*i-1 2*i]);
end
end