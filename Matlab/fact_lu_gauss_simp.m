function [x] = fact_lu_gauss_simp(A,b)
    [L,U] = fact_lu(A);
    L
    U
    z = sustitucion_progresiva(L,b);
    z
    x = sustitucion_regresiva(U,z);
end