function [answer,matrix]=newton(f,fder,tolerance,x0,niter)
    fx=f(x0);
    dfx= fder(x0);
    matrix=["iteration","xn","f(xn)","f'(xn)","erro"];
    counter=1;
    error = tolerance+1;
    B=[counter,x0,fx,dfx,error];
    matrix=[matrix;B];
    while(error>tolerance && fx~=0 && dfx~=0 && counter<niter)
        x1=x0-(fx/dfx);
        fx=f(x1);
        dfx=fder(x1);
        error=abs(x1-x0);
        x0=x1;
        counter=counter+1;
        B=[counter,x0,fx,dfx,error];
        matrix=[matrix;B];
    end
    if(fx==0)
        answer=x0+" is a root";
    elseif(error<tolerance)
        answer=x1+" is a root approximation with a tolerance of "+tolerance;
    elseif(dfx==0)
        answer=x1+" is a possible multiple root";
    else
        answer="The method failed in "+niter+" iterations"
    end