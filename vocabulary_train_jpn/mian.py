from flask import Flask, request, render_template
import vocabulary_train_jpn as vo

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def poker():
    if request.method == 'GET':
        outStr = """
        <html>
            <head>
                <title>日翻中字典</title>
            </head>
            <body>
                <h1><font face="fantasy" color="#4F4FFF">請輸入想找的詞彙</font></h1>
                <form action="/" method="post">
                      <h2><font face="monospace" color="#00D1D1">Please enter the keyword:</font></h2>
                          <input type="textbox" name="keyword_str">
                      <br>
                      <button type="submit" style="width:120px;height:40px;font-size:20px;">Submit</button>
                </form>
            </body>
        </html>
        """
        return outStr
    elif request.method == 'POST':
        keyword_str = str(request.form.get('keyword_str'))
        vo.train_jpy(keyword_str)
        ans = vo.ans
        return ans

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)