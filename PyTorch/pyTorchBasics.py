import torch

data = [[1,2,3,4],[3,4,5,6]] #Create a 2D array
x_data = torch.tensor(data) #Converting the 2D array to tensor
x_rand = torch.rand_like(x_data, dtype=torch.float) #Converting above numbers to random floating numbers

print(x_data)


print(x_rand)



'''
class MagicModel(nn.Module):
    def __init__(self):
        super(MagicModel, self).__init__()
        self.linear = nn.Linear(1,1)

    def forward(self, x):
        return self.linear(x)
    
model = MagicModel()
print(model)
'''
