from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Psychology concept
    psychology = {
        'name': '锚定效应 (Anchoring Effect)',
        'originator': 'Amos Tversky 和 Daniel Kahneman (1974)',
        'explanation': '人们在做决策时，会过分依赖第一条获得的信息（即"锚"），后续的判断会以此为基准进行调整。',
        'simple_explanation': '简单来说，就是我们容易被最初看到的数字或信息所影响，即使这个信息可能完全不相关。',
        'example': '电商平台经常使用这个效应：在商品旁边显示一个较高的"原价"，然后给出一个打折后的"现价"。即使原价可能是虚高的，消费者也会觉得现价很划算。'
    }
    
    # Product methodology
    methodology = {
        'name': 'PMF (Product-Market Fit)',
        'explanation': 'PMF是指产品与市场的契合度，代表你的产品很好地满足了市场的需求。',
        'key_points': [
            '解决真实痛点：产品必须解决用户的实际问题',
            '有足够市场：目标市场要够大，能支撑产品发展',
            '可持续性：商业模式要能持续运营',
            '用户认可：有稳定的用户群体愿意使用并付费'
        ]
    }
    
    # Latest news
    news = {
        'title': '微软发布 AI 驱动的 Windows 11 重大更新',
        'date': '2024年2月',
        'content': '微软推出了新一代Windows 11更新，集成了更强大的AI助手Copilot。这次更新使AI功能更深入地融入操作系统，包括智能文件管理、自动化任务处理等功能，标志着个人电脑进入AI时代的重要里程碑。'
    }
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>测试页面</title>
    </head>
    <body>
        <h1>测试页面</h1>
        <p>心理学概念：{{ psychology.name }}（{{ psychology.originator }}）</p>
        <p>解释：{{ psychology.explanation }}</p>
        <p>简单解释：{{ psychology.simple_explanation }}</p>
        <p>例子：{{ psychology.example }}</p>
        <p>产品方法论：{{ methodology.name }}</p>
        <p>解释：{{ methodology.explanation }}</p>
        <p>关键点：</p>
        <ul>
        {% for point in methodology.key_points %}
            <li>{{ point }}</li>
        {% endfor %}
        </ul>
        <p>最新新闻：{{ news.title }}（{{ news.date }}）</p>
        <p>内容：{{ news.content }}</p>
    </body>
    </html>
    """
    return render_template_string(html, psychology=psychology, methodology=methodology, news=news)

if __name__ == '__main__':
    app.run()
