#! C:\Users\kemfj\AppData\Local\Programs\Python\Python38-32\python.exe
print("Content-Type: text/html; charset=utf-8\n\r\n")
print()
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <form action="tts2.py" method="post">
      <p><input type="text" name="tts_text" placeholder="text"></p>
      <p><input type="text" name="file_text" placeholder="Filename extension"></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
''')
