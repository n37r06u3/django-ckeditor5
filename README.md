Django CKEditor 5
===

# 介绍 #
本项目整合了新版 [CKEditor 5](https://ckeditor.com/ckeditor-5/) 到Django. 老版本[django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) 仍然在使用[CKEditor 4](https://ckeditor.com/ckeditor-4/). 

根据 [ckeditor.com](https://ckeditor.com/docs/ckeditor5/latest/builds/guides/migrate.html)官方说明，CKEditor 5是一个你没有用过的船新版本。

整体上仍然使用 [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor/tree/master/ckeditor)项目的架构。不同点是：

- `static/ckeditor5` 包含最新的CKEditor 5经典编辑器（版本会随时更新，尽量与官方同步），[CKEditor 5下载](https://ckeditor.com/ckeditor-5/download/).
- 移除了`extraPlugins`，老的一些插件，如代码插入编辑，目前不可以使用，需要其他方案。
- 修改了`static/ckeditor5/ckeditor-init.js`部分代码， 在 `initialiseCKEditor` 方法里:
    + extraPlugins处理方法代码被删除
    + CKEditor 5 使用 `ClassicEditor.create` 来初始化创建编辑器，而不是用4的 `CKEDITOR.replace`

# 安装 #
pip install django-ckeditor5

升级
pip install django-ckeditor5 -U 

github
pip install git+https://github.com/n37r06u3/django-ckeditor5

# 测试 #
下载源码解压
cd ckeditor5_demo

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/admin/

# 参考 #
https://github.com/django-ckeditor/django-ckeditor

https://ckeditor.com/ckeditor-4/

https://github.com/pancodia/django-ckeditor5

https://ckeditor.com/ckeditor-5/

# 变更 #

20190304 - v0.0.1 初始化项目 CKEditor 5集成v11.0.1, 新版本django2.1.7测试可用

20190304 - v0.0.2 添加demo

20190304 - v0.0.3 添加大小配置

# TODO #
添加代码格式化插件

添加图片上传插件

添加html源码查看插件

完善安装说明
