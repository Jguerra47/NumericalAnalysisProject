function [] = muller(f,x0,x1,tolerance,nMax)
    
    fx0 = f(x0);
    fx1 = f(x1);
    x2 = (x0+x1)/2;
    fx2 = f(x2);
    
    h0 = x1 - x0;
    h1 = x2 - x1;
    delta0 = (fx1 -fx0) / h0;
    delta1 = (fx2 -fx1) / h1;

    a = (delta1 - delta0) / (h1 - h0);
    b = a * h1 + delta1;
    c =fx2;

    xi = x2 + (-2*c) / (b+(b / abs(b))* sqrt(b^2-4*a*c));
    fxi = f(xi);
    error = tolerance + 1;
    counter = 0;
    matrix = ["Counter","xi","Fxi","Error"];
    matrix = [matrix;[counter,xi,fxi,error]];


    while(fx1 ~= 0 && error > tolerance && counter < nMax)
        x2Aux = x2;
        x1Aux = x1;
        x2 = xi;
        x1 = x2Aux;
        x0 = x1Aux;
        fx0 = f(x0);
        fx1 = f(x1);
        fx2 = f(x2);

        h0 = x1 - x0;
        h1 = x2 - x1;
        delta0 = (fx1 -fx0) / h0;
        delta1 = (fx2 -fx1) / h1; 

        a = (delta1 - delta0) / (h1 - h0);
        b = a * (h1) + delta1;
        c = fx2;

        xi = x2 + (-2*c) / (b+(b / abs(b))* sqrt(b^2-4*a*c));
        fxi = f(xi);
        error = abs(xi-x2);
        counter = counter + 1;
        matrix = [matrix;[counter,xi,fxi,error]];
    end
    disp(matrix)

    if fxi == 0 
        disp(['The root has been found and it is: ', num2str(xi,12)])
    elseif error <= tolerance
        disp(['An approximation has been found and is: ', num2str(xi,12)])
    else 
        disp('The method fails with the maximum number of iterations given')
    end

end