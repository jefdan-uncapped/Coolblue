"""
Visualize the collected data from www.coolblue.nl
"""

# import section
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# reading data
PRODUCTINFO = pd.read_csv('data/productinfo_prep.csv')

# set plot dimensions
X_PIXELS, Y_PIXELS, DPI = 1500, 1000, 150
X_INCH, Y_INCH = X_PIXELS / DPI, Y_PIXELS / DPI

# plot price distribution per brand
plt.figure(figsize=(X_INCH, Y_INCH), dpi=DPI)
sns.boxplot(x='price',
            y='brand',
            data=PRODUCTINFO.groupby('brand').filter(lambda x: len(x) > 5),
            palette='PRGn',
            width=0.75).set_title('Price Distribution per Brand')
sns.despine(offset=10, trim=True)
plt.savefig('plots/price_distribution_brand.png')

# plot price distribution per storage size
plt.figure(figsize=(X_INCH, Y_INCH), dpi=DPI)
sns.boxplot(x='price',
            y='storage',
            data=PRODUCTINFO[PRODUCTINFO.storage.notnull()],
            order=['16 MB', '64 MB', '8 GB', '16 GB', '32 GB', '64 GB', '128 GB', '256 GB'],
            palette='PRGn',
            width=0.75).set_title('Price Distribution per Storage Size')
sns.despine(offset=10, trim=True)
plt.savefig('plots/price_distribution_storage.png')

# plot price distribution per operation system
X_PIXELS, Y_PIXELS, DPI = 1500, 1000, 150
X_INCH, Y_INCH = X_PIXELS / DPI, Y_PIXELS / DPI
plt.figure(figsize=(X_INCH, Y_INCH), dpi=DPI)
sns.boxplot(x='price',
            y='os',
            data=PRODUCTINFO[PRODUCTINFO.os.notnull()].groupby('os').filter(lambda x: len(x) > 5),
            order=['Android 5.0',
                   'Android 5.1',
                   'Android 6.0',
                   'Android 7.0',
                   'Android 7.1',
                   'Android 8.0',
                   'iOS 9',
                   'iOS 9.3',
                   'iOS 10',
                   'iOS 11'],
            palette='PRGn',
            width=0.75).set_title('Price Distribution per Operating System')
sns.despine(offset=10, trim=True)
plt.savefig('plots/price_distribution_os.png')
