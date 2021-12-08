using Statistics
x = [20:100];
mean(x)

median(skipmissing([10, 32, missing, 41, 75, 96]))
  
quantile(x, [0.1, 0.5, 0.9])

function sd(x):
  expectation = mean(x)
  x = map(i -> (i - expectation)^2, x)
  std_dev = sqrt(sum(x)/(length(x) - 1))
  return std_dev
