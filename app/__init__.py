from flask import Flask

nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'About', 'url': '/about'}, 
    {'name': 'Contact', 'url': '/contact'}
]  

from .web.views import web_bp

app = Flask(__name__)

## 无法解决在模板或视图函数更改后,需要重启服务器才会重新渲染
## 关闭调试模式后,Flask会在每次请求时重新渲染模板,无需重启。但是,关闭调试模式也带来一定的性能损失,并且无法使用调试工具。
# app.debug = False
# 进行蓝本注册
app.register_blueprint(web_bp)

@app.route("/hw")
def hello():
    return "Hello World!"