import sympy as sp
from sympy import *
import numpy as np

def evalVetorFunction(fx, vector = [], variables = []):
  pairWiseSubs = dict(zip(["x1","x2", "x3", "x4"], vector))
  return fx.evalf(subs = pairWiseSubs)
  
def GD(theta=[], grad=None, gd_pmr={}, f_params={}):
    '''
    Descenso de gradiente

    Parámetros
    -----------
    theta : condicion inicial
    grad : función que calcula el gradiente
    gd_params : lista de parametros para el algoritmo de desce nIter = gd_params[0] número de iteraciones
    alpha = gd_params[1] tamaño de paso alpha
    f_params : lista de parametros para la funcion objetivo
    kappa = f_params['kappa'] parametro de esca X = f_params['X'] Variable independient y = f_params['y'] Variable dependiente

    Regresa
    -----------
    Theta : trayectoria de los parametros
    Theta[-1] es el valor alcanzadoX
    '''
    nIter = gd_pmr['nIter']
    alpha = gd_pmr['alpha']
    Theta=[]
    for t in range(nIter):
        p = evalVetorFunction(Gf, theta)
        theta = sp.Matrix([theta]) - alpha*p
        Theta.append(theta)
    return np.array(Theta)


def NAG(theta=[], grad=None, gd_params={}, f_params={}):
    '''
    Descenso acelerado de Nesterov (NAG)
    Parámetros
    -----------
    theta : condicion inicial
    grad : funcion que calcula el gradiente
    gd_params : lista de parametros para el algoritmo de descenso
        nIter = gd_params['nIter'] número de iteraciones
        alpha = gd_params['alpha'] tamaño de paso alpha
        eta = gd_params['eta'] parametro de ine 
    f_params : lista de parametros para la funcion objetivo,
            kappa = f_params['kappa'] parametro de escala
            X = f_params['X'] Variable independiente 
            y = f_params['y'] Variable dependiente 
    Regresa
    -----------
    Theta : trayectoria de los parametros
    Theta[-1] es el valor alcanzado en la ultima evaluacion '''
    nIter = gd_params['nIter']
    alpha = gd_params['alpha']
    eta = gd_params['eta']
    p = np.zeros(shape=(1, len(theta))).tolist()
    p = Matrix([p])
    Theta=[]
    for _ in range(nIter):
        pre_theta = Matrix([theta]) - alpha*p
        g = evalVetorFunction(Gf, pre_theta)
        p = g + eta*p
        theta = theta - alpha*p
        Theta.append(theta)
    return np.array(Theta)





if __name__ == "__main__": 

    #VARIABLES
    x1 = sp.core.symbol.Symbol("x1")
    x2 = sp.core.symbol.Symbol("x2") 
    x3 = sp.core.symbol.Symbol("x3")
    x4 = sp.core.symbol.Symbol("x4")

    var = ["x"+str(i) for i in range(1, 5)]

    #FUNCION DE Rosenbrock
    f = Matrix([100*((x1**2-x2)**2+(x3**2-x4)**2)+(x1-1)**2+(x3-1)**2])

    g = Matrix([x1**2+x2**2])
    #Jacobiano de la fucnion de RosenBrock (Gradiente)
    Gf = f.jacobian([x1,x2,x3,x4])
    Gg = g.jacobian([x1,x2])
    #print(evalVetorFunction(Gf, [0,0,0,0], var))

    # XX print(GD([-1,0,2,1], None, gd_pmr={'nIter': 10000, 'alpha':1e-3},f_params={})) #ESTE VALOR TIENDE A UN BUEN VALOR
    print(GD([-1,-1,-1,-1], Gf, gd_pmr={'nIter': 3000, 'alpha':2.35e-3}, f_params={})[-1])
    #print(GD([-1,-1,1,-1], None, gd_pmr={'nIter': 100, 'alpha':1e-10}, f_params={}))
    #print(NAG([0,0,0,0], None, gd_params={'nIter': 100, 'alpha':1e-10, "eta": 10}, f_params={}))
    #print(Matrix([[-1,-1,-1,-1]])-Gf.evalf(subs = {"x1": 0, "x2": 0, "x3": 0, "x4": 0}))


def MGD(theta=[], grad=None, gd_params={}, f_params={}):
    '''
    Descenso de gradiente con momento (inercia)

    Parámetros
    -----------
    theta : condicion inicial
    grad : funcion que calcula el gradiente
    gd_params : lista de parametros para el algoritmo de desce nIter = gd_params['nIter'] número de itera alpha = gd_params['alpha'] tamaño de paso  eta = gd_params['eta'] parametro de ine f_params : lista de parametros para la funcion objetivo,
    kappa = f_params['kappa'] parametro de esc X = f_params['X'] Variable independien y = f_params['y'] Variable dependiente Regresa
    -----------
    Theta : trayectoria de los parametros
    Theta[-1] es el valor alcanzado en la ultim '''
    nIter = gd_params['nIter']
    alpha = gd_params['alpha']
    eta = gd_params['eta']
    p_old = np.zeros(theta.shape)
    Theta=[]
    for t in range(nIter):
        g = grad(theta, f_params=f_params)
        p = g + eta*p_old
        theta = theta - alpha*p
        p_old=p
        Theta.append(theta)
    return np.array(Theta)



def ADADELTA(theta=[], grad=None, gd_params={}, f_params={}):
    '''
    Descenso de Gradiente Adaptable (ADADELTA)

    Parámetros
    -----------
    theta : condicion inicial
    grad : funcion que calcula el gradiente
    gd_params : lista de parametros para el algoritmo de desce nIter = gd_params['nIter'] número de it alphaADA = gd_params['alphaADADELTA'] tama eta = gd_params['eta'] parametro ada f_params : lista de parametros para la funcion objetivo,
    kappa = f_params['kappa'] parametro de esc X = f_params['X'] Variable independien y = f_params['y'] Variable dependiente Regresa
    -----------
    Theta : trayectoria de los parametros
    Theta[-1] es el valor alcanzado en la ultim '''
    epsilon= 1e-8
    nIter = gd_params['nIter']
    alpha = gd_params['alphaADADELTA']
    eta = gd_params['eta']
    G = np.zeros(theta.shape)
    g = np.zeros(theta.shape)
    Theta=[]
    for t in range(nIter):
        g = grad(theta, f_params=f_params)
        G = eta*g**2 + (1-eta)*G
        p = 1.0/(np.sqrt(G)+epsilon)*g
        theta = theta - alpha * p
        Theta.append(theta)
    return np.array(Theta)