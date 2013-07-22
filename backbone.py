import matplotlib.pyplot as plot

def backbone(alpha, beta, f):
  return alpha / (f ** (1 - beta))
  
def generate_charts():
  f_values = [0.1 * x for x in range(1,31)]
  
  plot.title(r'Backbone for different values of $\beta$')
  plot.xlabel('$f$')
  plot.ylabel(r'Implied volatility')
  plot.plot(f_values, [backbone(0.04, 0.0, f) for f in f_values], label=r'$\beta=0.0$')
  plot.plot(f_values, [backbone(0.04, 0.5, f) for f in f_values], label=r'$\beta=0.5$')
  plot.plot(f_values, [backbone(0.04, 1.0, f) for f in f_values], label=r'$\beta=1.0$')
  plot.legend()
  plot.savefig('backbone.png')

if __name__ == "__main__":
  generate_charts()

