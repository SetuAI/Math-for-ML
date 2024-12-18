
"""
Gradient Descent 

"""

# create a small dataset using make_regression 
# make_regression is specifically designed to generate synthetic datasets for regression tasks.

import numpy as np
from sklearn.datasets import make_regression


"""
code creates a simple dataset with 4 data points for a linear regression problem, 
where each point has one feature and one target variable, 
and there's added noise to make it more realistic.

Explanation : 
    
n_samples=4: This specifies that the dataset should contain 4 samples (data points).
n_features=1: This indicates that each sample will have only one feature (predictor variable). Imagine this as a single column in a spreadsheet.
n_informative=1: This means that all of the features created actually contribute to the target variable's value.
n_targets=1: This specifies that there's only one target variable (the value we're trying to predict) for each sample. This is typical for simple linear regression.
noise=80: This introduces random noise into the target variable. A higher value means more scatter in the data, making the relationship between features and target less clear.
random_state=13: This sets the seed for the random number generator. Using a fixed seed ensures that you'll get the same dataset every time you run the code, which is useful for reproducibility

    

"""

X,y = make_regression(n_samples = 4,
                      n_features=1,
                      n_informative=1,
                      n_targets=1,
                      noise=80, 
                      random_state=13)


import matplotlib.pyplot as plt
plt.scatter(X,y)

# we need to appy LR on this using GD


"Applying OLS : so we already know what is  slope and intercept"

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X,y)

"checking slope value after training the model (after .fit)"
reg.coef_
# 78.35


"checking intercept value"
reg.intercept_
# 26.15

"""
now we will start with a random value of  intercept (b)

and the end goal is to reach near 26.15 which is the intercept value

"""

"we know m and b, so plot the regression line"

plt.scatter(X,y)
plt.plot(X, reg.predict(X), color='red') # this red line is OLS line
# reg.predict(X): This uses the trained model (reg) to predict the target 
# variable (y) for the input features (X)

"""
Let's apply Gradient Descent asssuming slop value is constant of m=78.35

and assume the value of intercept b = 0 (randonly taking b=0)


"""


y_pred = ((78.35 * X) + 0).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X), color="red", label="OLS")
plt.plot(X,y_pred, color="green",label ="at b=0") #when we start GD
plt.legend()
plt.show()

"""
Code explanation : 
    
y_pred = ((78.35 * X) + 0).reshape(4): 
This line calculates the predicted y values (y_pred) using the fixed slope (78.35) 
and an intercept of 0. 
The reshape(4) ensures that y_pred has the correct shape (a vector of 4 values) 
to match the number of data points.


plt.plot(X, reg.predict(X), color="red", label="OLS"): 
This plots the line generated by the OLS regression model (reg) in red. 
This represents the best-fit line according to the OLS method.

plt.plot(X, y_pred, color="green", label="at b=0"): 
This plots the line you calculated manually with the fixed slope and b=0 in green.

---------------------------------------------------------------------------------------------------

Output :

Blue Scatter Points: Represent the original data (X, y).

Red Line (OLS): This is the best-fit line calculated by the OLS method. It aims to minimize the sum of squared errors between the predicted and actual y values.

Green Line (at b=0): This is the line you calculated using the fixed slope (78.35) and intercept 0. It's likely not as good a fit as the red line because the intercept isn't optimized.

"""



"Now we have to start applying GD and notice that green line moves towards red line"


m = 78.35
b = 0

"""
if you can recall the formula

-2 summation from i=1 to n 
(yi- m.xi-b)

in the above  formula we fit the value of b

"""

loss_slope = -2 * np.sum(y - m*X.ravel() - b)
loss_slope #  -209.27

# X.ravel(): Flattens the feature matrix X into a 1D array.
# This is necessary to ensure correct element-wise operations with y. 
#If X is already a 1D array (or a column vector), this doesn't change anything, but it handles cases where X might be a 2D array even if it only has one feature.

"Now let's define learning rate as 0.1"
lr = 0.1

"""
FYI : the product of learning rate and slope is termed as "Step-size"

"""
step_size = loss_slope * lr
step_size # -20.92

"So now, just subtract b(old) - step_size , that gives your b(new)"

b = b - step_size
# initial value of b = 0
b #  20.92

"so we started at b = 0, we need to reach 26.15m, now we have reached 20.92"

"Let's plot with with b(new) and constant slope and check graph"

y_pred1 = ((78.35 * X) + b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X), color="red", label="OLS")
plt.plot(X,y_pred1, color="black",label = 'b = {}'.format(b))
plt.plot(X,y_pred, color="green",label ="at b=0") #when we start GD
plt.legend()
plt.show()
    

"Iteration 2 : now with the current b(new) at this point we will calculate slope"
# just here , b is not 0 but 20.92

loss_slope = -2 * np.sum(y - m*X.ravel() - b)
loss_slope #  -41.85

"calculate stepsize = loss_slope * lr"

step_size = loss_slope * lr
step_size  # -4.18

"Again calculate b(new)"
b = b - step_size
b # 25.11

"If  you recall the output we are chasing = 26.11 and we are close at 25.11"

"We will again calculate y"

y_pred2 = ((78.35 * X) + b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X), color="red", label="OLS")
plt.plot(X,y_pred2, color="blue",label = 'b = {}'.format(b))
plt.plot(X,y_pred1, color="black",label = 'b = {}'.format(b))
plt.plot(X,y_pred, color="green",label ="at b=0") #when we start GD
plt.legend()
plt.show()

"You can see the blue line has almost climbed upon the red line we were chasing"

"Iteration 3 , with the value of b(new) = 25.11"
loss_slope = -2 * np.sum(y - m*X.ravel() - b)
loss_slope  #-8.37

step_size = loss_slope * lr
step_size # -0.83
# if you look step size is going lower and lower

b = b - step_size
b  # 25.95 which is very close to 26.15

y_pred3 = ((78.35 * X) + b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X), color="red", label="OLS")
plt.plot(X,y_pred3, color="pink",label = 'b = {}'.format(b))
plt.plot(X,y_pred2, color="blue",label = 'b = {}'.format(b))
plt.plot(X,y_pred1, color="black",label = 'b = {}'.format(b))
plt.plot(X,y_pred, color="green",label ="at b=0") #when we start GD
plt.legend()
plt.show()

"""
The pink line is almost on top of red line, and as you keep on doing iterations

you will see the line keeps getting closer or overlaps or "converges"

by reducing the step_size further again


PS : Even if you start at say b = 100, the line will be very off from the red line

and then perform all the further calculations with b = 100

You can also try it without using learning rate and notice the zig zag movement

"""


"-----------------------------------------------------------------------------------"

"You can also loop this through and define the number of epochs"

b = -100 # initial b = -100
m = 78.35
lr = 0.1 

epochs = 10 # we will run the loops 10 times

for i in range(epochs):
    loss_slope = -2 * np.sum(y - m*X.ravel() - b)
    b = b - (lr * loss_slope)
    
    y_pred = m * X + b
    
    plt.plot(X,y_pred)
    
plt.scatter(X,y)

"""
in every epoch run, all values will be updated

so, if you look at the graph, we started at the blue line and 
after 10 iterations/epochs we are at the green line

If you reduce the learning rate say 0.01,
you will take very small steps and hence you might not reach
the right output in 10 iterations or epochs.

So in that case, increase the number of epochs, say epochs=100

"""

b = -100 # initial b = -100
m = 78.35
lr = 0.01  # learning rate too low for 10 epochs

epochs = 10 # we will run the loops 10 times

for i in range(epochs):
    loss_slope = -2 * np.sum(y - m*X.ravel() - b)
    b = b - (lr * loss_slope)
    
    y_pred = m * X + b
    
    plt.plot(X,y_pred)
    
plt.scatter(X,y)


"with learning rate as 0.01 and with 100 epochs"
b = -100 # initial b = -100
m = 78.35
lr = 0.01  # learning rate too low for 10 epochs

epochs = 100 # we will run the loops 100 times

for i in range(epochs):
    loss_slope = -2 * np.sum(y - m*X.ravel() - b)
    b = b - (lr * loss_slope)
    
    y_pred = m * X + b
    
    plt.plot(X,y_pred)
    
plt.scatter(X,y)
# here will converge at the right output with small steps


"------------------------------------------------------------------"

"""
Create a GD Regressor class
in that create 2 methods : fit and predict
in that implement GD

First step : calculate b 
second step : calculate m
 
"""
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score


X,y = make_regression(n_samples=100, 
                      n_features=1, 
                      n_informative=1,
                      n_targets=1,
                      noise=20,
                      random_state=13)


plt.scatter(X,y) # random data generation

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train,y_train)
print("Slope",lr.coef_)
print("Intercept",lr.intercept_)


y_pred = lr.predict(X_test)
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

"""
R-squared (R²) score is a statistical measure that represents the proportion
of the variance in the dependent variable (target variable y) 
that is explained by the independent variables (features X) in a regression model.
In simpler terms, it tells you how well your model fits the data.


Interpreting the R² Score:

R² = 1: A perfect fit. Your model explains all the variability in the target variable. This is very rare in real-world data.

R² = 0: Your model doesn't explain any of the variability of the data around its mean. This means your model's predictions are no better than simply predicting the average value of the target variable.

0 < R² < 1: Your model explains some of the variability in the target variable. The higher the R² value, the better the fit.

R² < 0: Your model fits the data worse than a horizontal line (the mean). This can happen if the model is highly inappropriate for the data.


"""

# slope = 28.12 and intercept = -2.27


"class to calculate intercept for given data which should be close to -2.27 "

m = 28.12

class GDRegressor:
    
    def __init__(self,learning_rate, epochs):
        self.m = 28.12
        self.b = -120 #initial can be any value 0 or -ve
        self.learning_rate = learning_rate
        self.epochs = epochs
        
    def fit(self,X,y):
        "calculate b using GD"
        for i in range(self.epochs):
            #calculate loss_slope (how much the loss changes as b changes)
            loss_slope = -2 * np.sum(y - self.m*X.ravel() - self.b)
            # update b
            self.b = self.b - (self.learning_rate * loss_slope)
        print(self.b)
    
gd = GDRegressor(0.1, 10) # learning rate = 0.1, epochs = 10

gd.fit(X,y)

"According to the model , the output is -721554187522014.0 " # learning rate is too high

"""
Learning Rate Too High: A learning rate of 0.1 is quite high, especially when the gradient can be large. A large learning rate can cause the updates to overshoot the optimal value and diverge, leading to very large or very small parameter values.

Incorrect Initial Value of b and Fixed m: The combination of a fixed m and a starting b of -120, when combined with the relatively high learning rate, could put the initial guess very far from the optimal solution. Each iteration, instead of converging, moves b further away in larger and larger steps.

"""
"--------------------------------------------------------------------------------------------------------------"

"let us take the same code and inside the look print the values of b and loss slope\
    to check the movement for 10 iterations or epochs"



m = 28.12

class GDRegressor:
    
    def __init__(self,learning_rate, epochs):
        self.m = 28.12
        self.b = -120 #initial can be any value 0 or -ve
        self.learning_rate = learning_rate
        self.epochs = epochs
        
    def fit(self,X,y):
        "calculate b using GD"
        for i in range(self.epochs):
            #calculate loss_slope (how much the loss changes as b changes)
            loss_slope = -2 * np.sum(y - self.m*X.ravel() - self.b)
            # update b
            self.b = self.b - (self.learning_rate * loss_slope)
            print(loss_slope, self.b)
        print(self.b)
    
gd = GDRegressor(0.1, 10) # learning rate = 0.1, epochs = 10

gd.fit(X,y)


"""
Observations :
    
Iteration 1: The initial loss_slope is -23537. With a learning rate of 0.1, b is updated by adding (0.1 * 23537) to the initial -120, resulting in a positive b value.

Iteration 2: The loss_slope flips sign and becomes much larger. Now, a large negative value is subtracted from b, making it negative again.

Subsequent Iterations: The loss_slope co ntinues to alternate in sign and grow exponentially in magnitude. This causes b to oscillate wildly and diverge to extremely large negative and positive values. The updates are so large that the algorithm never has a chance to converge.

Key Observation: The oscillation and rapid growth of both the loss_slope and b are clear signs that the learning rate is far too high for this problem. The updates are so large that they're constantly overshooting the optimal value.

"""
    

"------------------------------------------------------------------------------------------"
"Better way to reduce the learning rate and increase the number of epochs"


m = 28.12

class GDRegressor:
    
    def __init__(self,learning_rate, epochs):
        self.m = 28.12
        self.b = -120 #initial can be any value 0 or -ve
        self.learning_rate = learning_rate
        self.epochs = epochs
        
    def fit(self,X,y):
        "calculate b using GD"
        for i in range(self.epochs):
            #calculate loss_slope (how much the loss changes as b changes)
            loss_slope = -2 * np.sum(y - self.m*X.ravel() - self.b)
            # update b
            self.b = self.b - (self.learning_rate * loss_slope)
        print(self.b)
    
gd = GDRegressor(0.001, 100) # learning rate = 0.001, epochs = 100

gd.fit(X,y)


"-------------------------------------------------------------------------"

"you can now see the output we get here is -2.31"
"And the actual answer we calculated above the intercept value was -2.27"
"That is very close"

"Jus to check how the loss slope and b converge we can print the values inside loop"

m = 28.12

class GDRegressor:
    
    def __init__(self,learning_rate, epochs):
        self.m = 28.12
        self.b = -120 #initial can be any value 0 or -ve
        self.learning_rate = learning_rate
        self.epochs = epochs
        
    def fit(self,X,y):
        "calculate b using GD"
        for i in range(self.epochs):
            #calculate loss_slope (how much the loss changes as b changes)
            loss_slope = -2 * np.sum(y - self.m*X.ravel() - self.b)
            # update b
            self.b = self.b - (self.learning_rate * loss_slope)
            print(loss_slope, self.b)
        print(self.b)
    
gd = GDRegressor(0.001, 100) # learning rate = 0.001, epochs = 100

gd.fit(X,y)

"Observations : you can check b intercept starts at -96 and heads towards -2.31\
    and loss_slope that starts at -23537.641 decreases further and further"

"---------------------------------------------------------------------------"
"LEARNING RATE IS CRUCIAL AND SO ARE THE NUMBER OF EPOCHS DEFINED"

"please note, as of now WE HAVE CONSIDERED m to be constant in all scenarios"

"--------------------------------------------------------------------------------"


"Code for 2 components - m and b"

from sklearn.datasets import make_regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score



X,y = make_regression(n_samples=100,
                      n_features=1, 
                      n_informative=1, 
                      n_targets=1,
                      noise=20,
                      random_state=13)



plt.scatter(X,y)
# data is linear

# apply LR
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X_train,y_train)
print("Slope",lr.coef_)
print("Intercept",lr.intercept_)

# we can check cross val score
np.mean(cross_val_score(lr, X, y , scoring='r2',cv=10)) #0.63
# so we need to be near 0.63


class GDRegressor:
    """
    Here we will compute for m and b 
    hence loss_slop_b and loss_slope_m 
    
    """
    
    def __init__(self,learning_rate, epochs):
        self.m = 100 # initial value of slope 
        self.b = -120 #initial can be any value 0 or -ve
        self.learning_rate = learning_rate
        self.epochs = epochs
        
    def fit(self,X,y):
        "calculate b using GD"
        for i in range(self.epochs):
            #calculate loss_slope (how much the loss changes as b changes)
            loss_slope_b = -2 * np.sum(y - self.m*X.ravel() - self.b)
            loss_slope_m = -2 * np.sum((y - self.m*X.ravel() - self.b)*X.ravel()) # X.ravel so output is in single dimension
            # update m 
            self.m = self.m - (self.learning_rate * loss_slope_m)
            # update b
            self.b = self.b - (self.learning_rate * loss_slope_b)
        print(self.m, self.b)
    
gd = GDRegressor(0.001, 100) # learning rate = 0.001, epochs = 100

gd.fit(X,y)

"output , slope : 27.82 and intercept : -2.29"
# you can scroll above and check when you did lr.fit what was slope and intercept

"We can compare and it shows the algorithm is converged"

"we have checked for epochs = 100, check if it converges at lower epoch\
    say epoch = 50 "


class GDRegressor:
    """
    Here we will compute for m and b 
    hence loss_slop_b and loss_slope_m 
    
    """
    
    def __init__(self,learning_rate, epochs):
        self.m = 100 # initial value of slope 
        self.b = -120 #initial can be any value 0 or -ve
        self.learning_rate = learning_rate
        self.epochs = epochs
        
    def fit(self,X,y):
        "calculate b using GD"
        for i in range(self.epochs):
            #calculate loss_slope (how much the loss changes as b changes)
            loss_slope_b = -2 * np.sum(y - self.m*X.ravel() - self.b)
            loss_slope_m = -2 * np.sum((y - self.m*X.ravel() - self.b)*X.ravel()) # X.ravel so output is in single dimension
            # update m 
            self.m = self.m - (self.learning_rate * loss_slope_m)
            # update b
            self.b = self.b - (self.learning_rate * loss_slope_b)
        print(self.m, self.b)
    
gd = GDRegressor(0.001, 50) # learning rate = 0.001, epochs = 100

gd.fit(X,y)

"We can see, it easily converges at epochs= 50 as well"


"""
Blog for learning more on GD :
    https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent
"""
