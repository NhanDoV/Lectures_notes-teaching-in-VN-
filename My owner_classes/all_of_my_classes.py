import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import t, norm
from scipy.stats import norm, t, chisquare

# ===================================== STATISTICAL TESTING HYPOTHESIS =========================================
# Hypothesis class 
class prop_testing:
    """
        Input parameters:
            alternative = {"equal (two_side)", "lower_tail (less)", "upper_tail (greater)"}
            alpha (float in [0, 1]) = significance level / then (1 - alpha) be the confidence_level
        =================================================================================
        Attributes:
            prop_1_test(n, y, p0)
            prop_2_test(n1, n2, p1, p2)
        =================================================================================
        Example
            >> my_prop_test = prop_testing(alter='two_side', alpha=0.05)
            >> my_prop_test.prop_1_test(n=800, y=600, p0=0.77)
            -----------------------
                0.17888190308175522
                {'p_value': 0.17888190308175522,
                 'statistical_testing': -1.3442056254199006,
                 'sample_estimates': 0.75,
                 'conf_interval': [0.7199943020227793, 0.7800056979772207],
                 'final_claim': 'Not engough evidence to reject H0',
                 'alternative': 'p != p0 (not.equal)'}
            -----------------------
            # Testing tỷ lệ 2 mẫu
            >> my_prop_test.prop_2_test(n1=600,n2=800,y1=350,y2=390)
            -----------------------
                {'p_value': 0.00037828752742052885,
                 'statistical_testing': 3.5547855260901673,
                 'sample_estimates (prop_samp1, prop_samp2)': (0.5833333333333334, 0.4875),
                 'conf_interval': [0.043337122902925504, 0.14832954376374125],
                 'final_claim': 'Reject H0',
                 'alternative': 'p != p0 (not.equal)'}         
    """
    def __init__(self, alpha, alter = "equal"):
        valid_alter = ["less", "equal", "greater", "two_side", "lower_tail", "upper_tail"]
        self.alpha = alpha
        self.alter = alter
        if alter not in valid_alter:
            raise ValueError("Alternative (đối thuyết) phải là một trong các dạng sau đây,\n", valid_alter)
        if (alpha < 0) or (alpha > 1):
            raise ValueError("Mức ý nghĩa (significance level) alpha phải nằm trong (0, 1)")
    
    def prop_1_test(self, n, y, p0):
        """
            Testing tỷ lệ cho cùng một mẫu
            Input params:
                p0: theorictic_proportion
                n: sample size
                y: total the elements in population that satisfies a property
            Lý thuyết:
                ************************************************************************
                |   Case   |      Test statistics (Z0)        |        p_value         |
                |----------|----------------------------------|------------------------|
                | two_side | (p.hat - p0) / sqrt(p0*(1-p0)/n) | 2 min(P(Z<Z0), P(Z>Z0))|
                | less     | (p.hat - p0) / sqrt(p0*(1-p0)/n) | P(Z < Z0)              |
                | greater  | (p.hat - p0) / sqrt(p0*(1-p0)/n) | P(Z > Z0)              |
                ************************************************************************     
        """
        p_hat = y / n # proportion in empirical sample
        Z0 = (p_hat - p0)/np.sqrt(( p0 * (1 - p0))/n) # statistical testing'
        
        # for two_sided alternative
        if self.alter in ["equal", "two_side"]:
            p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            dung_sai = abs(norm.ppf(self.alpha / 2))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [p_hat - dung_sai, p_hat + dung_sai]
            alter = "p != p0 (not.equal)"
            
        # if alternative = "p < p0"
        elif self.alter in ["less", "lower_tail"]:
            p_value = norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [0, p_hat + dung_sai]
            alter = "p < p0 (less)"
            
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [p_hat - dung_sai, 1]
            alter = "p > p0 (greater)"
        print(p_value)
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
            Testing tỷ lệ cho 2 mẫu
            Input params:
                n1, n2: sample_size of 2 samples
                y1, y2: total the elements in population that satisfies a property
            Lý thuyết:
                *********************************************************
                |   Case   |  Test statistics  |        p_value         |
                |----------|-------------------|------------------------|
                | two_side |        Z0         | 2 min(P(Z<Z0), P(Z>Z0))|
                | less     |        Z0         | P(Z < Z0)              |
                | greater  |        Z0         | P(Z > Z0)              |
                *********************************************************
            trong đó:
                Z0 = (p1_hat - p2_hat) / np.sqrt(p_hat*(1 - p_hat)*( 1/n1 + 1/n2))
            và
                p1 = y1 / n1
                p2 = y2 / n2
                p_hat = (y1 + y2) / (n1 + n2)            
        """
        p1_hat = y1 / n1
        p2_hat = y2 / n2
        p_hat = (y1 + y2) / (n1 + n2)
        Z0 = (p1_hat - p2_hat) / np.sqrt(p_hat*(1 - p_hat)*( 1/n1 + 1/n2))
        diff_prop = p1_hat - p2_hat
        
        # for two_sided alternative
        if self.alter in ["equal", "two_side"]:
            p_value =  2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            dung_sai = abs(norm.ppf(self.alpha / 2))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [diff_prop - dung_sai, diff_prop + dung_sai]
            alter = "p != p0 (not.equal)"
            
        # if alternative = "p < p0"
        elif self.alter in ["less", "lower_tail"]:
            p_value = norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [0, diff_prop + dung_sai]
            alter = "p < p0 (less)"
            
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [diff_prop - dung_sai, 1]
            alter = "p > p0 (greater)"
        
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
    
## testing on sample-mean
class mean_test:
    """
        Kiểm định trung bình của một / 2 mẫu với các giả định
            - 1 mẫu khi biết phương sai tổng thể (known variance)
            - 1 mẫu khi không biết phương sai tổng thể (Unknown variance)
            - 2 mẫu khi biết phương sai
        =====================================================================
        Attributes:
            avg_1sample(x, muy0, alter, sigma)
            unpaired_data_equal_var(x1, x2, muy1, muy2, alter, sigma)
            unpaired_data_non_equal_var(x1, x2, muy1, muy2, alter, sigma)
    """
    def __init__(self, alpha, alter = "equal", sigma="unknown"):
        valid_alter = ["less", "equal", "greater", "two_side", "lower_tail", "upper_tail"]
        self.alpha = alpha
        self.alter = alter
        self.sigma = sigma        
        if alter not in valid_alter:
            raise ValueError("Alternative (đối thuyết) phải là một trong các dạng sau đây,\n", valid_alter)
        if (alpha < 0) or (alpha > 1):
            raise ValueError("Mức ý nghĩa (significance level) alpha phải nằm trong (0, 1)")
        if (sigma != 'unknown') and (type(sigma) not in [int, float]) and (sigma != None):
            raise ValueError("giá trị hợp lệ của sigma là `unknown` hay một số thực cụ thể, e.g. 5.1, 1.0 ")
    
    def get_params(self):
        print(f"Alternative (đối thuyết): {self.alter}")
        print(f"significance value (alpha): {self.alpha}")
        print(f"sigma (giả thuyết phương sai): {self.sigma}")

    def avg_1sample(self, x, muy0):
        """
            Kiểm định giả thuyết trung bình của 1 mẫu
            ============================================
            kịch bản 1. alternative = 2 side
                *************************************************************************************************************
                |         Case             |           Test Statistic         |                    p.value                  |
                *************************************************************************************************************
                | X is normal, σ known     |(X.bar - muy) / (sigma / sqrt(n)) |2*min(P[X>Z0], 1-P[X>Z0]) where X is normal  |       
                | n_large, X is not normal |(X.bar - muy) / (std.X / sqrt(n)) |2*min(P[X>Z0], 1-P[X>Z0]) where X apprx norm |
                | X is normal, σ un-known  |(X.bar - muy) / (std.X / sqrt(n)) |2*min(P[X>Z0], 1-P[X>Z0]) where X is St(n-1) | 
                ************************************************************************************************************|
            trong đó
                St(n-1) là phân phối Student với n-1 bậc tự do
             ============================================
             kịch bản 2. alternative = greater
                 Được thực hiện tương tự như kịch bản 1, ta chỉ thay đổi p.value thành P[X > Z0], tức là                 
                *************************************************************************************************
                |         Case             |           Test Statistic         |               p.value           |
                *************************************************************************************************
                | X is normal, σ known     |(X.bar - muy) / (sigma / sqrt(n)) |P[X > Z0]     where X is normal  |      
                | n_large, X is not normal |(X.bar - muy) / (std.X / sqrt(n)) |P[X > Z0]     where X apprx norm |
                | X is normal, σ un-known  |(X.bar - muy) / (std.X / sqrt(n)) |P[X > Z0]     where X is St(n-1) | 
                ************************************************************************************************|                 
             ============================================
             kịch bản 3. alternative = less
                 Lúc này ta cũng chỉ thay đổi p.value thành P[X < Z0]
                *************************************************************************************************
                |         Case             |           Test Statistic         |               p.value           |
                *************************************************************************************************
                | X is normal, σ known     |(X.bar - muy) / (sigma / sqrt(n)) |P[X < Z0]     where X is normal  |      
                | n_large, X is not normal |(X.bar - muy) / (std.X / sqrt(n)) |P[X < Z0]     where X apprx norm |
                | X is normal, σ un-known  |(X.bar - muy) / (std.X / sqrt(n)) |P[X < Z0]     where X is St(n-1) | 
                ************************************************************************************************|       
            ==================================================================================================================
            Example
            >> obj = mean_test(alpha=0.05, alter='less', sigma=1)
            >> obj.avg_1sample([1,2,4,5], 3)
            ...........................
                Not enough evidence to reject H0
                {'p-value': 0.5, 'T_stats': 0.0}
            ==================================================================================================================                           
        """
        n = len(x)
        # Biện luận Test-statistics theo sigma
        if self.sigma != None:
            Z0 = (np.mean(x) - muy0) / (self.sigma / n**0.5)
            
            # Biện luận p_value theo các đối thuyết
            if self.alter in ["equal", "two_side"]:
                p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            elif self.alter in ["less", "lower_tail"]:
                p_value = norm.cdf(Z0)
            elif self.alter in ["greater", "upper_tail"]:
                p_value = 1 - norm.cdf(Z0)
            
        else:
            std_x = np.std(x)
            Z0 = (np.mean(x) - muy0) / (std_x / n**0.5)
            
            # trước khi biện luận theo đối thuyết cần chú ý kỹ giả thuyết sample-size 
            # vì nó tương ứng với Student hoặc normal distribution
            if n > 30:
                if self.alter in ["equal", "two_side"]:
                    p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
                elif self.alter in ["less", "lower_tail"]:
                    p_value = norm.cdf(Z0)
                elif self.alter in ["greater", "upper_tail"]:
                    p_value = 1 - norm.cdf(Z0)
            # Lúc này nó tương ứng với pp student n-1 bậc tự do
            # note: df meant degree of freedom
            else:
                if self.alter in ["equal", "two_side"]:
                    p_value = 2*min(1 - t.cdf(Z0), t.cdf(Z0, df=n-1))
                elif self.alter in ["less", "lower_tail"]:
                    p_value = t.cdf(Z0, df=n-1)
                elif self.alter in ["greater", "upper_tail"]:
                    p_value = 1 - t.cdf(Z0, df=n-1)
        if p_value < self.alpha:
            print("Bác bỏ H0 nếu p_value < alpha")
        else:
            print("Not enough evidence to reject H0")

        return {'p-value':p_value, 'T_stats': Z0}
    
    def unpaired_data_equal_var(self, x1, x2, muy1, muy2):
        """
            ==================================================================================================================
            unpaired data and equal_variance
            Reference: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm
            ==================================================================================================================
            Example
            >> obj = mean_test(alpha=0.05, alter='less', sigma=1)
            >> obj.unpaired_data_equal_var([1,2,4,5], [2,3,3], 3, 4)
            ...................
                Not enough evidence to reject H0
                {'p-value': 0.2237139366373361, 'T_stats': -0.8240395855065445}
            ==================================================================================================================
        """
        # sample-sizes
        n1 = len(x1)
        n2 = len(x2)

        # difference of mean in 2 samples
        muy_diff = muy1 - muy2

        # common variance
        sd1 = np.std(x1)
        sd2 = np.std(x2)
        cmn_var = ( (n1 - 1)*sd1**2 + (n2 - 1)*sd2**2 ) / (n1 + n2 - 2)

        # Stastistical-testing
        T_stats = muy_diff / (cmn_var * (1/n1 + 1/n2)**0.5 )

        # degree of freedoms
        dfs = n1+n2-2
        # p.value
        # bien luan
        if self.alter in ["equal", "two_side"]:
            p_value = 2*min(1 - t.cdf(T_stats), t.cdf(T_stats, df=dfs))
        elif self.alter in ["less", "lower_tail"]:
            p_value = t.cdf(T_stats, df=dfs)
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - t.cdf(T_stats, df=dfs)

        if p_value < self.alpha:
            print("Bác bỏ H0 nếu p_value < alpha")
        else:
            print("Not enough evidence to reject H0")

        return {'p-value':p_value, 'T_stats': T_stats}

    def unpaired_data_non_equal_var(self, x1, x2, muy1, muy2):
        """
            unpaired data and non-equal_variance
            Reference: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm        
            =========================================================================
            Example
            >> obj = mean_test(alpha=0.05, alter='two_side', sigma=1)
            >> obj.unpaired_data_non_equal_var([1,2,4,5], [2,3,3], 3, 4)    
            ...........................................
                Not enough evidence to reject H0
                {'p-value': nan, 'T_stats': 1.1960198895331717}
        """
        # sample-sizes
        n1 = len(x1)
        n2 = len(x2)

        # difference of mean in 2 samples
        muy_diff = muy1 - muy2

        # common variance
        sd1 = np.std(x1)
        sd2 = np.std(x2)
        cmn_var = (sd1**2 / n1 + sd2**2 / n2)

        # Stastistical-testing        
        T_stats = muy_diff / (cmn_var**0.5)

        # degree of freedoms
        tu_so = (sd1**2 / n1 + sd2**2 / n2)**2
        mau_so = (n1-1)*(sd1**2 / n1)**2 + (n2-1)*(sd2**2 / n2)**2
        dfs = int(tu_so / mau_so)

        # p.value
        # Bien luan
        if self.alter in ["equal", "two_side"]:
            p_value = 2*min(1 - t.cdf(T_stats, df=dfs), t.cdf(T_stats, df=dfs))
        elif self.alter in ["less", "lower_tail"]:
            p_value = t.cdf(T_stats, df=dfs)
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - t.cdf(T_stats, df=dfs)

        if p_value < self.alpha:
            print("Bác bỏ H0 nếu p_value < alpha")
        else:
            print("Not enough evidence to reject H0")

        return {'p-value':p_value, 'T_stats': T_stats}
    
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

#============================================
class Polynomial_Univariate_Regression:
    """
        This class is used to solve the polynomial assumption of univariate-regression

                Y = a0 + a1 X + a2 X^2 + ... + a_d X^d
        ================================================================================
        Example.
            ############################################################################
            >> X = [1, 2, -1]
            >> y = [1, -1, -1]
            >> clf = Polynomial_Univariate_Regression(X, deg = 3)
            >> clf.coef()
            -------------------
                w_0:  -1.0000000000000004
                w_1:  1.0000000000000007
                w_2:  1.000000000000001
            #*********************************************
            #
            # this meant y = w2 * x^2 + w1 * x + w0
            # or         y =    x^2   +    x  -  1
            #
            #*********************************************
            >> clf.predict(np.array([1,2,4]))
            ---------------------
                [ 1.  5. 19.]
            #*********************************************
            # Note that
            #              1 = w2*1^2 + w1*1 + w0
            #              5 = w2*2^2 + w1*2 + w0
            #             19 = w2*4^2 + w1*4 + w0
            #*********************************************
            >> clf.MSE_score([1,2,4], [2,3,3])
            ----------------------
                87.00000000000023
            ############################################################################
    """
    def __init__(self, X, y, deg):
        self.X = np.array(X)
        self.y = np.array(y)
        self.deg = deg
        
    def coef(self, if_printed=True):
        coefs = np.polyfit(self.X, self.y, self.deg)
        if if_printed:
            for d in range(self.deg + 1):
                print(f"w_{d}: \t {coefs[d]}")
        return coefs
    
    def predict(self, X_new):
        coefs = self.coef(if_printed=False)
        X_new = np.array(X_new)
        X_bar = np.array([X_new**k for k in range(self.deg + 1)])
        y_pred = np.sum(np.array(coefs.reshape(-1, 1)*X_bar), axis = 0)
        
        return y_pred

    def MSE_score(self, X_new, y_new):
        coefs = self.coef(if_printed=False)
        y_pred = self.predict(X_new)
        return np.mean([(y_new[k] - y_pred[k])**2 for k in range((np.array(X_new).shape[0]))])
    
    def R2_score(self, X_new, y_new):
        coefs = self.coef(if_printed=False)
        y_pred = self.predict(X_new)
        
        # sum of square_error
        SSE = np.sum([(self.y[k] - y_pred[k])**2 for k in range((np.array(self.X).shape[0]))])
        
        # total_sum of square = SSE + Sum_squared_regression
        SST = SSE + np.sum([(y_pred[k] - np.mean(y_new))**2 for k in range((np.array(X_new).shape[0]))])
        
        return 1 - (SSE / SST)
    
    def plot(self):
        coefs = self.coef(if_printed=False)
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