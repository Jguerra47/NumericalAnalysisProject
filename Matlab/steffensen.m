function [ans,matrix] = steffensen(f,p0,tol,niter)
count = 0;
error = tol + 1;
matrix = et["iteration","p","error"];
b=[count,p0,""];
matrix=[matrix;b];
while(count < niter && error > tol) 
    p1 = f(p0);
    p2 = f(p1);
    p = p0-(p1-p0)^2/(p2-2*p1+p0);
    error = abs(p-p0);
    p0 = p; 
    count = count+1;
    b = [count,p0,error];
    matrix = [matrix;b];
end
if(f(p0) == 0)
    ans = p0+" is a root";
elseif error < tol
    ans = p0+" is an approximation with tolerance "+tol;
else 
    ans = 'failed to converge in 1000 iterations.';
end
