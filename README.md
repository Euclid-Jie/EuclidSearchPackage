# EuclidSearchPackage

this package is include some tools to get data from weibo、zhihu、guba and etc.

The project will continue to be updated and you are welcome to join us on [GitHub](https://github.com/Euclid-Jie/EuclidSearchPackage).

## Existing features

### 1、 get single weibo's reposts data, the data will write to MongoDB

```python
Get_single_weibo_details('reposts', mblogid='MrOtA75Fd', header=Set_header('cookie.txt')).main_get()
```
### 2、 get single weibo's data

```python
data_json = Get_single_weibo_data(mblogid='MrOtA75Fd')
print(data_json)
```
### 3、 get the weibo url list

set the url(contains keyword),  then  item in list is `"1562868034/MkXTBh9Fk"`, which is contains uid and mblogid

```python
url_list = Get_item_url_list('https://s.weibo.com/weibo?q=杭州公园')
print(url_list)
```
### 4、get user's info

```python
data_json = Get_user_info('1202150843', Set_header('cookie.txt'))
print(data_json)
```
### 5、get user's all blog

```python
Get_user_all_weibo(7416119836, 100, begin=50)
```