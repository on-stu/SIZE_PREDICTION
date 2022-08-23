```python
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings(action="ignore")
import seaborn as sns
import csv
import matplotlib
import matplotlib.pyplot as plt
```


```python
matplotlib.rcParams['font.family'] ='D2Coding'
matplotlib.rcParams['axes.unicode_minus'] =False
```


```python
data=pd.read_csv("data_extracted.csv")
```


```python
data.head()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>HUMAN_ID</th>
      <th>성별</th>
      <th>조사년도</th>
      <th>조사일</th>
      <th>나이</th>
      <th>측정지</th>
      <th>측정복젖가슴둘레</th>
      <th>측정복상의</th>
      <th>측정복배꼽수준허리둘레</th>
      <th>측정복하의</th>
      <th>...</th>
      <th>128. 배꼽수준앞중심길이</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20_M_1417</td>
      <td>남</td>
      <td>2020</td>
      <td>1114</td>
      <td>41</td>
      <td>서울/경기/강원</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.3</td>
      <td>90M</td>
      <td>...</td>
      <td>409</td>
      <td>482.0</td>
      <td>339.0</td>
      <td>536.0</td>
      <td>812</td>
      <td>771</td>
      <td>653</td>
      <td>577.0</td>
      <td>235.0</td>
      <td>342.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20_M_1455</td>
      <td>남</td>
      <td>2020</td>
      <td>1115</td>
      <td>41</td>
      <td>서울/경기/강원</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.5</td>
      <td>80M</td>
      <td>...</td>
      <td>369</td>
      <td>446.0</td>
      <td>325.0</td>
      <td>512.0</td>
      <td>733</td>
      <td>782</td>
      <td>641</td>
      <td>576.0</td>
      <td>249.0</td>
      <td>327.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20_M_1458</td>
      <td>남</td>
      <td>2020</td>
      <td>1115</td>
      <td>40</td>
      <td>서울/경기/강원</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84.0</td>
      <td>85M</td>
      <td>...</td>
      <td>401</td>
      <td>461.0</td>
      <td>340.0</td>
      <td>560.0</td>
      <td>707</td>
      <td>798</td>
      <td>664</td>
      <td>595.0</td>
      <td>267.0</td>
      <td>328.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20_F_1465</td>
      <td>여</td>
      <td>2020</td>
      <td>1116</td>
      <td>42</td>
      <td>서울/경기/강원</td>
      <td>86.0</td>
      <td>85XL</td>
      <td>88.0</td>
      <td>90F</td>
      <td>...</td>
      <td>449</td>
      <td>453.0</td>
      <td>356.5</td>
      <td>546.5</td>
      <td>882</td>
      <td>796</td>
      <td>659</td>
      <td>626.0</td>
      <td>294.0</td>
      <td>332.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20_F_1467</td>
      <td>여</td>
      <td>2020</td>
      <td>1116</td>
      <td>42</td>
      <td>서울/경기/강원</td>
      <td>73.6</td>
      <td>75M</td>
      <td>74.5</td>
      <td>75F</td>
      <td>...</td>
      <td>360</td>
      <td>391.0</td>
      <td>331.5</td>
      <td>477.5</td>
      <td>731</td>
      <td>738</td>
      <td>592</td>
      <td>544.0</td>
      <td>234.0</td>
      <td>310.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 147 columns</p>
</div>


```python
data.columns
```




    Index(['HUMAN_ID', '성별', '조사년도', '조사일', '나이', '측정지', '측정복젖가슴둘레', '측정복상의',
           '측정복배꼽수준허리둘레', '측정복하의',
           ...
           '128. 배꼽수준앞중심길이 ', '129. 배꼽수준등길이 ', '130. 목뒤젖꼭지길이 ',
           '131. 목뒤젖꼭지허리둘레선길이 ', '132. 배꼽수준샅앞뒤길이 ', '133. 앉은눈높이 ', '134. 앉은목뒤높이 ',
           '135. 앉은어깨높이 ', '136. 앉은팔꿈치높이(팔굽힌) ', '137. 위팔수직길이(팔굽힌) '],
          dtype='object', length=147)




```python
data.iloc[:,:11]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>HUMAN_ID</th>
      <th>성별</th>
      <th>조사년도</th>
      <th>조사일</th>
      <th>나이</th>
      <th>측정지</th>
      <th>측정복젖가슴둘레</th>
      <th>측정복상의</th>
      <th>측정복배꼽수준허리둘레</th>
      <th>측정복하의</th>
      <th>001. 머리위로뻗은주먹높이</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20_M_1417</td>
      <td>남</td>
      <td>2020</td>
      <td>1114</td>
      <td>41</td>
      <td>서울/경기/강원</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.3</td>
      <td>90M</td>
      <td>1976.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20_M_1455</td>
      <td>남</td>
      <td>2020</td>
      <td>1115</td>
      <td>41</td>
      <td>서울/경기/강원</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.5</td>
      <td>80M</td>
      <td>1949.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20_M_1458</td>
      <td>남</td>
      <td>2020</td>
      <td>1115</td>
      <td>40</td>
      <td>서울/경기/강원</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84.0</td>
      <td>85M</td>
      <td>1968.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20_F_1465</td>
      <td>여</td>
      <td>2020</td>
      <td>1116</td>
      <td>42</td>
      <td>서울/경기/강원</td>
      <td>86.0</td>
      <td>85XL</td>
      <td>88.0</td>
      <td>90F</td>
      <td>1963.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20_F_1467</td>
      <td>여</td>
      <td>2020</td>
      <td>1116</td>
      <td>42</td>
      <td>서울/경기/강원</td>
      <td>73.6</td>
      <td>75M</td>
      <td>74.5</td>
      <td>75F</td>
      <td>1815.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5087</th>
      <td>21_M_7293</td>
      <td>남</td>
      <td>2021</td>
      <td>924</td>
      <td>46</td>
      <td>경상권</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.0</td>
      <td>75</td>
      <td>2031.0</td>
    </tr>
    <tr>
      <th>5088</th>
      <td>21_M_7294</td>
      <td>남</td>
      <td>2021</td>
      <td>924</td>
      <td>45</td>
      <td>경상권</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>83.0</td>
      <td>75</td>
      <td>2036.0</td>
    </tr>
    <tr>
      <th>5089</th>
      <td>21_M_7295</td>
      <td>남</td>
      <td>2021</td>
      <td>924</td>
      <td>45</td>
      <td>경상권</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>88.0</td>
      <td>75</td>
      <td>2036.0</td>
    </tr>
    <tr>
      <th>5090</th>
      <td>21_M_7296</td>
      <td>남</td>
      <td>2021</td>
      <td>924</td>
      <td>45</td>
      <td>경상권</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>83.5</td>
      <td>75</td>
      <td>1915.0</td>
    </tr>
    <tr>
      <th>5091</th>
      <td>21_M_7297</td>
      <td>남</td>
      <td>2021</td>
      <td>924</td>
      <td>48</td>
      <td>경상권</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>82.5</td>
      <td>75</td>
      <td>2073.0</td>
    </tr>
  </tbody>
</table>
<p>5092 rows × 11 columns</p>
</div>



## 데이터 분석
 - 변수들 사이의 상관관계(EDA)는 다중공선성의 문제가 아니면 크게 상관 x (clustering 문제가 아니라면) -> 목적 무엇?
 - 성별에 따른 사이즈 차이는 분명하기에 따로 나눠서 분석해야함
 - 목표가 있는 상태이기에 그 목표와 함께 고려할 필요가 있다. 
 - 개인정보(HUMAN_ID, 조사년도, 조사일, 측정지)는 제거하고 보고자 함 (+ 나이는 상관이 있는가????)

### 불필요하다고 여겨지는 변수 제거 데이터 생성


```python
data_new=data.copy()
data_new=data_new.drop(["HUMAN_ID","조사년도","조사일","측정지"],axis=1)
```

### 성별에 따른 데이터 분리


```python
data_m=data_new[data_new["성별"]=="남"]
data_w=data_new[data_new["성별"]=="여"]
```


```python
print("남성 데이터 shape : ",data_m.shape)
print("여성 데이터 shape : ",data_w.shape)
```

    남성 데이터 shape :  (2319, 143)
    여성 데이터 shape :  (2773, 143)
    

### 결측치 값 확인

#### 남성


```python
# 남성
na_m=pd.DataFrame(data_m.isna().sum())     # col 별 na 값 count
na_m.reset_index(drop=False,inplace=True) 
na_m.columns=["col","na"]
na_m.sort_values(by="na")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col</th>
      <th>na</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>성별</td>
      <td>0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>086. 앉은무릎높이</td>
      <td>0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>087. 앉은오금높이</td>
      <td>0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>088. 어깨사이너비</td>
      <td>0</td>
    </tr>
    <tr>
      <th>94</th>
      <td>089. 위팔사이너비</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>51</th>
      <td>046. 배꼽수준허리둘레</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>040. 팔꿈치둘레(팔굽힌)</td>
      <td>0</td>
    </tr>
    <tr>
      <th>142</th>
      <td>137. 위팔수직길이(팔굽힌)</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>측정복상의</td>
      <td>2319</td>
    </tr>
    <tr>
      <th>2</th>
      <td>측정복젖가슴둘레</td>
      <td>2319</td>
    </tr>
  </tbody>
</table>
<p>143 rows × 2 columns</p>
</div>



#### 여성


```python
na_w=pd.DataFrame(data_w.isna().sum())     # col 별 na 값 count
na_w.reset_index(drop=False,inplace=True) 
na_w.columns=["col","na"]
na_w.sort_values(by="na")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col</th>
      <th>na</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>성별</td>
      <td>0</td>
    </tr>
    <tr>
      <th>91</th>
      <td>086. 앉은무릎높이</td>
      <td>0</td>
    </tr>
    <tr>
      <th>92</th>
      <td>087. 앉은오금높이</td>
      <td>0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>088. 어깨사이너비</td>
      <td>0</td>
    </tr>
    <tr>
      <th>94</th>
      <td>089. 위팔사이너비</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>49</th>
      <td>044. 허리기준선둘레(여)</td>
      <td>0</td>
    </tr>
    <tr>
      <th>50</th>
      <td>045. 허리둘레</td>
      <td>0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>039. 위팔둘레(팔굽힌)</td>
      <td>0</td>
    </tr>
    <tr>
      <th>142</th>
      <td>137. 위팔수직길이(팔굽힌)</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>측정복하의</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>143 rows × 2 columns</p>
</div>



### 결측치 확인 결론
- 남성은 "측정복상의" 와 "측정복젖가슴둘레" 가 전부 결측 값을 가진다. -> 변수 제거 후 데이터 분석 필요
- 여성은 "측정복 하의"에서 하나의 결측치가 발생함 -> row 제거하고 데이터 분석
- 나머지 변수에서는 결측치 존재 x

### 나이에 따른 차이 살펴보기

#### 남성
- 나이 분포
- 나이와 다른 변수들의 상관관계를 살펴보자


```python
# 나이분포
dd=data_m
dd_age=pd.DataFrame(dd["나이"].value_counts()) # 나이 count
dd_age.reset_index(drop=False,inplace=True)   # dataframe 형태 맞추기
dd_age.columns=["age","count"]                 # 변수명 설정
dd_age=dd_age.sort_values(by="age")
dd_age.plot.bar(x="age",y="count")
```




    <AxesSubplot:xlabel='age'>



    findfont: Font family ['D2Coding'] not found. Falling back to DejaVu Sans.
    


    
![png](output_20_2.png)
    


#### 나이와의 상관관계 



```python
dd["측정복하의"].value_counts()
```




    85M      377
    95M      262
    85       254
    95       214
    85       203
    90M      185
    95       176
    80M      127
    75M       92
    105M      79
    75        66
    100M      57
    75        52
    105       46
    105       45
    100F      19
    115M      17
    90F       15
    70M       12
    65         4
    80         3
    80F        2
    90         2
    100        2
    95M        1
    80         1
    209        1
    65M        1
    105M       1
    150M       1
    110F       1
    110M       1
    Name: 측정복하의, dtype: int64




```python
# 나이와 측정복배꼽수준허리둘레 의 관계 
dd['count']=1    # 나이에 따른 측정복배 count 하기 위한 변
a_mean=pd.DataFrame(dd.groupby(['나이'])['측정복배꼽수준허리둘레'].mean()) # 평균
a_mean['std']=dd.groupby(['나이'])['측정복배꼽수준허리둘레'].std() # 표준편차
a_mean=a_mean.reset_index(drop=False) # reset_index -> 형태 수정
a_mean.columns=["age","mean","std"]
```


```python
plt.figure(figsize=(10,7))
plt.title("age & waist")
plt.scatter(a_mean['age'],a_mean['mean'],c=a_mean['std'])
plt.xlabel("age",fontsize=20)
plt.ylabel("waist",fontsize=20)
plt.colorbar()
plt.show()
```

    findfont: Font family ['D2Coding'] not found. Falling back to DejaVu Sans.
    findfont: Font family ['D2Coding'] not found. Falling back to DejaVu Sans.
    


    
![png](output_24_1.png)
    



```python
### std 가 너무 큰 case 제거하자
a_mean2=a_mean[a_mean['std']<15]
plt.figure(figsize=(10,7))
plt.title("age & waist 2")
plt.scatter(a_mean2['age'],a_mean2['mean'],c=a_mean2['std'])
plt.xlabel("age",fontsize=20)
plt.ylabel("waist",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_25_0.png)
    


- 나이의 증가에 따라 허리둘레의 증가를 보이며, 다양해진다 -> 이를 고려한 모델링이 필요할 수도...

#### 여성


```python
# 나이분포
dd=data_w
dd_age=pd.DataFrame(dd["나이"].value_counts()) # 나이 count
dd_age.reset_index(drop=False,inplace=True)   # dataframe 형태 맞추기
dd_age.columns=["age","count"]                 # 변수명 설정
dd_age=dd_age.sort_values(by="age")
dd_age.plot.bar(x="age",y="count")
```




    <AxesSubplot:xlabel='age'>




    
![png](output_28_1.png)
    


- 20대의 자료가 압도적이었던 남성에 비해 3,40대의 비율이 높음

#### 나이 & 허리둘레


```python
# 나이와 측정복배꼽수준허리둘레 의 관계 
dd['count']=1    # 나이에 따른 측정복배 count 하기 위한 변
a_mean=pd.DataFrame(dd.groupby(['나이'])['측정복배꼽수준허리둘레'].mean()) # 평균
a_mean['std']=dd.groupby(['나이'])['측정복배꼽수준허리둘레'].std() # 표준편차
a_mean=a_mean.reset_index(drop=False) # reset_index -> 형태 수정
a_mean.columns=["age","mean","std"]
```


```python
plt.figure(figsize=(10,7))
plt.title("age & waist")
plt.scatter(a_mean['age'],a_mean['mean'],c=a_mean['std'])
plt.xlabel("age",fontsize=20)
plt.ylabel("waist",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_32_0.png)
    


#### 상당히 직선적인 관계를 보이나 이상치로 인한 것일 수 있으므로 제거하고 다시 탐색


```python
### outlier 제거  (std 활용)
a_mean2=a_mean[a_mean['std']<60]
plt.figure(figsize=(10,7))
plt.title("age & waist 2")
plt.scatter(a_mean2['age'],a_mean2['mean'],c=a_mean2['std'])
plt.xlabel("age",fontsize=20)
plt.ylabel("waist",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_34_0.png)
    


- 남성에 비해서 훨씬 직선적인 관계를 보이고 있으며 또한 변동의 폭 역시 좁다 
- 조금 더 안정화, 평균화 되어있다.


```python
dd.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>성별</th>
      <th>나이</th>
      <th>측정복젖가슴둘레</th>
      <th>측정복상의</th>
      <th>측정복배꼽수준허리둘레</th>
      <th>측정복하의</th>
      <th>001. 머리위로뻗은주먹높이</th>
      <th>002. 키</th>
      <th>003. 눈높이</th>
      <th>004. 목뒤높이</th>
      <th>...</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>여</td>
      <td>42</td>
      <td>86.0</td>
      <td>85XL</td>
      <td>88.0</td>
      <td>90F</td>
      <td>1963.0</td>
      <td>1685</td>
      <td>1562</td>
      <td>1425</td>
      <td>...</td>
      <td>453.0</td>
      <td>356.5</td>
      <td>546.5</td>
      <td>882</td>
      <td>796</td>
      <td>659</td>
      <td>626.0</td>
      <td>294.0</td>
      <td>332.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>여</td>
      <td>42</td>
      <td>73.6</td>
      <td>75M</td>
      <td>74.5</td>
      <td>75F</td>
      <td>1815.0</td>
      <td>1602</td>
      <td>1469</td>
      <td>1323</td>
      <td>...</td>
      <td>391.0</td>
      <td>331.5</td>
      <td>477.5</td>
      <td>731</td>
      <td>738</td>
      <td>592</td>
      <td>544.0</td>
      <td>234.0</td>
      <td>310.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>여</td>
      <td>40</td>
      <td>74.3</td>
      <td>75M</td>
      <td>77.0</td>
      <td>75F</td>
      <td>1901.0</td>
      <td>1642</td>
      <td>1523</td>
      <td>1386</td>
      <td>...</td>
      <td>405.0</td>
      <td>326.5</td>
      <td>488.5</td>
      <td>749</td>
      <td>738</td>
      <td>601</td>
      <td>552.0</td>
      <td>203.0</td>
      <td>349.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>여</td>
      <td>43</td>
      <td>77.5</td>
      <td>80L</td>
      <td>78.0</td>
      <td>80F</td>
      <td>1821.0</td>
      <td>1589</td>
      <td>1483</td>
      <td>1341</td>
      <td>...</td>
      <td>428.0</td>
      <td>331.5</td>
      <td>517.5</td>
      <td>741</td>
      <td>753</td>
      <td>611</td>
      <td>581.0</td>
      <td>268.0</td>
      <td>313.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>여</td>
      <td>40</td>
      <td>80.0</td>
      <td>80L</td>
      <td>80.0</td>
      <td>80F</td>
      <td>1766.0</td>
      <td>1531</td>
      <td>1430</td>
      <td>1292</td>
      <td>...</td>
      <td>415.0</td>
      <td>333.5</td>
      <td>527.5</td>
      <td>696</td>
      <td>716</td>
      <td>578</td>
      <td>544.0</td>
      <td>245.0</td>
      <td>299.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 144 columns</p>
</div>




```python
dd['측정복하의'].value_counts()
```




    80F     453
    75F     322
    80      300
    90F     258
    85F     253
    80      239
    90      209
    70      147
    70F     120
    70      103
    100F     97
    90       96
    100      59
    100      38
    60       27
    65F      22
    110F      9
    60        8
    75M       3
    70M       3
    60F       2
    1570      1
    80M       1
    95F       1
    105       1
    Name: 측정복하의, dtype: int64



#### 나이 & 가슴둘레


```python
# 나이와 측정복배꼽수준허리둘레 의 관계 
dd['count']=1    # 나이에 따른 측정복배 count 하기 위한 변
a_mean2=pd.DataFrame(dd.groupby(['나이'])['측정복젖가슴둘레'].mean()) # 평균
a_mean2['std']=dd.groupby(['나이'])['측정복젖가슴둘레'].std() # 표준편차
a_mean2=a_mean2.reset_index(drop=False) # reset_index -> 형태 수정
a_mean2.columns=["age","mean","std"]
```


```python
plt.figure(figsize=(10,7))
plt.title("age & chest")
plt.scatter(a_mean2['age'],a_mean2['mean'],c=a_mean2['std'])
plt.xlabel("age",fontsize=20)
plt.ylabel("chest",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_40_0.png)
    


- chest역시 전반적으로 나이와 아주강한 선형관계를 보이며 낮은 std를 나타낸다 

### 나이에 대한 분석은 나중에 마저 진행
- 변수들 사이의 상관관계에 나이가 상당히 영향을 미칠 수 있을 것으로 판단 
- 측정복 상의, 측정복 하의 등 도메인 지식및 해석이 필요한 경우
- 분석 목적에 따라 이를 고려한 모델링, 전처리를 진행해야함

### 사이즈 변수들에 대한 분석
#### 1. 상관관계 분석
- 상관성이 높은 변수가 많을 것으로 예상
ex.1) 살이 찜 -> 두께가 전반적으로 두꺼움
ex.2) 키가 큼 -> 전반적으로 길이(팔, 키, 높이)가 길것으로 예상



```python
data_m
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>성별</th>
      <th>나이</th>
      <th>측정복젖가슴둘레</th>
      <th>측정복상의</th>
      <th>측정복배꼽수준허리둘레</th>
      <th>측정복하의</th>
      <th>001. 머리위로뻗은주먹높이</th>
      <th>002. 키</th>
      <th>003. 눈높이</th>
      <th>004. 목뒤높이</th>
      <th>...</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.3</td>
      <td>90M</td>
      <td>1976.0</td>
      <td>1667</td>
      <td>1538</td>
      <td>1420</td>
      <td>...</td>
      <td>482.0</td>
      <td>339.0</td>
      <td>536.0</td>
      <td>812</td>
      <td>771</td>
      <td>653</td>
      <td>577.0</td>
      <td>235.0</td>
      <td>342.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.5</td>
      <td>80M</td>
      <td>1949.0</td>
      <td>1656</td>
      <td>1539</td>
      <td>1398</td>
      <td>...</td>
      <td>446.0</td>
      <td>325.0</td>
      <td>512.0</td>
      <td>733</td>
      <td>782</td>
      <td>641</td>
      <td>576.0</td>
      <td>249.0</td>
      <td>327.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>남</td>
      <td>40</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84.0</td>
      <td>85M</td>
      <td>1968.0</td>
      <td>1729</td>
      <td>1597</td>
      <td>1463</td>
      <td>...</td>
      <td>461.0</td>
      <td>340.0</td>
      <td>560.0</td>
      <td>707</td>
      <td>798</td>
      <td>664</td>
      <td>595.0</td>
      <td>267.0</td>
      <td>328.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>남</td>
      <td>43</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.6</td>
      <td>90M</td>
      <td>2005.0</td>
      <td>1715</td>
      <td>1587</td>
      <td>1456</td>
      <td>...</td>
      <td>490.0</td>
      <td>350.5</td>
      <td>569.5</td>
      <td>728</td>
      <td>796</td>
      <td>665</td>
      <td>590.0</td>
      <td>234.0</td>
      <td>356.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>75.6</td>
      <td>75M</td>
      <td>1954.0</td>
      <td>1646</td>
      <td>1529</td>
      <td>1398</td>
      <td>...</td>
      <td>448.0</td>
      <td>312.0</td>
      <td>491.0</td>
      <td>723</td>
      <td>766</td>
      <td>635</td>
      <td>563.0</td>
      <td>237.0</td>
      <td>326.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5087</th>
      <td>남</td>
      <td>46</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.0</td>
      <td>75</td>
      <td>2031.0</td>
      <td>1715</td>
      <td>1610</td>
      <td>1456</td>
      <td>...</td>
      <td>487.0</td>
      <td>326.0</td>
      <td>519.0</td>
      <td>694</td>
      <td>831</td>
      <td>677</td>
      <td>598.0</td>
      <td>281.0</td>
      <td>317.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5088</th>
      <td>남</td>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>83.0</td>
      <td>75</td>
      <td>2036.0</td>
      <td>1743</td>
      <td>1619</td>
      <td>1485</td>
      <td>...</td>
      <td>494.0</td>
      <td>350.0</td>
      <td>540.0</td>
      <td>787</td>
      <td>817</td>
      <td>683</td>
      <td>595.0</td>
      <td>280.0</td>
      <td>315.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5089</th>
      <td>남</td>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>88.0</td>
      <td>75</td>
      <td>2036.0</td>
      <td>1748</td>
      <td>1626</td>
      <td>1478</td>
      <td>...</td>
      <td>484.0</td>
      <td>351.0</td>
      <td>565.0</td>
      <td>793</td>
      <td>831</td>
      <td>683</td>
      <td>628.0</td>
      <td>311.0</td>
      <td>317.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5090</th>
      <td>남</td>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>83.5</td>
      <td>75</td>
      <td>1915.0</td>
      <td>1654</td>
      <td>1538</td>
      <td>1401</td>
      <td>...</td>
      <td>487.0</td>
      <td>341.0</td>
      <td>555.0</td>
      <td>734</td>
      <td>791</td>
      <td>654</td>
      <td>583.0</td>
      <td>283.0</td>
      <td>300.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5091</th>
      <td>남</td>
      <td>48</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>82.5</td>
      <td>75</td>
      <td>2073.0</td>
      <td>1741</td>
      <td>1632</td>
      <td>1489</td>
      <td>...</td>
      <td>492.0</td>
      <td>346.0</td>
      <td>548.0</td>
      <td>680</td>
      <td>806</td>
      <td>663</td>
      <td>583.0</td>
      <td>254.0</td>
      <td>329.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>2319 rows × 144 columns</p>
</div>




```python
dc=data_m.iloc[:,6:143]
dc.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>001. 머리위로뻗은주먹높이</th>
      <th>002. 키</th>
      <th>003. 눈높이</th>
      <th>004. 목뒤높이</th>
      <th>005. 어깨높이</th>
      <th>006. 어깨가쪽높이</th>
      <th>007. 겨드랑높이</th>
      <th>008. 허리기준선높이(여)</th>
      <th>009. 허리높이</th>
      <th>010. 배꼽수준허리높이</th>
      <th>...</th>
      <th>128. 배꼽수준앞중심길이</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1976.0</td>
      <td>1667</td>
      <td>1538</td>
      <td>1420</td>
      <td>1344.0</td>
      <td>1343</td>
      <td>1236</td>
      <td>9999</td>
      <td>988</td>
      <td>953</td>
      <td>...</td>
      <td>409</td>
      <td>482.0</td>
      <td>339.0</td>
      <td>536.0</td>
      <td>812</td>
      <td>771</td>
      <td>653</td>
      <td>577.0</td>
      <td>235.0</td>
      <td>342.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949.0</td>
      <td>1656</td>
      <td>1539</td>
      <td>1398</td>
      <td>1333.0</td>
      <td>1334</td>
      <td>1234</td>
      <td>9999</td>
      <td>1000</td>
      <td>977</td>
      <td>...</td>
      <td>369</td>
      <td>446.0</td>
      <td>325.0</td>
      <td>512.0</td>
      <td>733</td>
      <td>782</td>
      <td>641</td>
      <td>576.0</td>
      <td>249.0</td>
      <td>327.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1968.0</td>
      <td>1729</td>
      <td>1597</td>
      <td>1463</td>
      <td>1394.0</td>
      <td>1392</td>
      <td>1288</td>
      <td>9999</td>
      <td>1031</td>
      <td>1013</td>
      <td>...</td>
      <td>401</td>
      <td>461.0</td>
      <td>340.0</td>
      <td>560.0</td>
      <td>707</td>
      <td>798</td>
      <td>664</td>
      <td>595.0</td>
      <td>267.0</td>
      <td>328.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2005.0</td>
      <td>1715</td>
      <td>1587</td>
      <td>1456</td>
      <td>1381.0</td>
      <td>1381</td>
      <td>1273</td>
      <td>9999</td>
      <td>1017</td>
      <td>990</td>
      <td>...</td>
      <td>422</td>
      <td>490.0</td>
      <td>350.5</td>
      <td>569.5</td>
      <td>728</td>
      <td>796</td>
      <td>665</td>
      <td>590.0</td>
      <td>234.0</td>
      <td>356.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1954.0</td>
      <td>1646</td>
      <td>1529</td>
      <td>1398</td>
      <td>1326.0</td>
      <td>1327</td>
      <td>1217</td>
      <td>9999</td>
      <td>1005</td>
      <td>963</td>
      <td>...</td>
      <td>391</td>
      <td>448.0</td>
      <td>312.0</td>
      <td>491.0</td>
      <td>723</td>
      <td>766</td>
      <td>635</td>
      <td>563.0</td>
      <td>237.0</td>
      <td>326.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 137 columns</p>
</div>




```python
a=dc.corr()
```


```python
sns.heatmap(data=dc.corr(),annot=True,cmap='RdBu')
fig=plt.gcf()
fig.set_size_inches(15,13)
plt.title('corr',fontsize=20)
plt.show()
```


    
![png](output_47_0.png)
    


### 너무 많다......
#### 그리고 상관계수가 너무 높다


```python
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>001. 머리위로뻗은주먹높이</th>
      <th>002. 키</th>
      <th>003. 눈높이</th>
      <th>004. 목뒤높이</th>
      <th>005. 어깨높이</th>
      <th>006. 어깨가쪽높이</th>
      <th>007. 겨드랑높이</th>
      <th>008. 허리기준선높이(여)</th>
      <th>009. 허리높이</th>
      <th>010. 배꼽수준허리높이</th>
      <th>...</th>
      <th>128. 배꼽수준앞중심길이</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>001. 머리위로뻗은주먹높이</th>
      <td>1.000000</td>
      <td>0.922973</td>
      <td>0.919734</td>
      <td>0.940036</td>
      <td>0.917297</td>
      <td>0.921331</td>
      <td>0.902050</td>
      <td>NaN</td>
      <td>0.891727</td>
      <td>0.875179</td>
      <td>...</td>
      <td>0.380472</td>
      <td>0.479771</td>
      <td>0.377001</td>
      <td>0.421255</td>
      <td>0.296894</td>
      <td>0.645901</td>
      <td>0.653829</td>
      <td>0.578782</td>
      <td>0.076036</td>
      <td>0.699814</td>
    </tr>
    <tr>
      <th>002. 키</th>
      <td>0.922973</td>
      <td>1.000000</td>
      <td>0.983986</td>
      <td>0.970390</td>
      <td>0.957580</td>
      <td>0.954373</td>
      <td>0.950098</td>
      <td>NaN</td>
      <td>0.920158</td>
      <td>0.905226</td>
      <td>...</td>
      <td>0.416110</td>
      <td>0.474563</td>
      <td>0.420095</td>
      <td>0.512026</td>
      <td>0.312332</td>
      <td>0.741736</td>
      <td>0.684939</td>
      <td>0.628560</td>
      <td>0.128729</td>
      <td>0.698595</td>
    </tr>
    <tr>
      <th>003. 눈높이</th>
      <td>0.919734</td>
      <td>0.983986</td>
      <td>1.000000</td>
      <td>0.962659</td>
      <td>0.954922</td>
      <td>0.951633</td>
      <td>0.950424</td>
      <td>NaN</td>
      <td>0.919985</td>
      <td>0.899734</td>
      <td>...</td>
      <td>0.423945</td>
      <td>0.466787</td>
      <td>0.410289</td>
      <td>0.505660</td>
      <td>0.314473</td>
      <td>0.790928</td>
      <td>0.690095</td>
      <td>0.644005</td>
      <td>0.143967</td>
      <td>0.699694</td>
    </tr>
    <tr>
      <th>004. 목뒤높이</th>
      <td>0.940036</td>
      <td>0.970390</td>
      <td>0.962659</td>
      <td>1.000000</td>
      <td>0.964723</td>
      <td>0.967004</td>
      <td>0.943938</td>
      <td>NaN</td>
      <td>0.919720</td>
      <td>0.891456</td>
      <td>...</td>
      <td>0.433095</td>
      <td>0.565206</td>
      <td>0.435002</td>
      <td>0.485755</td>
      <td>0.353065</td>
      <td>0.708852</td>
      <td>0.753137</td>
      <td>0.651411</td>
      <td>0.155491</td>
      <td>0.694610</td>
    </tr>
    <tr>
      <th>005. 어깨높이</th>
      <td>0.917297</td>
      <td>0.957580</td>
      <td>0.954922</td>
      <td>0.964723</td>
      <td>1.000000</td>
      <td>0.996105</td>
      <td>0.968044</td>
      <td>NaN</td>
      <td>0.916934</td>
      <td>0.880972</td>
      <td>...</td>
      <td>0.450409</td>
      <td>0.500287</td>
      <td>0.449073</td>
      <td>0.532839</td>
      <td>0.378557</td>
      <td>0.704669</td>
      <td>0.694047</td>
      <td>0.732956</td>
      <td>0.225422</td>
      <td>0.714420</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>133. 앉은눈높이</th>
      <td>0.645901</td>
      <td>0.741736</td>
      <td>0.790928</td>
      <td>0.708852</td>
      <td>0.704669</td>
      <td>0.701882</td>
      <td>0.693093</td>
      <td>NaN</td>
      <td>0.584980</td>
      <td>0.557783</td>
      <td>...</td>
      <td>0.492383</td>
      <td>0.510495</td>
      <td>0.389847</td>
      <td>0.558228</td>
      <td>0.325923</td>
      <td>1.000000</td>
      <td>0.856501</td>
      <td>0.825767</td>
      <td>0.529750</td>
      <td>0.437957</td>
    </tr>
    <tr>
      <th>134. 앉은목뒤높이</th>
      <td>0.653829</td>
      <td>0.684939</td>
      <td>0.690095</td>
      <td>0.753137</td>
      <td>0.694047</td>
      <td>0.702515</td>
      <td>0.648977</td>
      <td>NaN</td>
      <td>0.544765</td>
      <td>0.500745</td>
      <td>...</td>
      <td>0.517350</td>
      <td>0.711916</td>
      <td>0.436189</td>
      <td>0.522856</td>
      <td>0.403945</td>
      <td>0.856501</td>
      <td>1.000000</td>
      <td>0.859334</td>
      <td>0.595608</td>
      <td>0.396788</td>
    </tr>
    <tr>
      <th>135. 앉은어깨높이</th>
      <td>0.578782</td>
      <td>0.628560</td>
      <td>0.644005</td>
      <td>0.651411</td>
      <td>0.732956</td>
      <td>0.729141</td>
      <td>0.666441</td>
      <td>NaN</td>
      <td>0.509769</td>
      <td>0.451416</td>
      <td>...</td>
      <td>0.537864</td>
      <td>0.565642</td>
      <td>0.450178</td>
      <td>0.600539</td>
      <td>0.443156</td>
      <td>0.825767</td>
      <td>0.859334</td>
      <td>1.000000</td>
      <td>0.729222</td>
      <td>0.413686</td>
    </tr>
    <tr>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <td>0.076036</td>
      <td>0.128729</td>
      <td>0.143967</td>
      <td>0.155491</td>
      <td>0.225422</td>
      <td>0.229593</td>
      <td>0.175617</td>
      <td>NaN</td>
      <td>-0.003550</td>
      <td>-0.047526</td>
      <td>...</td>
      <td>0.364475</td>
      <td>0.372826</td>
      <td>0.241644</td>
      <td>0.389197</td>
      <td>0.295376</td>
      <td>0.529750</td>
      <td>0.595608</td>
      <td>0.729222</td>
      <td>1.000000</td>
      <td>-0.321311</td>
    </tr>
    <tr>
      <th>137. 위팔수직길이(팔굽힌)</th>
      <td>0.699814</td>
      <td>0.698595</td>
      <td>0.699694</td>
      <td>0.694610</td>
      <td>0.714420</td>
      <td>0.703591</td>
      <td>0.688634</td>
      <td>NaN</td>
      <td>0.710194</td>
      <td>0.687948</td>
      <td>...</td>
      <td>0.259424</td>
      <td>0.286755</td>
      <td>0.301499</td>
      <td>0.313267</td>
      <td>0.220291</td>
      <td>0.437957</td>
      <td>0.396788</td>
      <td>0.413686</td>
      <td>-0.321311</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
<p>137 rows × 137 columns</p>
</div>



## 목적의 정의 확실히 
### 목적에 맞는 변수 활용이 필요 -> (ex. 상의 사이즈 측정시에 하체 사이즈는 필요 x)



```python
data_m.iloc[:,125:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>120. 검지손가락끝마디너비</th>
      <th>121. 막대쥔손안둘레</th>
      <th>122. 발직선길이</th>
      <th>123. 발너비</th>
      <th>124. 발꿈치너비</th>
      <th>125. 몸무게</th>
      <th>126. 몸통수직길이</th>
      <th>127. 엉덩이수직길이</th>
      <th>128. 배꼽수준앞중심길이</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17</td>
      <td>77</td>
      <td>260</td>
      <td>96</td>
      <td>69</td>
      <td>70.8</td>
      <td>672</td>
      <td>240</td>
      <td>409</td>
      <td>482.0</td>
      <td>339.0</td>
      <td>536.0</td>
      <td>812</td>
      <td>771</td>
      <td>653</td>
      <td>577.0</td>
      <td>235.0</td>
      <td>342.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>17</td>
      <td>90</td>
      <td>263</td>
      <td>104</td>
      <td>63</td>
      <td>58.8</td>
      <td>658</td>
      <td>260</td>
      <td>369</td>
      <td>446.0</td>
      <td>325.0</td>
      <td>512.0</td>
      <td>733</td>
      <td>782</td>
      <td>641</td>
      <td>576.0</td>
      <td>249.0</td>
      <td>327.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18</td>
      <td>96</td>
      <td>240</td>
      <td>99</td>
      <td>64</td>
      <td>65.6</td>
      <td>680</td>
      <td>248</td>
      <td>401</td>
      <td>461.0</td>
      <td>340.0</td>
      <td>560.0</td>
      <td>707</td>
      <td>798</td>
      <td>664</td>
      <td>595.0</td>
      <td>267.0</td>
      <td>328.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>113</td>
      <td>258</td>
      <td>99</td>
      <td>69</td>
      <td>73.3</td>
      <td>697</td>
      <td>258</td>
      <td>422</td>
      <td>490.0</td>
      <td>350.5</td>
      <td>569.5</td>
      <td>728</td>
      <td>796</td>
      <td>665</td>
      <td>590.0</td>
      <td>234.0</td>
      <td>356.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>14</td>
      <td>98</td>
      <td>235</td>
      <td>90</td>
      <td>55</td>
      <td>52.1</td>
      <td>640</td>
      <td>247</td>
      <td>391</td>
      <td>448.0</td>
      <td>312.0</td>
      <td>491.0</td>
      <td>723</td>
      <td>766</td>
      <td>635</td>
      <td>563.0</td>
      <td>237.0</td>
      <td>326.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5087</th>
      <td>16</td>
      <td>108</td>
      <td>247</td>
      <td>89</td>
      <td>57</td>
      <td>55.5</td>
      <td>695</td>
      <td>255</td>
      <td>389</td>
      <td>487.0</td>
      <td>326.0</td>
      <td>519.0</td>
      <td>694</td>
      <td>831</td>
      <td>677</td>
      <td>598.0</td>
      <td>281.0</td>
      <td>317.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5088</th>
      <td>16</td>
      <td>109</td>
      <td>261</td>
      <td>98</td>
      <td>61</td>
      <td>66.3</td>
      <td>710</td>
      <td>288</td>
      <td>414</td>
      <td>494.0</td>
      <td>350.0</td>
      <td>540.0</td>
      <td>787</td>
      <td>817</td>
      <td>683</td>
      <td>595.0</td>
      <td>280.0</td>
      <td>315.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5089</th>
      <td>19</td>
      <td>108</td>
      <td>255</td>
      <td>99</td>
      <td>67</td>
      <td>73.0</td>
      <td>706</td>
      <td>273</td>
      <td>438</td>
      <td>484.0</td>
      <td>351.0</td>
      <td>565.0</td>
      <td>793</td>
      <td>831</td>
      <td>683</td>
      <td>628.0</td>
      <td>311.0</td>
      <td>317.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5090</th>
      <td>17</td>
      <td>104</td>
      <td>244</td>
      <td>96</td>
      <td>59</td>
      <td>68.5</td>
      <td>701</td>
      <td>264</td>
      <td>412</td>
      <td>487.0</td>
      <td>341.0</td>
      <td>555.0</td>
      <td>734</td>
      <td>791</td>
      <td>654</td>
      <td>583.0</td>
      <td>283.0</td>
      <td>300.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5091</th>
      <td>16</td>
      <td>123</td>
      <td>256</td>
      <td>94</td>
      <td>62</td>
      <td>66.9</td>
      <td>708</td>
      <td>258</td>
      <td>400</td>
      <td>492.0</td>
      <td>346.0</td>
      <td>548.0</td>
      <td>680</td>
      <td>806</td>
      <td>663</td>
      <td>583.0</td>
      <td>254.0</td>
      <td>329.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>2319 rows × 19 columns</p>
</div>



## X 데이터로 사용될 변수 출력해보자


```python
data_m.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>성별</th>
      <th>나이</th>
      <th>측정복젖가슴둘레</th>
      <th>측정복상의</th>
      <th>측정복배꼽수준허리둘레</th>
      <th>측정복하의</th>
      <th>001. 머리위로뻗은주먹높이</th>
      <th>002. 키</th>
      <th>003. 눈높이</th>
      <th>004. 목뒤높이</th>
      <th>...</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.3</td>
      <td>90M</td>
      <td>1976.0</td>
      <td>1667</td>
      <td>1538</td>
      <td>1420</td>
      <td>...</td>
      <td>482.0</td>
      <td>339.0</td>
      <td>536.0</td>
      <td>812</td>
      <td>771</td>
      <td>653</td>
      <td>577.0</td>
      <td>235.0</td>
      <td>342.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.5</td>
      <td>80M</td>
      <td>1949.0</td>
      <td>1656</td>
      <td>1539</td>
      <td>1398</td>
      <td>...</td>
      <td>446.0</td>
      <td>325.0</td>
      <td>512.0</td>
      <td>733</td>
      <td>782</td>
      <td>641</td>
      <td>576.0</td>
      <td>249.0</td>
      <td>327.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>남</td>
      <td>40</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84.0</td>
      <td>85M</td>
      <td>1968.0</td>
      <td>1729</td>
      <td>1597</td>
      <td>1463</td>
      <td>...</td>
      <td>461.0</td>
      <td>340.0</td>
      <td>560.0</td>
      <td>707</td>
      <td>798</td>
      <td>664</td>
      <td>595.0</td>
      <td>267.0</td>
      <td>328.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>남</td>
      <td>43</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.6</td>
      <td>90M</td>
      <td>2005.0</td>
      <td>1715</td>
      <td>1587</td>
      <td>1456</td>
      <td>...</td>
      <td>490.0</td>
      <td>350.5</td>
      <td>569.5</td>
      <td>728</td>
      <td>796</td>
      <td>665</td>
      <td>590.0</td>
      <td>234.0</td>
      <td>356.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>75.6</td>
      <td>75M</td>
      <td>1954.0</td>
      <td>1646</td>
      <td>1529</td>
      <td>1398</td>
      <td>...</td>
      <td>448.0</td>
      <td>312.0</td>
      <td>491.0</td>
      <td>723</td>
      <td>766</td>
      <td>635</td>
      <td>563.0</td>
      <td>237.0</td>
      <td>326.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 144 columns</p>
</div>




```python
X_m=data_m.iloc[:,[0,1,7,130]]
X_m.columns=["sex","age","height","weight"]
X_m.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sex</th>
      <th>age</th>
      <th>height</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>남</td>
      <td>41</td>
      <td>1667</td>
      <td>70.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>남</td>
      <td>41</td>
      <td>1656</td>
      <td>58.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>남</td>
      <td>40</td>
      <td>1729</td>
      <td>65.6</td>
    </tr>
    <tr>
      <th>15</th>
      <td>남</td>
      <td>43</td>
      <td>1715</td>
      <td>73.3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>남</td>
      <td>41</td>
      <td>1646</td>
      <td>52.1</td>
    </tr>
  </tbody>
</table>
</div>



### 그래프를 기반으로 그나마 키와 몸무게와 관계성이 높아 보인 어깨 높이를 예측해보자


```python
y_m=pd.DataFrame(data_m.iloc[:,10])
y_m.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>005. 어깨높이</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1344.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1333.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1394.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1381.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1326.0</td>
    </tr>
  </tbody>
</table>
</div>



### plot


```python
plt.figure(figsize=(10,7))
plt.title("shoulder height")
plt.scatter(X_m.iloc[:,2],y_m)
plt.xlabel("height",fontsize=20)
plt.ylabel("shoulder height",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_58_0.png)
    



```python
plt.figure(figsize=(10,7))
plt.title("shoulder height")
plt.scatter(X_m.iloc[:,3],y_m)
plt.xlabel("weight",fontsize=20)
plt.ylabel("shoulder height",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_59_0.png)
    


#### 무게와 키를 함께 고려


```python
plt.figure(figsize=(10,7))
plt.title("shoulder height")
plt.scatter(X_m.iloc[:,2],y_m,c=X_m.iloc[:,3])
plt.xlabel("height",fontsize=20)
plt.ylabel("shoulder height",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_61_0.png)
    



```python
plt.figure(figsize=(10,7))
plt.title("shoulder height")
plt.scatter(X_m.iloc[:,3],y_m,c=X_m.iloc[:,2])
plt.xlabel("weight",fontsize=20)
plt.ylabel("shoulder height",fontsize=20)
plt.colorbar()
plt.show()
```


    
![png](output_62_0.png)
    


### 몸무게와 키 둘다 어깨높이와 상관이 있어보이지만 몸무게와 어깨 높이는 단순히 키에 대한 상관성으로 그래프가 나타날 뿐인것으로 해석된다. 
### 키와의 그래프에서 몸무게를 색으로 넣은 그래프를 보면 알 수 있다.

### 나이별로 그래프 형태를 살펴보자


```python
X_m['shoulder']=y_m
```


```python
x_2=X_m[X_m['age']<30]
x_3=X_m[(X_m['age']>=30)&(X_m['age']<40)]
x_4=X_m[(X_m['age']>=40)&(X_m['age']<50)]
x_5=X_m[(X_m['age']>=50)&(X_m['age']<60)]
x_6=X_m[X_m['age']>=60]
```


```python
x_3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sex</th>
      <th>age</th>
      <th>height</th>
      <th>weight</th>
      <th>shoulder</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>77</th>
      <td>남</td>
      <td>31</td>
      <td>1752</td>
      <td>72.4</td>
      <td>1411.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>남</td>
      <td>30</td>
      <td>1771</td>
      <td>72.2</td>
      <td>1450.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>남</td>
      <td>30</td>
      <td>1720</td>
      <td>64.1</td>
      <td>1376.0</td>
    </tr>
    <tr>
      <th>84</th>
      <td>남</td>
      <td>30</td>
      <td>1781</td>
      <td>80.3</td>
      <td>1422.0</td>
    </tr>
    <tr>
      <th>86</th>
      <td>남</td>
      <td>30</td>
      <td>1664</td>
      <td>70.8</td>
      <td>1353.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4991</th>
      <td>남</td>
      <td>36</td>
      <td>1738</td>
      <td>81.2</td>
      <td>1418.0</td>
    </tr>
    <tr>
      <th>5009</th>
      <td>남</td>
      <td>35</td>
      <td>1811</td>
      <td>72.7</td>
      <td>1479.0</td>
    </tr>
    <tr>
      <th>5014</th>
      <td>남</td>
      <td>34</td>
      <td>1726</td>
      <td>75.2</td>
      <td>1414.0</td>
    </tr>
    <tr>
      <th>5057</th>
      <td>남</td>
      <td>38</td>
      <td>1834</td>
      <td>81.2</td>
      <td>1493.0</td>
    </tr>
    <tr>
      <th>5058</th>
      <td>남</td>
      <td>36</td>
      <td>1816</td>
      <td>75.1</td>
      <td>1491.0</td>
    </tr>
  </tbody>
</table>
<p>493 rows × 5 columns</p>
</div>




```python
f, axes = plt.subplots(2, 2)
f.set_size_inches((12, 12))
plt.subplots_adjust(wspace = 0.15, hspace = 0.15)

# figure 전체 제목
f.suptitle('Shoulder height by age', fontsize = 15)

######################################################
axes[0, 0].scatter(x_2.iloc[:,2],x_2.iloc[:,4],c=x_2.iloc[:,3])
axes[0, 0].set_title('20', fontsize = 12)

axes[0, 1].scatter(x_3.iloc[:,2],x_3.iloc[:,4],c=x_3.iloc[:,3])
axes[0, 1].set_title('30', fontsize = 12)

axes[1, 0].scatter(x_4.iloc[:,2],x_4.iloc[:,4],c=x_4.iloc[:,3])
axes[1, 0].set_title('40', fontsize = 12)

axes[1, 1].scatter(x_5.iloc[:,2],x_5.iloc[:,4],c=x_5.iloc[:,3])
axes[1, 1].set_title('50', fontsize = 12)


plt.show()
```

    findfont: Font family ['D2Coding'] not found. Falling back to DejaVu Sans.
    


    
![png](output_68_1.png)
    


### 어깨너비


```python
data_m.columns
```




    Index(['성별', '나이', '측정복젖가슴둘레', '측정복상의', '측정복배꼽수준허리둘레', '측정복하의',
           '001. 머리위로뻗은주먹높이 ', '002. 키 ', '003. 눈높이 ', '004. 목뒤높이 ',
           ...
           '129. 배꼽수준등길이 ', '130. 목뒤젖꼭지길이 ', '131. 목뒤젖꼭지허리둘레선길이 ',
           '132. 배꼽수준샅앞뒤길이 ', '133. 앉은눈높이 ', '134. 앉은목뒤높이 ', '135. 앉은어깨높이 ',
           '136. 앉은팔꿈치높이(팔굽힌) ', '137. 위팔수직길이(팔굽힌) ', 'count'],
          dtype='object', length=144)




```python
X_m['shoulder_d']=data_m.iloc[:,65]
```


```python
data_m
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>성별</th>
      <th>나이</th>
      <th>측정복젖가슴둘레</th>
      <th>측정복상의</th>
      <th>측정복배꼽수준허리둘레</th>
      <th>측정복하의</th>
      <th>001. 머리위로뻗은주먹높이</th>
      <th>002. 키</th>
      <th>003. 눈높이</th>
      <th>004. 목뒤높이</th>
      <th>...</th>
      <th>129. 배꼽수준등길이</th>
      <th>130. 목뒤젖꼭지길이</th>
      <th>131. 목뒤젖꼭지허리둘레선길이</th>
      <th>132. 배꼽수준샅앞뒤길이</th>
      <th>133. 앉은눈높이</th>
      <th>134. 앉은목뒤높이</th>
      <th>135. 앉은어깨높이</th>
      <th>136. 앉은팔꿈치높이(팔굽힌)</th>
      <th>137. 위팔수직길이(팔굽힌)</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.3</td>
      <td>90M</td>
      <td>1976.0</td>
      <td>1667</td>
      <td>1538</td>
      <td>1420</td>
      <td>...</td>
      <td>482.0</td>
      <td>339.0</td>
      <td>536.0</td>
      <td>812</td>
      <td>771</td>
      <td>653</td>
      <td>577.0</td>
      <td>235.0</td>
      <td>342.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.5</td>
      <td>80M</td>
      <td>1949.0</td>
      <td>1656</td>
      <td>1539</td>
      <td>1398</td>
      <td>...</td>
      <td>446.0</td>
      <td>325.0</td>
      <td>512.0</td>
      <td>733</td>
      <td>782</td>
      <td>641</td>
      <td>576.0</td>
      <td>249.0</td>
      <td>327.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>남</td>
      <td>40</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84.0</td>
      <td>85M</td>
      <td>1968.0</td>
      <td>1729</td>
      <td>1597</td>
      <td>1463</td>
      <td>...</td>
      <td>461.0</td>
      <td>340.0</td>
      <td>560.0</td>
      <td>707</td>
      <td>798</td>
      <td>664</td>
      <td>595.0</td>
      <td>267.0</td>
      <td>328.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>남</td>
      <td>43</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89.6</td>
      <td>90M</td>
      <td>2005.0</td>
      <td>1715</td>
      <td>1587</td>
      <td>1456</td>
      <td>...</td>
      <td>490.0</td>
      <td>350.5</td>
      <td>569.5</td>
      <td>728</td>
      <td>796</td>
      <td>665</td>
      <td>590.0</td>
      <td>234.0</td>
      <td>356.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>남</td>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>75.6</td>
      <td>75M</td>
      <td>1954.0</td>
      <td>1646</td>
      <td>1529</td>
      <td>1398</td>
      <td>...</td>
      <td>448.0</td>
      <td>312.0</td>
      <td>491.0</td>
      <td>723</td>
      <td>766</td>
      <td>635</td>
      <td>563.0</td>
      <td>237.0</td>
      <td>326.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5087</th>
      <td>남</td>
      <td>46</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>77.0</td>
      <td>75</td>
      <td>2031.0</td>
      <td>1715</td>
      <td>1610</td>
      <td>1456</td>
      <td>...</td>
      <td>487.0</td>
      <td>326.0</td>
      <td>519.0</td>
      <td>694</td>
      <td>831</td>
      <td>677</td>
      <td>598.0</td>
      <td>281.0</td>
      <td>317.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5088</th>
      <td>남</td>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>83.0</td>
      <td>75</td>
      <td>2036.0</td>
      <td>1743</td>
      <td>1619</td>
      <td>1485</td>
      <td>...</td>
      <td>494.0</td>
      <td>350.0</td>
      <td>540.0</td>
      <td>787</td>
      <td>817</td>
      <td>683</td>
      <td>595.0</td>
      <td>280.0</td>
      <td>315.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5089</th>
      <td>남</td>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>88.0</td>
      <td>75</td>
      <td>2036.0</td>
      <td>1748</td>
      <td>1626</td>
      <td>1478</td>
      <td>...</td>
      <td>484.0</td>
      <td>351.0</td>
      <td>565.0</td>
      <td>793</td>
      <td>831</td>
      <td>683</td>
      <td>628.0</td>
      <td>311.0</td>
      <td>317.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5090</th>
      <td>남</td>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>83.5</td>
      <td>75</td>
      <td>1915.0</td>
      <td>1654</td>
      <td>1538</td>
      <td>1401</td>
      <td>...</td>
      <td>487.0</td>
      <td>341.0</td>
      <td>555.0</td>
      <td>734</td>
      <td>791</td>
      <td>654</td>
      <td>583.0</td>
      <td>283.0</td>
      <td>300.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5091</th>
      <td>남</td>
      <td>48</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>82.5</td>
      <td>75</td>
      <td>2073.0</td>
      <td>1741</td>
      <td>1632</td>
      <td>1489</td>
      <td>...</td>
      <td>492.0</td>
      <td>346.0</td>
      <td>548.0</td>
      <td>680</td>
      <td>806</td>
      <td>663</td>
      <td>583.0</td>
      <td>254.0</td>
      <td>329.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>2319 rows × 144 columns</p>
</div>



##

![image.png](attachment:image.png)



```python

```
