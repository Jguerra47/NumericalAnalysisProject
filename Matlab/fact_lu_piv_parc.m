function [x] = fact_lu_piv_parc(A,b)
    [L,U,P] = fact_lu(A);
    L
    U
    P
    Bn = P*b;
    Bn
    z = sustitucion_progresiva(L,Bn);
    z
    x = sustitucion_regresiva(U,z);
end

function [U,P,L] = partialPivot(U,k,P,L)
    list = U(:,k);
    major = -1;
    pos = -1;
    n = length(U);
    for i = k:1:n
        if(abs(list(i))>major)
            major = abs(list(i));
            pos = i;
        end
    end
    temp = U(k,:);
    U(k,:) = U(pos,:);
    U(pos,:) = temp;
    tempPer = P(k,:);
    P(k,:) = P(pos,:);
    P(pos,:) = tempPer;
    tempL = L(k,:);
    L(k,:) = L(pos,:);
    L(pos,:) = tempL;
end

function [L,U,P] = fact_lu(A)
U = A;
n = length(A);
L = zeros(n);
P = eye(n);
for i = 1 : 1 : n - 1
    [U,P,L] = partialPivot(U,i,P,L);
    for j = i + 1 : 1 : n
        L(j,i) = U(j,i)/U(i,i);
        U(j,:) = U(j,:)-L(j,i)*U(i,:);
    end
end
    L = L + eye(n);
end


