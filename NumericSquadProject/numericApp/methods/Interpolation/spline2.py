import numericApp.methods.Interpolation.totalPivoting as totalPivoting


def spline2Ans(xn,fxn):
    inequality =[]
    
    def createInequality():
        for i in range(0,len(xn)-1):
            if(i < len(xn)):
                inequality.append(((xn[i],fxn[i]),(xn[i+1],fxn[i+1])))
        
    createInequality() 
        
    def spline2():
        superMatrix = [[0 for x in range(3*len(inequality)+1)] for y in range(3*len(inequality))] 
        n = len(superMatrix)
        j = 0
        z = 0
        for i in inequality:
            superMatrix[j][z] = i[0][0]**2
            superMatrix[j][z+1] = i[0][0]
            superMatrix[j][z+2] = 1
            superMatrix[j][n] = i[0][1]
            superMatrix[j+1][z] = i[1][0]**2
            superMatrix[j+1][z+1] = i[1][0]
            superMatrix[j+1][z+2] = 1
            superMatrix[j+1][n] = i[1][1]
            z += 3
            j += 2
        k = j
        z = 0
        for i in range(0,len(inequality)-1):
            superMatrix[k][z] = 2*inequality[i][1][0]
            superMatrix[k][z+1] = 1
            superMatrix[k][z+3] = -2*inequality[i+1][0][0]
            superMatrix[k][z+4] = -1
            superMatrix[k][n] = 0
            k += 1
            z += 3
        superMatrix[k][0] = 1
        totalPivoting.a = superMatrix
        totalPivoting.n = len(superMatrix)
        totalPivoting.tags = [i for i in range(0,totalPivoting.n)]
        aux = totalPivoting.elimination()
        j = 0
        segments = []
        polBySeg = []
        for i in range(0,len(inequality)):
            polBySeg.append(f"{aux[j]:4g}x^2 + {aux[j+1]:4g}x + {aux[j+2]:4g}")
            segments.append(f"{inequality[i][0][0]:g} ≤ x ≤ {inequality[i][1][0]:g}")
            j += 3
        
        #Find the polynom (polBySeg_i) that applies to the segment (segments_i)
        return segments,polBySeg
    return spline2()


#xn =[-1,0,3,4]
#fxn =[15.5,3,8,1]
#print(spline2Ans(xn,fxn))