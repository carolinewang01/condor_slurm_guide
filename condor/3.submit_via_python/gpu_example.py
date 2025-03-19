#!/usr/bin/env python

import torch
import time

def main():
    # Check if CUDA is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    if torch.cuda.is_available():
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
        print(f"GPU Memory Usage:")
        print(f"Allocated: {torch.cuda.memory_allocated(0)/1024**2:.2f} MB")
        print(f"Cached: {torch.cuda.memory_reserved(0)/1024**2:.2f} MB")
    
    # Create a large tensor and perform some operations
    size = 5000
    print(f"\nCreating {size}x{size} matrices...")
    
    # Matrix multiplication on GPU
    start_time = time.time()
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)
    c = torch.matmul(a, b)
    end_time = time.time()
    
    print(f"Matrix multiplication completed in {end_time - start_time:.2f} seconds")
    print(f"Result shape: {c.shape}")
    print(f"Result device: {c.device}")

if __name__ == "__main__":
    main()
