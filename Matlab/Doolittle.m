function [x,L,U]=Doolittle(A,b)

n=size(A,1);
L=eye(n); 
U=eye(n);

for i=1:n-1
    for j=i:n
        U(i,j)=A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)');
    end
    for j=i+1:n
        L(j,i)=(A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)'))/U(i,i);
    end
end
U(n,n)=A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)');

z=sustprgr([L b]);
disp(z);
x=sustregr([U z]);     
end