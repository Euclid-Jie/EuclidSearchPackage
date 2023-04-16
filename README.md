# EuclidSearchPackage

this package is include some tools to get data from weibo、zhihu、guba and etc.

The project will continue to be updated and you are welcome to join us on [GitHub](https://github.com/Euclid-Jie/EuclidSearchPackage).

## How to use

### 1、install this package

```shell
pip install EuclidSearchPackage
```

### 2、set cookie and import package

```python
import EuclidSearchPackage as ESP
ESP.Set_cookie('cookie.txt')  # 'cookie.txt' is your local cookie file path
```

### 3、use `WeiboClassV1 ` to get data

```python
timeBegin = '2023-03-01-0'
timeEnd = '2023-03-10-0'
demoClass = ESP.WeiboClassV1(Mongo=False)
demoClass.main_get(['北师大', '珠海'], timeBegin, timeEnd)
```

### 4、use `WeiboClassV3` to get data

compare to `WeiboClassV2`, `WeiboClassV3` use thread to get data more fast.

```python
ESP.WeiboClassV3('北师大', Mongo=False, max_work_count=20, LongText=False).main('2023-03-11-00', '2023-03-27-21')
```

## Existing features

you can use these methods to fulfill yours purpose, just like `WeiboClassV2`


### 1、 get single weibo's data

```python
data_json = ESP.Get_single_weibo_data(mblogid='MrOtA75Fd')
print(data_json)
```
### 2、 get the weibo url list

set the url(contains keyword),  then  item in list is `"1562868034/MkXTBh9Fk"`, which is contains uid and mblogid

```python
url_list =  ESP.Get_item_url_list('https://s.weibo.com/weibo?q=杭州公园')
print(url_list)
```
### 3、get user's info

```python
data_json =  ESP.Get_user_info('1202150843')
print(data_json)
```
### 4、get user's all blog

```python
 ESP.Get_user_all_weibo(2656274875, 100, query='主播说联播', colName='主播说联播', csv=True)
```
