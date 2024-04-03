import cv2
import numpy as np
import matplotlib.pyplot as plt

def noise_show(img_scr, var_ls, nrows = 2, fs = (20, 9)):
    """
        Input:
            img_scr: (array) image_source
            var_ls: (list of integer) the variances of random_noises
            nrows : number of rows in ploting
            fs (tuple): figsize
        Return:
            subplots of the noise_image
    """
    ncols = int(np.ceil(len(var_ls) / nrows))
    plt.figure(figsize = fs)
    k = 0
    for var in var_ls:
        plt.subplot(nrows, ncols, k+1)        
        noise = np.random.normal(0, var, img_scr.shape)
        noise = noise + img_scr
        noise = [np.uint8(i) for i in noise]
        plt.imshow(noise, 'gray')
        plt.title('Gaussian noise image with sigma = %s'%(var))
        k += 1
    plt.show()

def filter_strength_vary_show(img_scr, filter_strength_ls, nrows, fs):
    """
        This function returns a subplots with in n_rows of vary filter_strength affects,
        Input:
            img_scr (array) : source of image
            filter_strength_ls (list): list of filter_strength
            nrows (int) : number of rows to display
            fs (tuple of 2 number): figsize
    """
    ncols = int(np.ceil(len(filter_strength_ls) / nrows))
    plt.figure(figsize = fs)
    k = 0
    for h in filter_strength_ls:
        plt.subplot(nrows, ncols, k+1) 
        new_img = cv2.fastNlMeansDenoising(img_scr, h, h, 7, 21)
        plt.imshow(new_img)
        plt.title('filter_strength (h) = %s'%(h))
        k += 1
    plt.show()

def template_WindowSize_vary_show(img_scr, template_Window_Size_ls, nrows, fs):
    """
        This function returns a subplots with in n_rows of vary filter_strength affects,
        Input:
            img_scr (array) : source of image
            template_Window_Size_ls (list): list of templateWindowSize
            nrows (int) : number of rows to display
            fs (tuple of 2 number): figsize
    """
    ncols = int(np.ceil(len(template_Window_Size_ls) / nrows))
    plt.figure(figsize = fs)
    k = 0
    for temp in template_Window_Size_ls:
        plt.subplot(nrows, ncols, k+1) 
        new_img = cv2.fastNlMeansDenoising(img_scr, 40, 40, temp, 21)
        plt.imshow(new_img)
        plt.title('template_Window_Size = %s'%(temp))
        k += 1
    plt.show()

def search_WindowSize_vary_show(img_scr, search_Window_Size_ls, nrows, fs):
    """
        This function returns a subplots with in n_rows of vary filter_strength affects,
        Input:
            img_scr (array) : source of image
            search_Window_Size_ls (list): list of searchWindowSize
            nrows (int) : number of rows to display
            fs (tuple of 2 number): figsize
    """
    ncols = int(np.ceil(len(search_Window_Size_ls) / nrows))
    plt.figure(figsize = fs)
    k = 0
    for sws in search_Window_Size_ls:
        plt.subplot(nrows, ncols, k+1) 
        new_img = cv2.fastNlMeansDenoising(img_scr, 40, 40, 7, sws)
        plt.imshow(new_img)
        plt.title('search_Window_Size = %s'%(sws))
        k += 1
    plt.show()

def sigma_gaussianblur_vary_show(img_scr, sigma_ls, nrows, fs):
    """
        This function returns a subplots with in n_rows of vary filter_strength affects,
        Input:
            img_scr (array) : source of image
            sigma_ls (list of tuple): list of tuple(sigma_x, sigma_y)
            nrows (int) : number of rows to display
            fs (tuple of 2 number): figsize
    """
    ncols = int(np.ceil(len(sigma_ls) / nrows))
    plt.figure(figsize = fs)
    k = 0
    for sigma in sigma_ls:
        plt.subplot(nrows, ncols, k+1) 
        new_img = cv2.GaussianBlur(img_scr, sigma, 14)
        plt.imshow(new_img)
        plt.title('(sigma_X, sigma_Y) = (%s, %s)'%(sigma))
        k += 1
    plt.show()

def ksize_gaussianblur_vary_show(img_scr, ksize_ls, nrows, fs):
    """
        This function returns a subplots with in n_rows of vary filter_strength affects,
        Input:
            img_scr (array) : source of image
            ksize_ls (list of tuple): list of ksizes
            nrows (int) : number of rows to display
            fs (tuple of 2 number): figsize
    """
    ncols = int(np.ceil(len(ksize_ls) / nrows))
    plt.figure(figsize = fs)
    k = 0
    for ks in ksize_ls:
        plt.subplot(nrows, ncols, k+1) 
        new_img = cv2.GaussianBlur(img_scr, (7, 7), ks)
        plt.imshow(new_img, 'gray')
        plt.title('ksize = %s'%(ks))
        k += 1
    plt.show()