

import webapp2
from caesar import encrypt

# html
page_header = """
<!DOCTYPE html>
<html>
<head>
	<title>Caesar Cipher</title>
</head>

<body>
	<h2>Caesar Cipher</h2>
	<form action "/rotate" method="post">
		<textarea name = "text" style = "height: 100px; width: 400px;">{0}</textarea>
		<br>
		<label>Pick a Number
		<input name = "num">
		</label>
		<input type ="submit">
	</form>
</body>
<html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(page_header)

    def post(self):
    	text = self.request.get("text")
    	num = int(self.request.get("num"))

    	answer = encrypt(text, num)

    	self.response.out.write(page_header.format(answer))
    	

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
