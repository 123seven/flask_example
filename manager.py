# @Time    : 2020-04-28 17:11
# @Author  : Seven
# @File    : manager.py
# @Desc    : 项目入口

from app.app import creat_app

app = creat_app()

if __name__ == '__main__':
    app.run(debug=True)
