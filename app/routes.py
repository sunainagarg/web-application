from app import app
@app.route('/')
@app.route('/index')
def index():
 user={'username':'sunaina'}
 return '''
<html>
 <head>
   <title> my APPLICATION</title>
</head>
<body>
  <h1>hello, ''' + user['username'] +''' !</h1>
</body>
</html>'''