"""
Reads results_1000.txt, results_5000.txt and results_10000.txt
Performs stat tests to check if samples from all cooling schedules
are likely to come from the same distribution
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# 0. Set files to read and confidence
iterations = [1000,5000,10000]
CONFIDENCE = 0.95

SIGNIFICANCE = 1-CONFIDENCE
print('Confidence:', CONFIDENCE*100,'%')
print()

for i in iterations:
    #with open(f'results_{i}.txt') as f: # For small city
    # For medium size city
    with open(f'a280_results_{i}.txt') as f:

        # 1. Read data
        results = eval(f.read())
        print('Iterations:',i)

        # 2. Extract data
        logarithmic_cool = results[0]['data'][2]['scores']
        linear_cool = results[1]['data'][2]['scores']
        arithmetic_geometric_cool = results[2]['data'][2]['scores']
        exponential_cool = results[3]['data'][2]['scores']
        quadratic_cool = results[4]['data'][2]['scores']

        # 3. Perform stat testing
        
        # 3.1 Kruskal-Wallis H-test
        _, p_value = sp.stats.kruskal(logarithmic_cool, linear_cool,arithmetic_geometric_cool,exponential_cool,quadratic_cool)
        
        SAME_DISTRIBUTION = p_value > SIGNIFICANCE
        pass_string = 'PASS' if SAME_DISTRIBUTION else 'FAIL'
        print(pass_string,'Kruskal-Wallis H-test:','(pval='+str(round(p_value,4))+')')

        # 3.2 K-sample Anderson-Darling test
        samples = [logarithmic_cool, linear_cool,arithmetic_geometric_cool,exponential_cool,quadratic_cool]
        _, _, p_value = sp.stats.anderson_ksamp(samples)

        SAME_DISTRIBUTION = p_value > SIGNIFICANCE
        pass_string = 'PASS' if SAME_DISTRIBUTION else 'FAIL'
        print(pass_string,'K-sample Anderson-Darling test:','(pval='+str(round(p_value,4))+')')

        # 3.3 Kolmogorov-Smirnov test
        _, pvalue_1 = sp.stats.ks_2samp(logarithmic_cool, linear_cool)
        _, pvalue_2 = sp.stats.ks_2samp(linear_cool, arithmetic_geometric_cool)
        _, pvalue_3 = sp.stats.ks_2samp(arithmetic_geometric_cool, exponential_cool)
        _, pvalue_4 = sp.stats.ks_2samp(exponential_cool, quadratic_cool)
        
        SAME_DISTRIBUTION = pvalue_1 > SIGNIFICANCE and pvalue_2 > SIGNIFICANCE and pvalue_3 > SIGNIFICANCE and pvalue_4 > SIGNIFICANCE
        pass_string = 'PASS' if SAME_DISTRIBUTION else 'FAIL'
        print(pass_string,'Kolmogorov-Smirnov test:')
        print('p_values:',pvalue_1,pvalue_2,pvalue_3,pvalue_4)
        print()


# EXTRA: Plot points for insight
with open('a280_results_10000.txt') as f:
    results = eval(f.read())
    logarithmic_cool = results[0]['data'][2]['scores']
    linear_cool = results[1]['data'][2]['scores']
    arithmetic_geometric_cool = results[2]['data'][2]['scores']
    exponential_cool = results[3]['data'][2]['scores']
    quadratic_cool = results[4]['data'][2]['scores']
    
    plt.scatter(np.ones(len(logarithmic_cool))*0,logarithmic_cool)
    plt.scatter(np.ones(len(linear_cool))*1,linear_cool)
    plt.scatter(np.ones(len(arithmetic_geometric_cool))*2,arithmetic_geometric_cool)
    plt.scatter(np.ones(len(exponential_cool))*3,exponential_cool)
    plt.scatter(np.ones(len(quadratic_cool))*4,quadratic_cool)
    plt.show()