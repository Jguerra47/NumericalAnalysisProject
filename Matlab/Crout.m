function [x,L,U]=Crout(A,b)

n=size(A,1);
L=eye(n); 
U=eye(n);

for i=1:n-1
    for j=i:n
        L(j,i)=A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)');
    end
    for j=i+1:n
        U(i,j)=(A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)'))/L(i,i);
        if(U(i,j)==-0.2324)
            disp(L(i,1:i-1))
            disp(U(1:i-1,j)')
    end
end
L(n,n)=A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)');

z=sustprgr([L b]);
x=sustregr([U z]);        
end