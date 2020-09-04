from django.db import models

# Create your models here.
class DB_tucao(models.Model):
    '''
    吐槽表，存放吐槽的内容
    '''
    user=models.CharField(max_length=30,null=True)   #吐槽人姓名
    text=models.CharField(max_length=1000,null=True) #吐槽的内容
    ctime=models.DateTimeField(auto_now=True)        #创建时间

    def __str__(self):
        return self.text+str(self.ctime)


class DB_home_href(models.Model):
    '''
    首页的超链接传送门表
    '''
    name=models.CharField(max_length=30,null=True)    #超链接名字
    href=models.CharField(max_length=2000,null=True)  #超链接内容

    def __str__(self):
        return self.name


