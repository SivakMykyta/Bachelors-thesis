import torch

if torch.cuda.is_available():
    print("CUDA je k dispozici")
else:
    print("CUDA neni k dispozici")
