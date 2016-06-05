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

#### 四，上传图片
django 1.8，在模型中（admin app），首先安装Pillow，3.x无法安装

    pip install Pillow==2.8.0
    
app中models创建图片模型

    // models.py
    class ProductImg(models.Model):
        img = models.ImageField(upload_to='company/')   # 图片上传到media_root下的company文件夹
project中设置图片文件路径

    // settings.py
    MEDIA_ROOT = os.path.join(BASE_DIR，'media')
    MEDIA_URL = '/media/'
    
意思为在project同目录文件夹中创建media文件夹存放图片或其他文件

    // project目录中settings.py
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns = [
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
templates中显示图片
    
    // template.html
    <img src="media/{{img.img.url}}" />
    
#### TODOLIST:
1，根据公司列表点击相应的公司名称才渲染出与该名称对应的新闻列表，不使用TAB切换，避免数据一次性输出全部
`已完成`
2，admin中TextField集成符文本编辑器  
`Done`
3，增加新闻列表分页
`Done`

