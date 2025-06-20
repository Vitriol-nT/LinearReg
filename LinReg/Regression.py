#Module
#USE OF EXTENSIONAL LIBRARY IS AN ACTION OF PROVING THAT YOU ARE A TOTAL NUMB NUT
#IT IS WITHIN PROVING THE LANGUAGE YOU ARE USING IS A NOTHING BUT BUNCH OF LIBRARIES. WHAT ARE YOU USING? LIBRARY? PYTHON?

#Linear Regression ----------------------------------------------------------------------------------
class LR2:
  def __init__(self, I_val, II_val):
    self.I_val = list(I_val)
    self.II_val = list(II_val)

  def LR2Essence(self):
    best_slope = None
    best_intercept = None
    ss = float('inf')
    mean_1 = sum(self.I_val) / len(self.I_val)
    mean_2 = sum(self.II_val) / len(self.II_val)

    for i in range(-10000, 10001):
      slope = i / 100
      intercept = mean_2 - slope * mean_1
      chunk1 = []

      for j in range(len(self.I_val)):
        x = float(self.I_val[j])
        y = float(self.II_val[j])
        diff = (slope * x + intercept) - y
        ss_part = diff ** 2
        chunk1.append(ss_part)

      total_ss = sum(chunk1)

      if total_ss < ss:
        ss = total_ss
        best_slope = slope
        best_intercept = intercept
    print(f"\nBest fit: {best_slope}x + {best_intercept} with ss of {ss}")

    #getting r sqr
    var_mean = 0
    var_fit = ss / len(self.I_val)
    for _ in range(len(self.II_val)):
      chunk2 = []
      each = (self.II_val[_] - mean_2)**2
      chunk2.append(each)
      var_mean = sum(chunk2) / len(self.II_val)

    r_sqr = (var_mean - var_fit) / var_mean
    print(f"which can explain {(r_sqr) * 100}% of the situations.")

    self.slope = best_slope
    self.intercept = best_intercept

  def LR2PredictionX(self, One):
    print(f"\nPrediction: {self.slope * One + self.intercept}")
    return self.slope * One + self.intercept

  def LR2PredictionY(self, Two):
    print(f"\nPrediction: {(Two - self.intercept)/self.slope}")

#Linear Regression ----------------------------------------------------------------------------------

#Polynomial Regression-------------------------------------------------------------------------------

#Polynomial Regression-------------------------------------------------------------------------------

#Perceptron ------------------------------------------------------------------------------------------
def unit_step_function(x):
  return 1 if x > 0 else 0

class Perceptron:
  def __init__(self, learning_rate=0.1, iterate=1000):
    self.learning_rate = learning_rate
    self.iterate = iterate
    self.activation = unit_step_function
    self.weight = []
    self.bias = None

  def fit(self, X, y):
    n_samples = len(X)
    n_features = len(X[0])
    self.weight = [0.0 for _ in range(n_features)]
    self.bias = 0

    y_ = [1 if i > 0 else 0 for i in y]

    for _ in range(self.iterate):
      for i in range(n_samples):
        x_i = X[i]
        linear_output = sum(x_i[j] * self.weight[j] for j in range(n_features)) + self.bias
        prediction = self.activation(linear_output)
        update = self.learning_rate * (y_[i] - prediction)
        for j in range(n_features):
          self.weight[j] += update * x_i[j]
        self.bias += update

  def prediction(self, X):
    predictions = []
    for x in X:
      linear_output = sum(x[j] * self.weight[j] for j in range(len(x))) + self.bias
      y_pred = self.activation(linear_output)
      predictions.append(y_pred)
    return predictions
#Perceptron ------------------------------------------------------------------------------------------

#Multi-Layered (pre-set 1)----------------------------------------------------------------------------
import math

def tanh(z):
  return (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))


#Multi-Layered  --------------------------------------------------------------------------------------
