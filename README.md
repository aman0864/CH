<div class="cell markdown">

<h1 style="text-align:center; font-size:160%; font-family:verdana;color:#F44A79;"><em>Date 25-06-2021</em></h1>

</div>

<div class="cell markdown">

<h1 style="text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;"><em>More in Seaborn HeatMap</em></h1>

</div>

<div class="cell code" data-execution_count="1">

``` python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
```

</div>

<div class="cell code" data-execution_count="2">

``` python
rows_in_data_frame=20
max_value_in_data_frame=100 # use values of more than 11 (refrence arr06)
indeces=np.array(['arr01','arr02','arr03','arr04','arr05','arr06','arr07','arr08','arr09','arr10'])
arr01=np.linspace(12,max_value_in_data_frame-.9,rows_in_data_frame)
arr02=np.random.uniform(0,max_value_in_data_frame,rows_in_data_frame)
arr03=np.linspace(.99,max_value_in_data_frame-50.9,rows_in_data_frame)
arr04=np.random.uniform(0,max_value_in_data_frame,rows_in_data_frame)
arr05=np.random.uniform(0,max_value_in_data_frame,rows_in_data_frame)
arr06=np.linspace(.9,max_value_in_data_frame-10.99,rows_in_data_frame)
arr06=np.sort(arr06)[::-1]
arr07=np.linspace(.99,max_value_in_data_frame-.9,rows_in_data_frame)
arr08=np.random.uniform(0,max_value_in_data_frame,rows_in_data_frame)
arr09=np.random.uniform(0,max_value_in_data_frame,rows_in_data_frame)
arr10=np.linspace(.99,max_value_in_data_frame-.9,rows_in_data_frame)
arr10=np.sort(arr10)[::-1]
main_arr = np.vstack((arr01,arr02,arr03,arr04,arr05,arr06,arr07,arr08,arr09,arr10))
main_arr
data_2=pd.DataFrame(main_arr).set_index(indeces)
data_2
```

<div class="output execute_result" data-execution_count="2">

``` 
              0          1          2          3          4          5   \
arr01  12.000000  16.584211  21.168421  25.752632  30.336842  34.921053   
arr02   4.925852  92.920864  69.788858  77.159324  57.708498   6.874130   
arr03   0.990000   3.522105   6.054211   8.586316  11.118421  13.650526   
arr04  49.848766   2.473244   1.939821  42.538752   9.723571  50.657333   
arr05   6.504514  43.148669  40.677650  44.175267  18.757514  74.321703   
arr06  89.010000  84.372632  79.735263  75.097895  70.460526  65.823158   
arr07   0.990000   6.153684  11.317368  16.481053  21.644737  26.808421   
arr08  19.404873  90.172644  48.697018  15.884649  40.972229   7.177256   
arr09  48.709348  73.559620  94.143179  96.408338  60.853601   4.019778   
arr10  99.100000  93.936316  88.772632  83.608947  78.445263  73.281579   

              6          7          8          9          10         11  \
arr01  39.505263  44.089474  48.673684  53.257895  57.842105  62.426316   
arr02  32.324887  78.118216  83.844715  89.945999  85.885332  63.545299   
arr03  16.182632  18.714737  21.246842  23.778947  26.311053  28.843158   
arr04  72.576437  81.557554  15.383750  15.753845  38.389502  11.337540   
arr05  15.720703  17.165957  74.015835  38.251779  73.651961  38.674252   
arr06  61.185789  56.548421  51.911053  47.273684  42.636316  37.998947   
arr07  31.972105  37.135789  42.299474  47.463158  52.626842  57.790526   
arr08  91.893698  55.781581  33.549109  57.806304  92.786607  16.996416   
arr09  35.729812  94.510709  34.621760   0.741488  57.072727  53.670750   
arr10  68.117895  62.954211  57.790526  52.626842  47.463158  42.299474   

              12         13         14         15         16         17  \
arr01  67.010526  71.594737  76.178947  80.763158  85.347368  89.931579   
arr02  84.543641  68.869015   3.048119  10.657029  44.798461  19.373622   
arr03  31.375263  33.907368  36.439474  38.971579  41.503684  44.035789   
arr04  67.917948  90.025181  17.757379  86.698851  76.890506  69.192580   
arr05  64.034324  21.479349  47.546224  65.468640  17.926138  98.948736   
arr06  33.361579  28.724211  24.086842  19.449474  14.812105  10.174737   
arr07  62.954211  68.117895  73.281579  78.445263  83.608947  88.772632   
arr08  29.183260  89.267597  61.925946  24.421167  78.062650  95.353679   
arr09  46.703759  62.410151  41.006287  50.418571  56.723512  72.706096   
arr10  37.135789  31.972105  26.808421  21.644737  16.481053  11.317368   

              18         19  
arr01  94.515789  99.100000  
arr02  73.326042  16.303017  
arr03  46.567895  49.100000  
arr04  25.113717  61.555249  
arr05  20.948862  21.426458  
arr06   5.537368   0.900000  
arr07  93.936316  99.100000  
arr08  87.038414  19.230292  
arr09  41.900802  81.784338  
arr10   6.153684   0.990000  
```

</div>

</div>

<div class="cell code" data-execution_count="3">

``` python
plt.figure(figsize=(16,9))
 
annot_dict={'fontsize':12, 
           'fontstyle':'italic',  
           'color':"#ff0062",
           'alpha':.9, 
           'rotation':45,
           'verticalalignment':'center',
           'backgroundcolor':'#e3cfe3'}
 
sns.heatmap(data_2, annot = True, annot_kws= annot_dict)
```

<div class="output execute_result" data-execution_count="3">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](6ed2f06c5cb137ae0ffc719c28594a7d97c6d220.png)

</div>

</div>

<div class="cell code" data-execution_count="4">

``` python
plt.figure(figsize=(16,9))
 
annot_dict={'fontsize':12, 
           'fontstyle':'italic',  
           'color':"#ff0062",
           'alpha':.9, 
           'rotation':45,
           'verticalalignment':'center',
           'backgroundcolor':'#e3cfe3'}
 
sns.heatmap(data_2, annot = True, annot_kws= annot_dict,linewidths=5)
```

<div class="output execute_result" data-execution_count="4">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](434694124bec58e7ca4f936136d0ec9cea6d6ab1.png)

</div>

</div>

<div class="cell code" data-execution_count="5">

``` python
plt.figure(figsize=(16,9))
 
annot_dict={'fontsize':12, 
           'fontstyle':'italic',  
           'color':"#ff0062",
           'alpha':.9, 
           'rotation':45,
           'verticalalignment':'center',
           'backgroundcolor':'#e3cfe3'}
 
sns.heatmap(data_2, annot = True, annot_kws= annot_dict,linewidths=5,linecolor='g')
```

<div class="output execute_result" data-execution_count="5">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](bc04b041a3d7e49df1b09ad86539bdf197159bc6.png)

</div>

</div>

<div class="cell code" data-execution_count="6">

``` python
plt.figure(figsize=(16,9))
 
annot_dict={'fontsize':12, 
           'fontstyle':'italic',  
           'color':"#ff00f2",
           'alpha':1, 
           'rotation':45,
           'verticalalignment':'center'}
 
sns.heatmap(data_2, annot = True, annot_kws= annot_dict,linewidths=5,linecolor='#fa52f2',cmap='winter_r')
```

<div class="output execute_result" data-execution_count="6">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](d7513e81b195bc22b7bb13de02bdd63e1c5218d6.png)

</div>

</div>

<div class="cell code" data-execution_count="7">

``` python
plt.figure(figsize=(16,9))
 
annot_dict={'fontsize':12, 
           'fontstyle':'italic',  
           'color':"#ff00f2",
           'alpha':1, 
           'rotation':45,
           'verticalalignment':'center'}
 
sns.heatmap(data_2, 
            annot = True, 
            annot_kws= annot_dict,
            linewidths=5,
            linecolor='#fa52f2',
            cmap='winter_r',
            cbar=False)
```

<div class="output execute_result" data-execution_count="7">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](a777b349d078ec04d5a48871a9d568570b9cd78d.png)

</div>

</div>

<div class="cell code" data-execution_count="8">

``` python
plt.figure(figsize=(16,9))
 
annot_dict={'fontsize':12, 
           'fontstyle':'italic',  
           'color':"#ff00f2",
           'alpha':1, 
           'rotation':45,
           'verticalalignment':'center'}
 
sns.heatmap(data_2, 
            annot = True, 
            annot_kws= annot_dict,
            linewidths=5,
            linecolor='#fa52f2',
            cmap='winter_r',
            cbar=False,
            xticklabels=False,
            yticklabels=False)
```

<div class="output execute_result" data-execution_count="8">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](35f50bbbb156cb95c06f9a4cf87e2da4f1f5f1fd.png)

</div>

</div>

<div class="cell code" data-execution_count="9">

``` python
plt.figure(figsize=(16,9))

cbar_dict=dict(shrink=10,
               orientation='horizontal',
               drawedges=True,
               ticks=np.linspace(0,max_value_in_data_frame,30,dtype=int),
               extend='min', 
               extendfrac=.2,)
 
sns.heatmap(data_2, 
            annot = True, 
            annot_kws= annot_dict,
            linewidths=5,
            linecolor='#fa52f2',
            cmap='winter_r',
            xticklabels=False,
            yticklabels=False,
            cbar_kws=cbar_dict)
```

<div class="output execute_result" data-execution_count="9">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](85719394464e8734703114b9b69d4af5f1793b81.png)

</div>

</div>

<div class="cell code" data-execution_count="10">

``` python
plt.figure(figsize=(16,9))
sns.heatmap(data_2, 
            annot = True, 
            annot_kws= annot_dict,
            linewidths=5,
            linecolor='#fa52f2',
            cmap='winter_r',
            xticklabels=np.arange(0,10),
            yticklabels=False,
            cbar_kws=cbar_dict)
```

<div class="output execute_result" data-execution_count="10">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](66b8aa7123dd4c1d4407a1efcc616f42932cce03.png)

</div>

</div>

<div class="cell code" data-execution_count="11">

``` python
plt.figure(figsize=(16,9))
sns.heatmap(data_2, 
            annot = True, 
            annot_kws= annot_dict,
            linewidths=5,
            linecolor='#fa52f2',
            cmap='winter_r',
            xticklabels=np.arange(0,10),
            yticklabels=['arrsekjdsfjhsjdfhsdf',86254436954362523456],
            cbar_kws=cbar_dict)
```

<div class="output execute_result" data-execution_count="11">

    <AxesSubplot:>

</div>

<div class="output display_data">

![](31372b4098c54cb4e66fa60b91dc5eee0058d096.png)

</div>

</div>
