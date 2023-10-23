#coding=utf-8
import torch.nn.functional as F
import torch
import torch
from torchvision import transforms, utils
from torch.utils.data import Dataset, DataLoader
import numpy as np
import torch.optim as optim
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#------------------数据集设置
root ="G:/Arc_detection/arc_dataset/train/"
root1 = "G:/Arc_detection/arc_dataset/test/"


#定义读取文件格式的代码
def default_loader(path):
	return np.loadtxt(path,dtype=float)
class MyDataset(Dataset):
	def __init__(self,txt,transform = None, target_transform = None,loader = default_loader):
		super(MyDataset, self).__init__()
		fh = open(txt,'r')
		time_series = []
		for line in fh:
			line = line.strip('\n')
			line = line.rstrip('\n')
			words = line.split()
			time_series.append((words[0],int(words[1])))

		self.time_series = time_series
		self.transform = transform
		self.target_transform = target_transform
		self.loader = loader

	def __getitem__(self, index):
		fn, label = self.time_series[index]
		time_data = self.loader(fn)
		time_data = torch.Tensor(time_data)


		return torch.unsqueeze(time_data, dim=0), label
	def __len__(self):
		return len(self.time_series)

train_transforms = None
val_transforms = None
test_transforms = None

train_data = MyDataset(txt = root+'train.txt',transform=None)
val_data = MyDataset(txt=root1+'test.txt',transform=None)
test_data = MyDataset(txt=root1+'test.txt',transform=None)

train_loader = DataLoader(dataset=train_data,batch_size=8,shuffle=True,num_workers=0,drop_last=True)
val_loader = DataLoader(dataset=test_data,batch_size=8,shuffle=True,num_workers=0,drop_last=True)
test_loader = DataLoader(dataset=test_data,batch_size=8,shuffle=True,num_workers=0,drop_last=True)


print(len(train_data))
print(len(train_loader))
