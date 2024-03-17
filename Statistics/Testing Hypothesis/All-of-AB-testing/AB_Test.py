from scipy.stats import norm, t
import numpy as np

def find_sample_size(alpha=0.05, beta=0.2, Base_rt=0.3, MDE_Rt=0.45):
    """
        Xác định sample size khi có các nhân tố 
            MDE_rate : minimum detectable effort rate
            Base_rt: Baseline conversion rate
            alpha: significance value
            beta (1 - beta): statistical power
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