## Django开发企业官网



### Tips：
#### 一，与mysql连接
使用pip安装**pymysql**作为connector，python3后不使用mysql-python  
安装好pymysql后，在project目录中与**settings**目录同一文件夹中的**__init__.py**文件中:

        import pymysql
        pymysql.install_as_MySQLdb()

在settings中设置database:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'website',  # database name
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

#### 二，修改admin后台显示语言
django1.9后

        LANGUAGE_CODE = 'zh-cn'
无效  
需修改为:

    LANGUAGE_CODE = 'zh-hans'

#### 三，创建模型时，需将数据库编码设置为utf8
在mysql中创建数据库时，应设置编码`(windows下可使用mysql unicode bash创建，linux下用terminal创建数据库需设置编码)`:

    CREATE DATABASE (DATABASE NAME) CHARACTER SET utf8;
