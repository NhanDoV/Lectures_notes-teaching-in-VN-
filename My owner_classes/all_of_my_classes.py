import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#======================= DEFINE KERNEL FUNCTION =========================
def rect_kernel(t):
    """
        rectangle shape
    """
    return 0.5 * (abs(t) <= 1)

def biw_kernel(t):
    """
        bi-weight kernel
    """
    return (15/16)*(1-t**2)**2*(abs(t) <= 1)

def trig_kernel(t):
    """
        Triangular kernel
    """
    return (1 - abs(t))*(abs(t) <= 1)

def epa_kernel(t):
    """
        Epanechnikov kernel
    """
    return 0.75*(1 - t**2)*(abs(t) <= 1)

def gau_kernel(t):
    """
        Gaussian kernel
    """
    return (1/np.sqrt(2*np.pi))*np.exp(-t**2/2)

def silv_kernel(t):
    """
        Silverman kernel    
    """
    return 0.5*np.exp(-abs(t / np.sqrt(2)))*np.sin(abs(t / np.sqrt(2)) + np.pi/4)

def sigm_kernel(t):
    """ 
        Sigmoid kernel
    """
    pi = np.pi
    return 2/(pi*(np.exp(t) + np.exp(-t)))

def logis_kernel(t):
    """
        Logistic kernel
    """
    return 1/(2 + np.exp(t) + np.exp(-t))

def tricube_kernel(t):
    """
        Tricube kernel
    """
    return (70/81)*((1 - abs(t**3))**3)*(abs(t) <= 1)

## Define the class
class kernel_density_est:
    """ 
        ***********************************************************************
        *    This class used for:
        *        - 1) Find the optimal_bins
        *        - 2) Display many k.d.e with different type of kernel_function
        *        - 3) Given the ecdf of the data.
        *    
        *     of the 1-D data input.
        ************************************************************************
        * Parameters :
        *-------------------------------------------------------------------------
        *     data : must be 1-D dataset
        *     kernel_type (str): type of kernel, can be {"gauss", "bi-weight", "rectangle".
        *                                               "triangle", "Epanechnikov", "silverman",
        *                                               "sigmoid", "logistic", "tri-cube"}
        *     normed : normed your kde and histogram or not?
        *------------------------------------------------------------------------------------------------
        * Attributes:
        * -----------------
        *    get_params: returns the parameters in this class
        *    get_bins: returns the bins-width of histogram_kde
        *    display : show the kde
        *    show_ecdf: display the empirical cummulative distribution function
        *************************************************************************
    """
    def __init__(self, data, kernel_type = "gauss", normed = True):
        
        self.data = data
        self.kernel_type = kernel_type
        self.normed = normed
        
    def get_params(self):
        """ Returns the initial parameters """
        return {'kernel': self.kernel_type, 'normed': self.normed}
    
    def get_bins(self):
        return 1 / np.sqrt(len(self.data))
    
    def display(self):
        n = len(self.data)
        h = self.get_bins()
        is_normed = self.normed
        
        kde_constant = (1 / (2*n*h))**(is_normed)
        kernel_type = self.kernel_type
        
        u = np.linspace(min(self.data), max(self.data), 1000)
        kde = np.zeros(len(u))
        
        for x_k in self.data:
            if kernel_type == "gauss":
                kde = kde + gau_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "bi-weight":
                kde = kde + biw_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "rectangle":
                kde = kde + rect_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "triangle":
                kde = kde + trig_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "Epanechnikov":
                kde = kde + epa_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "silverman":
                kde = kde + silv_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "tricube":
                kde = kde + tricube_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "sigmoid":
                kde = kde + sigm_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "logistic":
                kde = kde + logis_kernel((x_k -  u)/h) * kde_constant
            else:
                raise TypeError("No kernel named: "+str(kernel_type))
        
        
        plt.plot(u, kde, '-', label = 'kde')
        plt.title('kernel = '+str(kernel_type))
        plt.xlabel("normed = "+str(is_normed))
                
    def show_ecdf(self):
        """
            Display the ecdf (empirical cumulative distribution function)
        """
        x = self.data
        x = np.sort(x)
        n = len(x)
        y = np.arange(1, n + 1, 1) / n
        plt.plot(x, y, label = 'ecdf')
        plt.legend()
    plt.show()

#============================================
from sklearn.base import clone 
from itertools import combinations
from sklearn.metrics import accuracy_score
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split

class Sequential_Backwar_Selection:
    """

    """
    def __init__(self, estimator, k_features, scoring=accuracy_score,                 
                 test_size=0.25, random_state=1):        
 
        self.scoring = scoring        
        self.estimator = clone(estimator)        
        self.k_features = k_features        
        self.test_size = test_size
        self.random_state = random_state
        
    def fit(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = self.test_size, 
                                                             random_state = self.random_state)
        dim = X_train.shape[1]        
        self.indices_ = tuple(range(dim))        
        self.subsets_ = [self.indices_]        
        score = self._calc_score(X_train, y_train, X_test, y_test, self.indices_)        
        self.scores_ = [score]
        while dim > self.k_features:            
            scores = []            
            subsets = []
            for p in combinations(self.indices_, r=dim - 1):                
                score = self._calc_score(X_train, y_train, X_test, y_test, p)
                scores.append(score)
                subsets.append(p)
            best = np.argmax(scores)
            self.indices_ = subsets[best]
            self.subsets_.append(self.indices_)            
            dim -= 1 
            self.scores_.append(scores[best])
        self.k_score_ = self.scores_[-1]
        return self
    def transform(self, X):        
        return X[:, self.indices_]
    def _calc_score(self, X_train, y_train, X_test, y_test, indices):        
        self.estimator.fit(X_train[:, indices], y_train)        
        y_pred = self.estimator.predict(X_test[:, indices])        
        score = self.scoring(y_test, y_pred)        
        return score    
    
from scipy.stats import norm, t, chisquare

# Hypothesis class 
class prop_testing:
    """
        Importance parameters:
            alternative = {"equal (two_side)", "lower_tail (less)", "upper_tail (greater)"}
            alpha (float in [0, 1]) = significance level / then (1 - alpha) be the confidence_level
    """
    def __init__(self, alpha, alter = "equal"):
        self.alpha = alpha
        self.alter = alter
    
    def prop_1_test(self, n, y, p0):
        """
            p0: theorictic_proportion
            n: sample size
            y: total the elements in population that satisfies a property
        """
        p_hat = y / n # proportion in empirical sample
        Z0 = (p_hat - p0)/np.sqrt(( p0 * (1 - p0))/n) # statistical testing'
        
        # for two_sided alternative
        if self.alter == "equal":
            p_value = 1 - norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha / 2))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [p_hat - dung_sai, p_hat + dung_sai]
            alter = "p = p0 (equal)"
            
        # if alternative = "p < p0"
        elif self.alter == "less":
            p_value = norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [0, p_hat + dung_sai]
            alter = "p < p0 (less)"
            
        elif self.alter == "greater":
            p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [p_hat - dung_sai, 1]
            alter = "p > p0 (greater)"
        else:
            raise ValueError("no alternative like %s, please type help to get more details"%format(alter))
        
        if p_value < self.alpha:
            claim = "Reject H0"
        else:
            claim = "Not engough evidence to reject H0"
            
        return {'p_value': p_value, 
                "statistical_testing": Z0,
                'sample_estimates': p_hat, 
                "conf_interval": conf_int,
                "final_claim": claim,
                "alternative": alter
               }
    
    def prop_2_test(self, n1, n2, y1, y2):
        """
            n1, n2: sample_size of 2 samples
            y1, y2: total the elements in population that satisfies a property
        """
        p1_hat = y1 / n1
        p2_hat = y2 / n2
        p_hat = (y1 + y2) / (n1 + n2)
        Z0 = (p1_hat - p2_hat) / np.sqrt(p_hat*(1 - p_hat)*( 1/n1 + 1/n2))
        diff_prop = p1_hat - p2_hat
        
        # for two_sided alternative
        if self.alter == "equal":
            p_value = 1 - norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha / 2))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [diff_prop - dung_sai, diff_prop + dung_sai]
            alter = "p = p0 (equal)"
            
        # if alternative = "p < p0"
        elif self.alter == "less":
            p_value = norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [0, diff_prop + dung_sai]
            alter = "p < p0 (less)"
            
        elif self.alter == "greater":
            p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [diff_prop - dung_sai, 1]
            alter = "p > p0 (greater)"
        else:
            raise ValueError("no alternative like %s, please type help to get more details"%format(alter))
        
        if p_value < self.alpha:
            claim = "Reject H0"
        else:
            claim = "Not engough evidence to reject H0"
            
        return {'p_value': p_value, 
                "statistical_testing": Z0,
                'sample_estimates (prop_samp1, prop_samp2)': (p1_hat, p2_hat), 
                "conf_interval": conf_int,
                "final_claim": claim,
                "alternative": alter
               }
    
## independent test
    
#============================================
class Polynomial_Univariate_Regression:
    """
        This class is used to solve the polynomial assumption of univariate-regression

                Y = a0 + a1 X + a2 X^2 + ... + a_d X^d
    """
    def __init__(self, X, y, deg):
        self.X = np.array(X)
        self.y = np.array(y)
        self.deg = deg
        
    def coef(self):
        coefs = np.polyfit(self.X, self.y, self.deg)
        return coefs
    
    def predict(self):
        coefs = self.coef()
        X_bar = np.array([self.X**k for k in range(self.deg + 1)])
        y_pred = np.sum(np.array(coefs.reshape(-1, 1)*X_bar), axis = 0)
        return y_pred

    def MSE_score(self):
        coefs = self.coef()
        y_pred = self.predict()
        return np.mean([(self.y[k] - y_pred[k])**2 for k in range((np.array(self.X).shape[0]))])
    
    def R2_score(self):
        coefs = self.coef()
        y_pred = self.predict()
        
        # sum of square_error
        SSE = np.sum([(self.y[k] - y_pred[k])**2 for k in range((np.array(self.X).shape[0]))])
        
        # total_sum of square = SSE + Sum_squared_regression
        SST = SSE + np.sum([(y_pred[k] - np.mean(self.y))**2 for k in range((np.array(self.X).shape[0]))])
        
        return 1 - (SSE / SST)
    
    def plot(self):
        coefs = self.coef()
        y_pred = self.predict()
        plt.plot(self.X, self.y, '*', label = 'actual')
        plt.plot(self.X, y_pred, '--', label = 'pred')
        plt.legend()
        plt.plot()

#========================== cartoon transformation
#
#       See more: https://github.com/NhanDoV/All-of-my-projects./tree/main/Jan2022-Jan2024/4.%20Cartoon-transform-sketch
#        
#=======================================================================#
import cv2
from sklearn.cluster import KMeans

def KMean_transform(img, nb_clusters=6):
    """
        Image segmentation is the classification of an image into different groups. 
        Many kinds of research have been done in the area of image segmentation 
        using clustering, here is KMeans.
        This will reduce the number of color-range from the original images and make
        your output look like a cartoon image.
    """
    ## Flatten the image_array
    X = img.reshape((img.shape[0]*img.shape[1], img.shape[2]))
    kmeans = KMeans(n_clusters = nb_clusters)
    kmeans.fit(X)

    ## create labels and centroids
    label = kmeans.predict(X)
    temp_img = np.zeros_like(X)

    # replace each pixel by its center
    for k in range(nb_clusters):
        centroids_val =  np.uint8(kmeans.cluster_centers_[k])
        temp_img[label == k] = centroids_val 

    out_img = temp_img.reshape(img.shape[0], img.shape[1], img.shape[2])

    return out_img

def smoothing_image(img, size=(960, 640)):
    """
        Smoothing image by using median-bluring into the gray-scale image
    """
    ReSized1 = cv2.resize(img, size)

    # converting an image to grayscale
    grayScaleImage= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, size)

    # applying median blur to smoothen an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, size)

    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9)

    ReSized4 = cv2.resize(getEdge, size)

    return ReSized1, getEdge, ReSized4

def to_cartoon(ImagePath, nb_clusters, size=(960, 640)):
    """
        Wrapping up all the techniques (gray-scale + Smoothing + KMeans-clustering)
    """
    # read the image
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
    #print(image)  # image is stored in form of numbers

    # retrieving the edges for cartoon effect by using thresholding technique
    ReSized1, getEdge, ReSized4 = smoothing_image(originalmage, size)

    # applying bilateral filter to remove noise & keep edge sharp as required
    colorImage = cv2.bilateralFilter(originalmage, 5, 300, 300)
    ReSized5 = cv2.resize(colorImage, size)
    
    # masking edged image with our "BEAUTIFY" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    ReSized6 = KMean_transform(cv2.resize(cartoonImage, size), nb_clusters)

    return ReSized6