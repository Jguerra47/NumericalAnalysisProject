function [answer,matrix]= trisection(f,left,right,tolerance,niter)

fRight = f(right);
fLeft= f(left);
matrix=["iteration","left","right","xmid1","xmid2","f(xmid1)","f(xmid2)","error1","error2"];
if(fRight==0)
    answer = right+" is a root";
elseif(fLeft==0)
    answer=left+" is a root";
elseif(fLeft*fRight<0)
    xmid1=left+(right-left)/3;
    xmid2= right-(right-left)/3;
    fXmid1=f(xmid1);
    fXmid2=f(xmid2);
    counter=1;
    error1=tolerance+1;
    error2=tolerance+1;
    while(error1>tolerance  && error2>tolerance && fXmid1~=0 && fXmid2~=0 && counter<niter)
        B= [counter,left,right,xmid1,xmid2,fXmid1,fXmid2,error1,error2];
        matrix=[matrix;B];
        if(fLeft*fXmid1<0)
            right=xmid1;
            fRight=fXmid1;
        elseif(fXmid1*fXmid2<0)
            left=xmid1;
            fLeft=fXmid1;
            right=xmid2;
            fRight=fXmid2;
        else
            left=xmid2;
            fLeft=fXmid2;
        end
        xAux1=xmid1;
        xAux2=xmid2;
        xmid1=left+(right-left)/3;
        xmid2= right-(right-left)/3;
        fXmid1=f(xmid1);
        fXmid2=f(xmid2);
        error1=abs(xmid1-xAux1);
        error2=abs(xmid2-xAux2);
        counter=counter+1;
    end
    B= [counter,left,right,xmid1,xmid2,fXmid1,fXmid2,error1,error2];
    matrix=[matrix;B];
    if(fXmid1==0)
        answer=xmid1+" is a root";
    elseif(fXmid2==0)
        answer=xmid2+" is a root";
    elseif(error1<tolerance)
        answer =xmid1+" is an approximation with tolerance "+tolerance;
    elseif(error2<tolerance)
        answer=xmid2+" is an approximation with tolerance "+tolerance;
    else
        answer="The method fails in "+niter+" iterations";
    end
else
    answer="bad range";
end