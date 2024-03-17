import numpy as np
import torch

# Load your input values as numpy-array
X = np.array([[1,2], [2,3], [3,3]]) #torch.Tensor([[1.0], [2.0], [3.0]])
Y = np.array([5, 8,10]) #torch.Tensor([[5.0], [8.0], [10.0]])
# ------------------------- in fact
"""
data_dir = {}
data = pd.read_csv(data_dir)
X = data[[input_cols]].to_numpy()
Y = data[target_col].to_numpy()
"""
#========================== class of linear regression
class LinearRegressionModel(torch.nn.Module):
    """
        Class này được sử dụng cho các bài toán Linear Regression trong torch
    """
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)  

    def forward(self, x):
        out = self.linear(x)
        return out

def ridge_loss(Y_true, Y_pred, w, lamb):
    """
        Trong trường hợp bài toán hồi quy tuyến tính có một lượng chỉnh hóa bởi Ridge
    """
    pred_loss = torch.norm((Y_true-Y_pred),p='fro')**2
    reg = torch.norm(w, p='fro')**2
    return ((1/Y_true.size()[0])*pred_loss + lamb*reg)

#============================== Convert numpy array to torch Variable
# assume that we have 2 features as inputs
inputs = torch.Tensor(X.reshape(-1, 2))
print(inputs)
labels = torch.Tensor(Y.reshape(-1, 1))
print(labels)

#============================== cpu or gpu
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
inputs = inputs.to(device)
labels = labels.to(device)
model = LinearRegressionModel(inputs.shape[1], 1)
model.to(device)
print('Device.training on cpu/gpu:', device)

#============================= Other parameters
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=5e-2)

print(f"|{'Epoch': ^5}|{'slopes': ^25}|{'intercept': ^10}|{'loss': ^15}|")
# ============================= TRAINING
def save_model(model, inputs, labels, criterion, optimizer, 
               n_epochs=600, if_ridge=False, saved_model_name='reg_model.h5'):
    """
        Input params
            * model (class)
            * inputs: X
            * labels: y
            * criterion: MSE / MAE or MAPE
            * optimizer = SGF / Adam / ...
            * n_epochs : default 600
            * if_ridge : if linear regression model included Ridge
    """
    for epoch in range(n_epochs): 
        # Forward pass: Compute predicted y by passing 
        # x to the model
        pred_y = model(inputs)

        # Compute and print loss
        if if_ridge == False:
            loss = criterion(pred_y, labels)
        else:
            loss = ridge_loss(pred_y, labels,
                              model.state_dict()['linear.weight'],
                              lamb=0.05) 

        # Zero gradients, perform a backward pass, 
        # and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()    

        if epoch % 100 == 99:        
            epoch_vals = str(epoch).zfill(3)
            w = model.state_dict()['linear.weight']
            b = model.state_dict()['linear.bias']        
            w = ', '.join([f"{x:.8f}" for x in w.reshape(-1).tolist()])
            b = f"{b.tolist()[0]:.6f}"
            loss_val = f"{loss.item():.11f}"
            print(f"|{epoch_vals: ^5}|{w: ^25}|{b: ^10}|{loss_val: ^15}|")
    
    # Saved your model    
    torch.save(model.state_dict(), saved_model_name)

if __name__ == "__main__":
    n_epochs = int(input("Input the number of epochs: "))   
    saved_model_name = input("Name to saved your model: ")
    print(100*"=")
    save_model(model, inputs, labels, criterion, optimizer, 
               n_epochs=n_epochs, if_ridge=True, saved_model_name=saved_model_name)
    
    # if you wanna to load model
    # model = LinearRegressionModel(2, 1)
    # model.load_state_dict(torch.load("reg_model.h5"))