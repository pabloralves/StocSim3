"""
Read the results for inversion mutation.
Performs stat tests on the different cooling schedules
to check if they likely come from the same distribution
"""

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

# Step 1, Read data, which is a list of dict of dict
# results = eval(open(results.txt))
results = [{'cooling schedule': 'logarithmic_cool', 'data': [{'mutation function': 'swap', 'scores': [740.2510138171019, 677.512301987272], 'average': 708.881657902187, 'std': 31.369355914914934}, {'mutation function': 'insert', 'scores': [827.5476140642019, 694.4222078425839], 'average': 760.984910953393, 'std': 66.56270311080897}, {'mutation function': 'inversion', 'scores': [544.431714975575, 548.6797704435935], 'average': 546.5557427095843, 'std': 2.124027734009246}, {'mutation function': 'two_opt', 'scores': [932.0881538623785, 829.548969756104], 'average': 880.8185618092413, 'std': 51.26959205313722}]}, {'cooling schedule': 'linear_cool', 'data': [{'mutation function': 'swap', 'scores': [854.6037654692818, 904.0220096244796], 'average': 879.3128875468807, 'std': 24.709122077598863}, {'mutation function': 'insert', 'scores': [729.1915006805948, 834.4188715504249], 'average': 781.8051861155099, 'std': 52.613685434915055}, {'mutation function': 'inversion', 'scores': [662.5596851576493, 727.5463297125016], 'average': 695.0530074350754, 'std': 32.49332227742616}, {'mutation function': 'two_opt', 'scores': [716.5264228857052, 1153.5543782528794], 'average': 935.0404005692923, 'std': 218.5139776835871}]}, {'cooling schedule': 'arithmetic_geometric_cool', 'data': [{'mutation function': 'swap', 'scores': [871.3717834260049, 796.971275333229], 'average': 834.1715293796169, 'std': 37.200254046387954}, {'mutation function': 'insert', 'scores': [681.6176626539461, 676.7122731990064], 'average': 679.1649679264763, 'std': 2.4526947274698614}, {'mutation function': 'inversion', 'scores': [640.3760232473577, 625.6639209646276], 'average': 633.0199721059926, 'std': 7.3560511413650715}, {'mutation function': 'two_opt', 'scores': [753.3557096231718, 704.2606924641254], 'average': 728.8082010436486, 'std': 24.547508579523196}]}, {'cooling schedule': 'exponential_cool', 'data': [{'mutation function': 'swap', 'scores': [688.4331425994345, 707.6568991990413], 'average': 698.0450208992379, 'std': 9.61187829980338}, {'mutation function': 'insert', 'scores': [755.3031675444455, 739.4723653410643], 'average': 747.3877664427549, 'std': 7.915401101690577}, {'mutation function': 'inversion', 'scores': [661.2451602338629, 806.0476345682218], 'average': 733.6463974010423, 'std': 72.40123716717949}, {'mutation function': 'two_opt', 'scores': [723.6461581485935, 784.061543403033], 'average': 753.8538507758133, 'std': 30.207692627219785}]}, {'cooling schedule': 'quadratic_cool', 'data': [{'mutation function': 'swap', 'scores': [759.5849044127292, 894.9508162054648], 'average': 827.2678603090969, 'std': 67.68295589636779}, {'mutation function': 'insert', 'scores': [788.109588903458, 748.7452148267517], 'average': 768.4274018651049, 'std': 19.682187038353106}, {'mutation function': 'inversion', 'scores': [688.30298628717, 821.8658912693048], 'average': 755.0844387782374, 'std': 66.7814524910674}, {'mutation function': 'two_opt', 'scores': [911.3898569051877, 1096.2854585356226], 'average': 1003.8376577204051, 'std': 92.44780081521748}]}]

# Step 2. Extract data from list of dict of dict
logarithmic_cool = results[0]['data'][2]['scores'] #['scores']
linear_cool = results[1]['data'][2]['scores']
arithmetic_geometric_cool = results[2]['data'][2]['scores']
exponential_cool = results[3]['data'][2]['scores']
quadratic_cool = results[4]['data'][2]['scores']

# EXTRA: Plot to test data was correctly obtained :)
#plt.scatter(0,np.mean(logarithmic_cool))
#plt.scatter(1,np.mean(linear_cool))
#plt.scatter(2,np.mean(arithmetic_geometric_cool))
#plt.scatter(3,np.mean(exponential_cool))
#plt.scatter(4,np.mean(quadratic_cool))
# Plot all points!
#plt.scatter(np.ones(len(logarithmic_cool))*0,logarithmic_cool)
#plt.scatter(np.ones(len(linear_cool))*1,linear_cool)
#plt.scatter(np.ones(len(arithmetic_geometric_cool))*2,arithmetic_geometric_cool)
#plt.scatter(np.ones(len(exponential_cool))*3,exponential_cool)
#plt.scatter(np.ones(len(quadratic_cool))*4,quadratic_cool)
#plt.show()

# Step 3.Do tests to show if distributions are similar
confidence = 0.95
significance = 1-confidence

# 3.1 Kruskal-Wallis H-test
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html
# """ The Kruskal-Wallis H-test tests the null hypothesis
# that the population median of all of the groups are equal. 
# It is a non-parametric version of ANOVA. The test works on 2 or more 
# independent samples, which may have different sizes. 
# Note that rejecting the null hypothesis does not indicate 
# which of the groups differs. Post hoc comparisons between groups are 
# required to determine which groups are different."""
_, p_value = sp.stats.kruskal(logarithmic_cool, linear_cool,arithmetic_geometric_cool,exponential_cool,quadratic_cool)
SAME_DISTRIBUTION = p_value > significance

print('Kruskal-Wallis H-test')
print('Confidence:', confidence*100,'%')
print('p_value:',p_value)
print('Samples come from same distribution' if SAME_DISTRIBUTION else 'Samples do not come from the same distribution.')
print()

# 3.2 K-sample Anderson-Darling test 
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson_ksamp.html
# """ The k-sample Anderson-Darling test is a modification of the one-sample 
# Anderson-Darling test. It tests the null hypothesis that k-samples are drawn 
# from the same population without having to specify the distribution function 
# of that population. The critical values depend on the number of samples."""
samples = [logarithmic_cool, linear_cool,arithmetic_geometric_cool,exponential_cool,quadratic_cool]
_, _, p_value = sp.stats.anderson_ksamp(samples)
SAME_DISTRIBUTION = p_value > significance

print('K-sample Anderson-Darling test ')
print('Confidence:', confidence*100,'%')
print('p_value:',p_value)
print('Samples come from same distribution' if SAME_DISTRIBUTION else 'Samples do not come from the same distribution.')