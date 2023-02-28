import numpy as np

c = 299792458.0                       # [m/s]
hbar = 6.582119569e-16                # [eV.s]
alpha_pref = np.sqrt(2) / (hbar * c)  # [1/m]

def average_epsilon_qe(re_eps, im_eps, fname):
    eneg = re_eps[:, 0]
    ave_re_eps = np.mean(re_eps[:, 1:], axis=1)
    ave_im_eps = np.mean(im_eps[:, 1:], axis=1)

    with open(fname, 'w+') as f:
        f.write('# omega (eV)     <Re(Eps)>     <Im(Eps)>\n')
        for i in range(len(eneg)):
            f.write(f'{eneg[i]:.8f}    {ave_re_eps[i]:.8f}    {ave_im_eps[i]:.8f}\n')
        f.write('\n')

def refractive_index(eps1, eps2):
    eps = np.sqrt(eps1 * eps1 + eps2 * eps2)
    return np.sqrt((eps + eps1) / 2)

def extinction_index(eps1, eps2):
    eps = np.sqrt(eps1 * eps1 + eps2 * eps2)
    return np.sqrt((eps - eps1) / 2)

def absorption_coefficient(energy, eps1, eps2):
    eps = np.sqrt(eps1 * eps1 + eps2 * eps2)
    return alpha_pref * energy * np.sqrt(eps - eps1)

def optical_properties(energy, eps1, eps2, fname):
    n = refractive_index(eps1, eps2)
    kappa = extinction_index(eps1, eps2)
    alpha = absorption_coefficient(energy, eps1, eps2)

    with open(fname, 'w+') as f:
        f.write('# omega(eV)     n     kappa     alpha(1/m)\n')
        for i in range(len(energy)):
            f.write(f'{energy[i]:.8f}     {n[i]:.8f}     {kappa[i]:.8f}     {alpha[i]:.8f}\n')
        f.write('\n')
