import torch
from torch import nn

torch.manual_seed(torch.seed())

# define neural network
n = nn.Sequential(
    nn.Linear(3, 4), # first layer
    nn.Tanh(), # squash
    nn.Linear(4, 5),
    nn.Tanh(),
    nn.Linear(5, 4), 
    nn.Tanh(),
    nn.Linear(4, 1), # output layer
    nn.Tanh(),
)

# training dataset
#xs = torch.tensor([
    #[2.0,  3.0, -1.0], # each 3-element input corresponds to a 1-element output
    #[3.0, -1.0,  0.5],
    #[0.5,  1.0,  1.0],
    #[1.0,  1.0, -1.0],
#])

# xs1 = torch.randn(4, 3) # randomized 4x3 input dataset

# xs2 = torch.randn(4, 3)

dataset = []
for i in range(10):
    dataset.append(torch.randn(4, 3))

# define goals
ys = torch.tensor([
    [ 1.0],
    [-1.0],
    [-1.0],
    [ 1.0],
])

# define the loss function in pytorch. Mean Squared Error (MSE) loss function
loss_fn = nn.MSELoss(reduction="sum")
# define an optimizer using Stochastic Gradient Descent (SGD)
optimizer = torch.optim.SGD(n.parameters(), lr=0.01) # SGD with inputs of my parameters and a learning rate of 0.05

# optimization loop

for k in range(1000):
    
    for data in dataset:
    
        optimizer.zero_grad() # zero out gradients to prevent accumulation
    
        ypred = n(data) # calculate predictions from model
        loss = loss_fn(ypred, ys) # calculate loss, comparing predictions to expected
    
        loss.backward() # perform backpropagation, calculating new gradients
        optimizer.step() # run the optimizer - update each parameter by a little bit times the opposite of its gradient to MINIMIZE the loss function
    
    print(k, loss.item())
    

xstest = torch.randn(4, 3)

# Normalize test inputs from their observed range to [-1, 1].
# xstest = 2 * (xstest - xstest.min()) / (xstest.max() - xstest.min()) - 1


print(n(xstest))