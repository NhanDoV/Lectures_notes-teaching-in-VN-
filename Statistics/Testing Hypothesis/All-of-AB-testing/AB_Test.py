from scipy.stats import norm

def find_sample_size(alpha=0.05, beta=0.2, Base_rt=0.3, MDE_Rt=0.45):
    """
        Xác định sample size khi có các nhân tố 
            MDE_rate : minimum detectable effort rate
            Base_rt: Baseline conversion rate
            alpha: 
            beta:    
    """
    za = norm.ppf(alpha/2)
    zb = norm.ppf(beta)

    return (za*(2*Base_rt*(1-Base_rt))**0.5 + zb*(Base_rt*(1-Base_rt) + MDE_Rt*(1-MDE_Rt))**0.5 )**2 / (MDE_Rt - Base_rt)**2

def permutation_sample(data1, data2):
    """Chia tách dữ liệu bằng cách ghép 2 dữ liệu rồi tạo ra hoán vị trên chúng"""
    data = np.concatenate((data1, data2))

    # Hoán vị các phần tử
    permuted_data = np.random.permutation(data)

    perm_sample_1 = permuted_data[: len(data1)]
    perm_sample_2 = permuted_data[len(data1): ]

    return perm_sample_1, perm_sample_2

def confidence_interval(alpha, alternative='two.side'):
    """
    
    """
    pass