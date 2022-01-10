import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


## Veri ##

df_c = pd.read_excel(r"C:\Users\yildi\OneDrive\Masaüstü\datasets/ab_testing.xlsx",
                    sheet_name="Control Group")

df_t = pd.read_excel(r"C:\Users\yildi\OneDrive\Masaüstü\datasets/ab_testing.xlsx",
                    sheet_name="Test Group")

df_control = df_c.copy()
df_test = df_t.copy()

df_control.head()
df_test.head()

df_control.Purchase.mean()
df_control.Earning.mean()

df_test.Purchase.mean()
df_test.Earning.mean()

##satın alma ve kazançta artış meydana gelmiştir. AB testine geçelim.##

# İki grup ortalaması arasında karşılaştırma yapılmak istenildiğinde kullanılır.

# 1. Varsayım Kontrolü
#   - 1. Normallik Varsayımı
#   - 2. Varyans Homojenliği
# 2. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi (non-parametrik test)
# Not:
# - Normallik sağlanmıyorsa direk 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.

## Varsayımlar ##

##Normallik Varsayımı - Shapiro

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(df_control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
test_stat, pvalue = shapiro(df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

##p-value = 0.5891 p-value = 0.1541 0,05'ten küçük olmadığından reddedemiyoruz ve
## control ve test grubu normal dağılımdır.

##Varyans Homojenliği Varsayımı - Levene

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df_control["Purchase"], df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

##p-value = 0.1083 0,05'ten küçük olmadığından reddedemiyoruz ve
##varyanslar homojendir.

##Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)

# H0: M1 = M2 Control ve Test grup ortalamaları arasında fark yoktur.
# H1: M1 != M2 Control ve Test grup ortalamaları arasında fark vardır.

test_stat, pvalue = ttest_ind(df_control["Purchase"], df_test["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

##p-value = 0.3493 0,05'ten küçük olmadığından reddedemiyoruz.
## Control ve test grupları ortalamaları arasında fark yoktur.


## Parametrik T Test
####Normallik - Shapiro ve Varyans Homojenliği - Levene varsayımlarını test ettim.
##iki varsayım da sağlandı. Bu nedenle parametrik - ttest kullandım.


##Purchasede hipotezi kabul ettik. Earning kriterinde reddettik.

test_stat, pvalue = ttest_ind(df_control["Earning"], df_test["Earning"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
















