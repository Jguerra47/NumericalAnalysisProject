function [x] = gausPartialPivot(A,b,n)
    [m] = upperTriangular(A,b,n);
    [x] = sustitution(m,n);
end

function [x] = sustitution(m,n)
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

function [m] = partialPivot(m,n,k)
    list = m(:,k);
    major = -1;
    pos = -1;
    for i = k:1:n
        if(abs(list(i))>major)
            major = abs(list(i));
            pos = i;
        end
    end
    temp = m(k,:);
    m(k,:) = m(pos,:);
    m(pos,:) = temp;
end

function [m] = upperTriangular(A,b,n)   
    m = [A b];
    disp('Etapa 0')
    disp(m)
    
    for i = 1:1:n-1
        m = partialPivot(m,n,i);
        if (m(1,1)==0)
            disp('Un 0 fue encontrado en la diagonal')
            return 
        end
        for j = i+1:1:n
            if(m(j,i)~=0)
                m(j,:) = m(j,:) - (m(j,i)/m(i,i)).*m(i,:);
            end
        end
        disp(['Etapa ',num2str(i)])
        disp(m)
    end
end