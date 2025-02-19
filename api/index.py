from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
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

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>每日一学</title>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                padding: 2rem;
                max-width: 800px;
                margin: 0 auto;
                background-color: #f5f5f5;
            }}
            .card {{
                background: white;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h1, h2 {{
                color: #333;
            }}
            .key-points {{
                list-style-type: none;
                padding-left: 0;
            }}
            .key-points li {{
                margin-bottom: 10px;
                padding-left: 20px;
                position: relative;
            }}
            .key-points li:before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <h1>每日一学</h1>
        
        <div class="card">
            <h2>今日心理学概念</h2>
            <h3>{psychology['name']}</h3>
            <p><strong>提出者：</strong>{psychology['originator']}</p>
            <p><strong>解释：</strong>{psychology['explanation']}</p>
            <p><strong>简单说明：</strong>{psychology['simple_explanation']}</p>
            <p><strong>实例：</strong>{psychology['example']}</p>
        </div>

        <div class="card">
            <h2>产品方法论</h2>
            <h3>{methodology['name']}</h3>
            <p>{methodology['explanation']}</p>
            <h4>关键要点：</h4>
            <ul class="key-points">
                {''.join([f'<li>{point}</li>' for point in methodology['key_points']])}
            </ul>
        </div>

        <div class="card">
            <h2>科技新闻</h2>
            <h3>{news['title']}</h3>
            <p><strong>日期：</strong>{news['date']}</p>
            <p>{news['content']}</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
