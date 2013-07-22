from __future__ import division
from math import log, sqrt
import matplotlib.pyplot as plot

init = {}
init['a'] = 0.04
init['b'] = 0.75
init['f'] = 0.02
init['p'] = -0.2
init['v'] = 0.5
init['t'] = 1.0

def sabr(a, b, f, K, p, v, t):
  A = a/((f*K)**((1-b)/2)*(1+(1-b)**2/24*log(f/K)**2+(1-b)**4/1920*log(f/K)**4))
  B = 1+((1-b)**2/24*a**2/((f*K)**(1-b))+1/4*p*b*v*a/((f*K)**((1-b)/2))+(2-3*p**2)/24*(v**2))*t
  
  if not f == K:
    z = v/a * (f*K)**((1-b)/2) * log(f/K)
    x = log((sqrt(1-2*p*z+z*z)+z-p) / (1-p))    
    return A*(z/x)*B
  else:
    return A*B        
  
def smile():
  strikes = [x*0.0025 for x in range(1, 41)]
  imp_vols = [sabr(init['a'], init['b'], init['f'], K, init['p'], init['v'], init['t']) for K in strikes]
  plot.title(r'Basic volatility smile')
  plot.xlabel('$K$')
  plot.ylabel(r'Implied volatility')
  plot.plot(strikes, imp_vols)
  plot.savefig('basic.png')
  
def shock(parameter, amount, parameter_name, description):
  up = init.copy()
  down = init.copy()
  up[parameter] = init[parameter] + amount
  down[parameter] = init[parameter] - amount
  strikes = [x*0.0025 for x in range(1, 41)]
  imp_vols_init = [sabr(init['a'], init['b'], init['f'], K, init['p'], init['v'], init['t']) for K in strikes]
  imp_vols_down = [sabr(down['a'], down['b'], down['f'], K, down['p'], down['v'], down['t']) for K in strikes]
  imp_vols_up = [sabr(up['a'], up['b'], up['f'], K, up['p'], up['v'], up['t']) for K in strikes]
  plot.figure()
  plot.title(description)
  plot.xlabel('$K$')
  plot.ylabel('Implied volatility')
  plot.plot(strikes, imp_vols_down, label='%s = %f' % (parameter_name, down[parameter]))
  plot.plot(strikes, imp_vols_init, label='%s = %f' % (parameter_name, init[parameter]))
  plot.plot(strikes, imp_vols_up, label='%s = %f' % (parameter_name, up[parameter]))
  plot.legend()
  plot.savefig('%s.png' % (parameter))
  
def run_experiments():
  shock('f', 0.01, r'$f$', 'Shocking the forward price')
  shock('v', 0.1, r'$v$', 'Shocking the volatility of volatility')
  shock('a', 0.02, r'$\alpha$', 'Shocking the initial volatility')
  shock('p', 0.7, r'$\rho$', 'Shocking the correlation')
  shock('b', 0.1, r'$\beta$', 'Shocking the elasticity')

if __name__ == "__main__":
  run_experiments()
  
  
