import pysindy as ps
import HystereticExpansionSindy as HS





#define function H1 for x1 and add it to a library
p11=HS.preisachFun(alpha=1,alphaproxy=0.1,beta=2,betaproxy=0.1) 
l11=ps.feature_library.CustomLibrary([lambda x: p11.fun(x)],[lambda x: "H11("+str(x)+")"]) 
#define function H1 for x2 and add it to a library
p12=HS.preisachFun(alpha=1,alphaproxy=0.1,beta=2,betaproxy=0.1) 
l12=ps.feature_library.CustomLibrary([lambda x: p12.fun(x)],[lambda x: "H12("+str(x)+")"]) 


p21=HS.preisachFun(0.05,0.01,0.1,0.01)
l21=ps.feature_library.CustomLibrary([lambda x: p21.fun(x)],[lambda x: "H21("+str(x)+")"])
p22=HS.preisachFun(0.05,0.01,0.1,0.01)
l22=ps.feature_library.CustomLibrary([lambda x: p22.fun(x)],[lambda x: "H22("+str(x)+")"])

#concatenate the libraries, restricting their access to their own variable(H11 - x1, H12 - x2 etc...)
inputs=np.array([[0,0,0,0],[1,1,1,1],[0,0,0,0],[1,1,1,1]])
hylib=ps.feature_library.GeneralizedLibrary([l11,l12,l21,l22],inputs_per_library=inputs) 
