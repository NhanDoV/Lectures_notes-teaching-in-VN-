import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torch import autograd
from torch.autograd import Variable
from torchvision.utils import make_grid
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# Configurable variables
device = 'cuda' if torch.cuda.is_available() else 'cpu'
dataroot = "/kaggle/input/fashionmnist/fashion-mnist_train.csv" # this file has 60k-rows and 785-columns (first is label and 784 cols of pixel)
img_size = 28 # Image size
batch_size = 64  # Batch size
z_size = 100
epochs = 50  # Train epochs
learning_rate = 1e-4
generator_layer_size = [256, 512, 1024]
discriminator_layer_size = [1024, 512, 256]
class_list = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
class_num = len(class_list)

# Speed ups
torch.autograd.set_detect_anomaly(False)
torch.autograd.profiler.profile(False)
torch.autograd.profiler.emit_nvtx(False)
torch.backends.cudnn.benchmark = True

# Set random seed for reproducibility
manualSeed = 999
np.random.seed(manualSeed)
torch.manual_seed(manualSeed)
torch.use_deterministic_algorithms(True) # Needed for reproducible results

# We can use an image folder dataset the way we have it setup.
# Create the dataset
class FashionMNIST(Dataset):
    def __init__(self, path, img_size, transform=None):
        self.transform = transform
        fashion_df = pd.read_csv(path)
        self.images = fashion_df.iloc[:, 1:].values.astype('uint8').reshape(-1, img_size, img_size)
        self.labels = fashion_df.label.values
        print('Image size:', self.images.shape)
        print('--- Label ---')
        print(fashion_df.label.value_counts())

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        label = self.labels[idx]
        img = self.images[idx]
        img = Image.fromarray(self.images[idx])
            
        if self.transform:
            img = self.transform(img)
        
        return img, label
    
dataset = FashionMNIST(dataroot, img_size)
transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5,), std=(0.5,))
])
dataset = FashionMNIST(dataroot, img_size, transform=transform)
data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

# We can use an image folder dataset the way we have it setup.
# Create the dataset
class FashionMNIST(Dataset):
    def __init__(self, path, img_size, transform=None):
        self.transform = transform
        fashion_df = pd.read_csv(path)
        self.images = fashion_df.iloc[:, 1:].values.astype('uint8').reshape(-1, img_size, img_size)
        self.labels = fashion_df.label.values
        print('Image size:', self.images.shape)
        print('--- Label ---')
        print(fashion_df.label.value_counts())

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        label = self.labels[idx]
        img = self.images[idx]
        img = Image.fromarray(self.images[idx])
            
        if self.transform:
            img = self.transform(img)
        
        return img, label
    
dataset = FashionMNIST(dataroot, img_size)
transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5,), std=(0.5,))
])
dataset = FashionMNIST(dataroot, img_size, transform=transform)
data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

# for images, labels in data_loader:
#     fig, ax = plt.subplots(figsize=(18,10))
#     ax.set_xticks([])
#     ax.set_yticks([])
#     ax.imshow(make_grid(images, nrow=16).permute(1,2,0))
#     break

class Generator(nn.Module):
    def __init__(self, generator_layer_size, z_size, img_size, class_num):
        super().__init__()        
        self.z_size = z_size
        self.img_size = img_size        
        self.label_emb = nn.Embedding(class_num, class_num)        
        self.model = nn.Sequential(
                                    nn.Linear(self.z_size + class_num, generator_layer_size[0]),
                                    nn.LeakyReLU(0.2, inplace=True),
                                    nn.Linear(generator_layer_size[0], generator_layer_size[1]),
                                    nn.LeakyReLU(0.2, inplace=True),
                                    nn.Linear(generator_layer_size[1], generator_layer_size[2]),
                                    nn.LeakyReLU(0.2, inplace=True),
                                    nn.Linear(generator_layer_size[2], self.img_size * self.img_size),
                                    nn.Tanh()
                                )
    
    def forward(self, z, labels):        
        # Reshape z
        z = z.view(-1, self.z_size)        
        # One-hot vector to embedding vector
        c = self.label_emb(labels)        
        # Concat image & label
        x = torch.cat([z, c], 1)
        # Generator out
        out = self.model(x)        
        return out.view(-1, self.img_size, self.img_size)
    
class Discriminator(nn.Module):
    def __init__(self, discriminator_layer_size, img_size, class_num):
        super().__init__()        
        self.label_emb = nn.Embedding(class_num, class_num)
        self.img_size = img_size        
        self.model = nn.Sequential(
                                    nn.Linear(self.img_size * self.img_size + class_num, discriminator_layer_size[0]),
                                    nn.LeakyReLU(0.2, inplace=True),
                                    nn.Dropout(0.3),
                                    nn.Linear(discriminator_layer_size[0], discriminator_layer_size[1]),
                                    nn.LeakyReLU(0.2, inplace=True),
                                    nn.Dropout(0.3),
                                    nn.Linear(discriminator_layer_size[1], discriminator_layer_size[2]),
                                    nn.LeakyReLU(0.2, inplace=True),
                                    nn.Dropout(0.3),
                                    nn.Linear(discriminator_layer_size[2], 1),
                                    nn.Sigmoid()
                                )

    def forward(self, x, labels):        
        # Reshape fake image
        x = x.view(-1, self.img_size * self.img_size)        
        # One-hot vector to embedding vector
        c = self.label_emb(labels)        
        # Concat image & label
        x = torch.cat([x, c], 1)        
        # Discriminator out
        out = self.model(x)        
        return out.squeeze()

# Define generator
generator = Generator(generator_layer_size, z_size, img_size, class_num).to(device)
# Define discriminator
discriminator = Discriminator(discriminator_layer_size, img_size, class_num).to(device)
# Loss function
criterion = nn.BCELoss()
# Optimizer
g_optimizer = torch.optim.Adam(generator.parameters(), lr=learning_rate)
d_optimizer = torch.optim.Adam(discriminator.parameters(), lr=learning_rate)

def generator_train_step(batch_size, discriminator, generator, g_optimizer, criterion):    
    # Init gradient
    g_optimizer.zero_grad()    
    # Building z
    z = Variable(torch.randn(batch_size, z_size)).to(device)    
    # Building fake labels
    fake_labels = Variable(torch.LongTensor(np.random.randint(0, class_num, batch_size))).to(device)    
    # Generating fake images
    fake_images = generator(z, fake_labels)    
    # Disciminating fake images
    validity = discriminator(fake_images, fake_labels)    
    # Calculating discrimination loss (fake images)
    g_loss = criterion(validity, Variable(torch.ones(batch_size)).to(device))    
    # Backword propagation
    g_loss.backward()    
    #  Optimizing generator
    g_optimizer.step()    
    
    return g_loss.data

def discriminator_train_step(batch_size, discriminator, generator, d_optimizer, criterion, real_images, labels):    
    # Init gradient 
    d_optimizer.zero_grad()
    # Disciminating real images
    real_validity = discriminator(real_images, labels)    
    # Calculating discrimination loss (real images)
    real_loss = criterion(real_validity, Variable(torch.ones(batch_size)).to(device))    
    # Building z
    z = Variable(torch.randn(batch_size, z_size)).to(device)    
    # Building fake labels
    fake_labels = Variable(torch.LongTensor(np.random.randint(0, class_num, batch_size))).to(device)    
    # Generating fake images
    fake_images = generator(z, fake_labels)    
    # Disciminating fake images
    fake_validity = discriminator(fake_images, fake_labels)    
    # Calculating discrimination loss (fake images)
    fake_loss = criterion(fake_validity, Variable(torch.zeros(batch_size)).to(device))    
    # Sum two losses
    d_loss = real_loss + fake_loss    
    # Backword propagation
    d_loss.backward()    
    # Optimizing discriminator
    d_optimizer.step()
    
    return d_loss.data

def Cond_GANs(epochs):
    for epoch in range(epochs):
        print('Starting epoch {}...'.format(epoch+1))
        for i, (images, labels) in enumerate(data_loader):
            # Train data
            real_images = Variable(images).to(device)
            labels = Variable(labels).to(device)
            # Set generator train
            generator.train()
            # Train discriminator
            d_loss = discriminator_train_step(len(real_images), discriminator,
                                              generator, d_optimizer, criterion,
                                              real_images, labels)

            # Train generator
            g_loss = generator_train_step(batch_size, discriminator, generator, g_optimizer, criterion)
        # Set generator eval
        generator.eval()
        print('g_loss: {}, d_loss: {}'.format(g_loss, d_loss))
        # Building z 
        z = Variable(torch.randn(class_num-1, z_size)).to(device)
        # Labels 0 ~ 8
        labels = Variable(torch.LongTensor(np.arange(class_num-1))).to(device)
        # Generating images
        sample_images = generator(z, labels).unsqueeze(1).data.cpu()
        # Show images
        grid = make_grid(sample_images, nrow=3, normalize=True).permute(1,2,0).numpy()
        plt.imshow(grid)
        plt.show()

if __name__ == '__main__':
    Cond_GANs(epochs)