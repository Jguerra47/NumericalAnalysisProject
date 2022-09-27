function [x] = gausTotalPivot(A,b,n)
    [m,marks] = upperTriangular(A,b,n);
    xPrev = sustitution(m,n);
    x = order(xPrev,marks);
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

function [m,posColumn] = totalPivot(m,n,k)
    major = -1;
    posRow = -1;
    posColumn = -1;

    for i = k:1:n
        for j = k:1:n
            if(abs(m(i,j))>major)
                major = abs(m(i,j));
                posRow = i;
                posColumn = j;
            end
        end
    end

    if(posRow ~= k)
        temp = m(k,:);
        m(k,:) = m(posRow,:);
        m(posRow,:) = temp;
    end

    if(posColumn ~= k)
        temp = m(:,k);
        m(:,k) = m(:,posColumn);
        m(:,posColumn) = temp;
    end
end

function [marks] = generateMark(n)
    marks = rand(1,n);
    for i = 1:1:n
        marks(i) = i;
    end
end

function [x] = order(xPrev,marks)
    x = rand(1,length(xPrev));
    for i=1:1:length(marks)
        x(marks(i)) = xPrev(i);
    end
end

function [m,marks] = upperTriangular(A,b,n)   
    m = [A b];
    [marks] = generateMark(n);
    disp('Stage 0')
    disp(m)
    
    for i = 1:1:n-1
        [m,posColumn] = totalPivot(m,n,i);

        markAux = marks(i);
        marks(i) = marks(posColumn);
        marks(posColumn) = markAux;

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