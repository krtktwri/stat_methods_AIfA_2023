import numpy as np

## Incorrect Sampling Functions (The error sets in because of the phi dependence of the area element)

def sample_sphere(n):
    theta = np.random.uniform(0, 2*np.pi, n)
    phi = np.random.uniform(0, np.pi, n)
    return theta, phi

def get_cartesian_coords(phi, theta, r = 1):
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return x, y, z

## Correct Sampling Function 

def sample_sphere_correct(n):
    u = np.random.uniform(-1, 1, n)
    theta = np.random.uniform(0, 2*np.pi, n)
    
    x = np.sqrt(1 - u**2) * np.cos(theta)
    y = np.sqrt(1 - u**2) * np.sin(theta)
    z = u
    return x, y, z
