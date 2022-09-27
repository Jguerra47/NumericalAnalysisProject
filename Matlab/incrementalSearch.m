function [answer,matrix] = incrementalSearch(f,x0,delta,niter)
fx0 =f(x0);
matrix=["iteration","x0","x1","fx0","fx1","fx0*fx1"];
if(fx0==0)
    answer=x0+" is a root";
else
    x1=x0+delta;
    counter=1;
    fx1=f(x1);
    while(fx0*fx1>0 && counter<niter)
        B=[counter,x0,x1,fx0,fx1,fx0*fx1];
        matrix=[matrix;B];
        x0=x1;
        fx0=fx1;
        x1=x0+delta;
        fx1=f(x1);
        counter=counter+1;
    end
    B=[counter,x0,x1,fx0,fx1,fx0*fx1];
    matrix=[matrix;B];
    if(fx1==0)
        answer=x1+" is a root";
    elseif(fx0*fx1<0)
        answer="There is at least one root between "+x0+" and "+x1;
    else
        answer="The method failed in "+niter+" iterations";
    end
end
