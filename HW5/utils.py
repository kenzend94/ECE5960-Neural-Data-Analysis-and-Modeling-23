import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import diagsvd
from scipy.io import loadmat

# Gets mat data frames at certain indices.
def get_data(f_i=0, f_e=None, idxs=None, \
    data_file="windowedSpikes.mat", data_keys=['data']):
    data_pth = f"data/{data_file}"
    
    f_e = f_e+1 if f_e is not None else f_e
    
    if(len(data_keys) == 1):
        return loadmat(data_pth)[data_keys[0]][idxs,:] if idxs is not None else \
            loadmat(data_pth)[data_keys[0]][f_i:(f_e),:]
    data = []
    for data_k in data_keys:
        data.append(loadmat(data_pth)[data_k][idxs,:] if idxs is not None else \
            loadmat(data_pth)[data_k][f_i:(f_e),:])
    return tuple(data)

# Returns the projection component and vector of v along normal vector u.
def get_proj_vec(v, u):
    comp = np.dot(v, u.T)
    return comp, comp*u

# Returns the rejection of vector v on u.
def get_rej_vec(v, u):
    return v-get_proj_vec(v,u)

# Returns vector components of vector v projection on u
def proj_vec(v, u):
    proj_v = get_proj_vec(v, u)
    return proj_v, v-proj_v

# Get magnitude of vector
def get_vec_len(v):
    return np.linalg.norm(v)

# Returns random vector
def get_rand_vec(dim=2):
    return np.random.rand(dim)*(np.random.randint(1,5)) + 0.01

# Gets a list of size n of random col vectors of dimension dim. 
def get_rand_vec_list(n,dim):
    return [get_rand_vec(dim=dim) for _ in range(n)]

# Setup subplot.
def setup_subplot(
    title=None,
    subplot_titles=None,
    ylabels = None,
    xlabels = None,
    nrows=1,
    ncols=2,
    figsize=[10,10],
    sharey=False,
    sharex=False
    ):
    
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, sharey=sharey, sharex=sharex)
    fig.set_figwidth(figsize[0]); fig.set_figheight(figsize[1])
    if title is not None: fig.suptitle(title)
    if subplot_titles is not None and len(axs.flat) == len(subplot_titles):
        for i, ax in enumerate(axs.flat):
            ax.set_title(subplot_titles[i])
    if ylabels is not None and len(axs.flat) == len(ylabels):
        for i, ax in enumerate(axs.flat):
            ax.set_ylabel(ylabels[i])
    if xlabels is not None and len(axs.flat) == len(xlabels):
        for i, ax in enumerate(axs.flat):
            ax.set_xlabel(xlabels[i])
    return fig, axs

# Get Histogram mean.  
def get_hist_mean(heights, x):
    return np.sum(heights)/np.sum(heights*x), np.sum(heights*x)/np.sum(heights)

'''
Approximates an N-dimensioanl Gaussian distribution 
    with the specified mean and covariance and returns num samples.
''' 
def ndRandn(mean, cov, num=1):
    
    def gaussian_approx(M, b_vect, N):
        w_vect = np.random.randn(N)
        return M@w_vect + b_vect
    
    N = mean.shape[0]

    _, S,VT = np.linalg.svd(cov); S = diagsvd(S,cov.shape[0], cov.shape[1])
    M = VT.T@S.T # C = D.T@D = V@S.T@S@V.T
    idxs = M < 0
    M = np.sqrt(np.abs(M)); M[idxs] *= -1
    
    # M = np.abs(np.sqrt(cov + 0j)) # cov = M*M.T, cov ~= M^2
    # M[idxs] *= -1
    return np.array([gaussian_approx(M, mean, N) for _ in range(num)])