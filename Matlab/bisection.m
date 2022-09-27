function [answer,A]= bisection(f,left,right,tol,niter)
format longG
fRight=f(right);
fLeft=f(left);
A=["counter","left","right","xmid","fmid","error"];
if(fRight==0)
    answer= right+' is a root';
elseif(fLeft==0)
    answer= right+' is a root';
elseif(fLeft*fRight<0)
    mid = (left+right)/2;
    fmid = f(mid);
    counter = 1;
    error = tol+1;
    while(error>tol && fmid~=0 && counter<niter)
        B= [counter,left,right,mid,fmid,error];
        A=[A;B];
        if(fLeft*fmid<0)
            right=mid;
            fRight=fmid;
        else
            left=mid;
            fLeft=fmid;
        end
        xAux=mid;
        mid=(right+left)/2;
        fmid=f(mid);
        error =abs(mid-xAux);
        counter=counter+1;
    end
    B= [counter,left,right,mid,fmid,error];
    A=[A;B];
    if(fmid==0)
        answer = mid+ " is a root";
    elseif(error<tol)
        answer= mid+" is an approach with tolerance "+tol;
    else
        answer = "The method failed in "+niter+" iterations";
    end
end
