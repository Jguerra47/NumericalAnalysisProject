function [answer, matrix] = fixedpoint(f,g,x0,tol,niter)
    matrix=["iteration","xn","f(xn)","error"];
    fx=f(x0);
    counter=0;
    error=tol+1;
    B=[counter,x0,fx,error];
    matrix=[matrix;B];
    while(fx~=0 && error > tol && counter < niter)
        x1=g(x0);
        fx=f(x1);
        error=abs(x1-x0);
        x0=x1;
        counter=counter+1;
        B=[counter,x0,fx,error];
        matrix=[matrix;B];
    end

    if(fx==0)
        answer=x0+" is a root\n\n";
    elseif(error < tol)
        answer=x0+" is an approximation to a root with a tolerance "+tol;
    else
        answer="The method failed at "+niter+" iteration";
    end