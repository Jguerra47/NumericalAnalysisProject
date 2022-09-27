
function [x] = simpleGaus(A,b,n)
    format longG
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

function [m] = upperTriangular(A,b,n)
    m = [A b];
    for i = 1:1:n-1
        if (m(1,1)==0)
            disp('A 0 was found on the diagonal')
            return 
        end
        for j = i+1:1:n
            if(m(j,i)~=0)
                m(j,:) = m(j,:) - (m(j,i)/m(i,i)).*m(i,:);
            end
        end
        disp(['Stage ',num2str(i)])
        disp(m)
    end
end