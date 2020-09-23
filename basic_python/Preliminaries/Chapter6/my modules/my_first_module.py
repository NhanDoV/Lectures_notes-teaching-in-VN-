# calculate mean
def mean(data):
    """
        This function is used to find the mean of the input data (list / array)
    """
    trung_binh = 0
    for x in data:
        trung_binh += x / len(data)
    return trung_binh

def variance_hc(data):
    """ 
        This function is used to find the adjusted_variance of your data
    """
    phuong_sai = 0
    for x in data:
        phuong_sai += (x - mean(data))**2 / (len(data) - 1)
    return phuong_sai

def standard_deviation(data):
    """
        Ham nay duoc viet de tinh do lech chuan cho phuong sai hieu chinh
    """
    import math
    return math.sqrt(variance_hc(data))

def phan_vi(data, alpha):
    """
        Ham nay duoc su dung de tinh phan vi voi cac tham so:
            data (list or array of the numeric)
            alpha : must be in (0, 1) is the quantiles level
    """
    data.sort()   ## sap xep du lieu theo tu tu tang dan
    n = len(data) ## tinh so phan tu trong du~ lieu
    p = int(alpha*n/100)
    return data[p] + (alpha*n/100 - p - 0.5)*(data[p+1] - data[p])


def mode(data):
    """
        Ham nay se tra ra mode: gia tri xuat hien nhieu lan nhat trong du lieu
        hoac tra ra thong bao khong ton tai mode (co it nhat 2 gia tri co tan suat cao nhat)
    """
    import numpy as np
    def count(data, value):
        dem = 0
        for vrs in data:
            if vrs == value:
                dem += 1
        return dem
    data_unique = np.unique(data)  ## tao ra cac gia tri duy nhat: distinct values
    dem_giatri = [count(data, vl) for vl in data_unique]
    
    ## Bien luan max co duy nhat?
    count_max = max(dem_giatri)
    if count(dem_giatri, count_max) == 1:
        position_index = dem_giatri.index(count_max)
        data_mode = data_unique[position_index]
    else:
        print("Du lieu nay khong co mode")
    print("So %s xuat hien %s lan trong du lieu nay!"%(data_mode, count_max))
    return data_mode

def box_plot_info(data):
    """ 
        Ham nay chua cac thong tin co ban cua 1 boxplot gom`:
            Tu phan vi: Q1, Q2, Q3
            IQR = (Q3 - Q1)
            max, min
            outliers
    """
    data_max = max(data)
    data_min = min(data)
    Q1 = phan_vi(data, 25)
    Q2 = phan_vi(data, 50)
    Q3 = phan_vi(data, 75)
    IQR = Q3 - Q1
    outliers = []
    for outlier in data:
        if ((outlier < max(data_min, Q1 - 1.5*IQR)) or (outlier > min(data_max, Q3 + 1.5*IQR) ) ) :
            outliers.append(outlier)
    return outliers