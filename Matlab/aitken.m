
function aitken(f,x0,tolerance,nMax)
    fxi = f(x0);
    if fxi == 0
        disp(['A root was found: ', num2str(x0,12)])
    else
        matrix = ["counter","xi","fxi","error"];
        matrix = [matrix;[1,x0,fxi,2]];
        x1 = f(x0);
        error = abs(x1-x0);
        fxi = f(x1);
        matrix = [matrix;[2,x1,fxi,error]];
        x2 = f(x1);
        error = abs(x2-x1);
        fxi = f(x2);
        matrix = [matrix;[3,x2,fxi,error]];
        det = (x2-x1)-(x1-x0);
        counter = 4;
        while(fxi ~= 0 && error > tolerance && counter < nMax && det~=0)
            xi = x2 - ( (x2 - x1)^2 )/det;
            fxi = f(xi);
            det = (x2-x1)-(x1-x0);
            error = abs(xi-x2);
            matrix = [matrix;[counter,xi,fxi,error]];
            x0 = xi;
            x1 = f(x0);
            x2 = f(x1);
            counter = counter + 1;
        end
        
        disp(matrix)

        if fxi == 0 
            disp(['The root has been found and it is: ', num2str(xi,12)])
        elseif error <= tolerance
            disp(['An approximation has been found and is: ', num2str(xi,12)])
        elseif det == 0
            disp('Error during method execution')
        else 
            disp('The method fails with the maximum number of iterations given')
        end
        
    end
end