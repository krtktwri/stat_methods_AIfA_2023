import matplotlib.pyplot as plt 
import numpy as np


def plot_scatter_2D(x, y, z):
    """
    Making a three 2D scatter plots of the sampled points
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))
    ax1.scatter(x, y, s=0.5)
    ax1.set_title('XY-plane')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(alpha=0.4)
    ax2.scatter(x, z, s=0.5)
    ax2.set_title('XZ-plane')
    ax2.set_xlabel('x')
    ax2.set_ylabel('z')
    ax2.grid(alpha=0.4)
    ax3.scatter(y, z, s=0.5)
    ax3.set_title('YZ-plane')
    ax3.set_xlabel('y') 
    ax3.set_ylabel('z')
    ax3.grid(alpha=0.4)
    
def plot_histogram(x, y, z):
    """
    Plotting histograms of the sampled points
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))
    ax1.hist(x, bins=100, alpha=0.5, label='x')
    ax1.set_xlabel('x')
    ax2.hist(y, bins=100, alpha=0.5, label='y')
    ax2.set_xlabel('y')
    ax3.hist(z, bins=100, alpha=0.5, label='z')
    ax3.set_xlabel('z')
    
# Additional Functions
def plot_scatter_3D(correct, incorrect):
    """
    Making a 3D scatter plot of the sampled points
    """
    x, y, z = incorrect
    x_correct, y_correct, z_correct = correct
    fig = plt.figure(figsize=plt.figaspect(0.5)) 
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.scatter(x, y, z, s=0.4);
    ax.set_box_aspect((np.ptp(x), np.ptp(y), np.ptp(z)))
    ax.set_title('Points Bunched Near Poles')
    
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.scatter3D(x_correct, y_correct, z_correct, s=0.4);
    ax.set_box_aspect((np.ptp(x_correct), np.ptp(y_correct), np.ptp(z_correct)))  
    ax.set_title('Evenly Distributed Points')
    plt.show()