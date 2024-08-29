# NOTE: MVC模型
#  MVC模型将Web后端代码分为三个层次：
#  M：Model模型层，实现业务对象和数据库对象之间的映射
#  V：View视图层，负责业务逻辑和用户交互
#  C：Controller控制层，实现用户请求到视图层的调用

# NOTE: MTV模型——Django框架
#  除了和MVC模型定义上不同外，解耦和依赖解决方面均采用相同的处理逻辑
#  M：model模型层
#  T：Template页面模板
#  V：View视图层
#  用户请求->URL控制器->view视图->[Model模型]->Template模板->返回HTML

# django-admin startproject mysite
# cd mysite
# python manage.py startapp myapp
# python manage.py runserver 127.0.0.1:8000
