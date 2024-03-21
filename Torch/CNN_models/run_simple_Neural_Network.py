import torch
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#====================== Load data: example iris ============================
iris = sns.load_dataset("iris")
lab = LabelEncoder()
iris['species'] = lab.fit_transform(iris['species'])
X = iris.drop(columns='species')
y = iris['species']
# Phân tách dữ liệu để huấn luyện và kiểm chứng
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, 
                                                    stratify=y, random_state=42)
# Transform từ numpy array thành torch-tensor
X_train = torch.FloatTensor(X_train.to_numpy())
X_test = torch.FloatTensor(X_test.to_numpy())
y_train = torch.LongTensor(y_train.to_numpy())
y_test = torch.LongTensor(y_test.to_numpy())

#======================= modeling
class DNN(torch.nn.Module):
    """
        Các tham số giữa các layers trong đây có thể được tùy chỉnh
        Ở đây ta dùng activation-function là RELU
        Layer 1 có dimension = 4 x 256
        Layer 2 là 256 x 64
        Output layer là 64 x 3
        Ở đây ta đang giả định output_dim = 3 là số categories trong iris-data
            - setosa
            - versicolor    
            - virginica     
    """
    def __init__(self, input_dim, output_dim):
        super(DNN,self).__init__()
        self.input_layer    = torch.nn.Linear(input_dim, 256)
        self.hidden_layer1  = torch.nn.Linear(256, 64)
        self.output_layer   = torch.nn.Linear(64, output_dim)
        self.relu = torch.nn.ReLU()    
    
    def forward(self,x):
        out =  self.relu(self.input_layer(x))
        out =  self.relu(self.hidden_layer1(out))
        out =  self.output_layer(out)
        return out
    
#======================= modeling
class DNN2(torch.nn.Module):
    """
        Các tham số giữa các layers trong đây có thể được tùy chỉnh
        Hơn nữa ở model này ta sẽ dùng thêm nhân tố DropOut
        Ở đây ta dùng activation-function là RELU
        Hidden-Layer 1 có dimension = 4 x 512
        Hidden-Layer 2 là 512 x 256
        ...
        Hidden-Layer 6 là 16 x 8
        Output layer là 8 x 3
        Ở đây ta đang giả định output_dim = 3 là số categories trong iris-data
            - setosa
            - versicolor    
            - virginica     
    """
    def __init__(self, input_dim, output_dim):
        super(DNN2, self).__init__()
        self.dropout        = torch.nn.Dropout(0.3)
        self.input_layer    = torch.nn.Linear(input_dim, 512)
        self.hidden_layer1  = torch.nn.Linear(512, 256)
        self.hidden_layer2  = torch.nn.Linear(256, 128)
        self.hidden_layer3  = torch.nn.Linear(128, 64)
        self.hidden_layer4  = torch.nn.Linear(64, 32)
        self.hidden_layer5  = torch.nn.Linear(32, 16)
        self.hidden_layer6  = torch.nn.Linear(16, 8)        
        self.output_layer   = torch.nn.Linear(8, output_dim)
        self.relu = torch.nn.ReLU()    
    
    def forward(self,x):
        out =  self.relu(self.input_layer(x))
        out =  self.relu(self.hidden_layer1(out))
        out =  self.relu(self.hidden_layer2(out))
        out =  self.relu(self.hidden_layer3(out))
        out =  self.relu(self.hidden_layer4(out))
        out =  self.relu(self.hidden_layer5(out))
        out =  self.relu(self.hidden_layer6(out))        
        out =  self.output_layer(out)
        return out
        
#====================== TRAINING    
def train(model,optimizer,criterion,
                  X_train,y_train,
                  X_test,y_test,
                  num_epochs,
                  train_losses,test_losses,
                  saved_model_name):
    """
        model: Your CNN model to classify
        optimizer: thường là Adam / SGD
        criterion: Cross-entropy
        X_train, X_test, y_train, y_test: validation check
        num_epochs: number of epochs
        train_losses,test_losses: loss at each epoch
        saved_model_name: name of model after trained
    """
    for epoch in range(num_epochs):
        #clear out the gradients from the last step loss.backward()
        optimizer.zero_grad()
        
        #forward feed
        output_train = model(X_train)

        #calculate the loss
        loss_train = criterion(output_train, y_train)

        #backward propagation: calculate gradients
        loss_train.backward()

        #update the weights
        optimizer.step()
        
        output_test = model(X_test)
        loss_test = criterion(output_test,y_test)

        train_losses[epoch] = loss_train.item()
        test_losses[epoch] = loss_test.item()

        if (epoch + 1) % 50 == 0:
            print(f"Epoch {epoch+1}/{num_epochs}, Train Loss: {loss_train.item():.4f}, Test Loss: {loss_test.item():.4f}")

    torch.save(model.state_dict(), "clf_model.h5")

#=======================================================================================
if __name__ == "__main__":
    num_epochs = int(input("Input the number of epochs: "))   
    saved_model_name = input("Name to saved your model: ")
    input_dim = int(input("Number of features in your models: "))
    output_dim = int(input("Your output-dimension (how many categories in your output) is: "))
    learning_rate = float(input("Your learning_rate is: "))
    model = DNN(input_dim,output_dim)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)
    train_losses = np.zeros(num_epochs)
    test_losses  = np.zeros(num_epochs)
    print(100*"=")
    train(model,optimizer,criterion,
          X_train,y_train,X_test,y_test,
          num_epochs,
          train_losses,test_losses,
          saved_model_name)
    
    # if you wanna to load model
    # model = DNN(4, 3)
    # model.load_state_dict(torch.load("clf_model.h5"))