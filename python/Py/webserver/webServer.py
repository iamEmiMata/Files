
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = '127.0.0.1'
serverPort = 8080

script = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Python</title>

	<style>
		* {
			padding: 0;
			margin: 0;
			font-family: sans-serif;
			text-decoration: none;
			list-style: none;
		}

		body {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
		}


		main {
			margin-top: 50px;
			border:5px solid #B69DFC;
			border-radius: 10px;
			padding: 50px;
			display: flex;
			justify-content: center;
			align-items: center;
			max-width: 50%;
			flex-direction: column;
			box-shadow: 2px 4px 8px #ddd;
		}

		section {
			display: flex;
			justify-content: center;
			align-items: center;
			flex-direction: column;
		}

		section img {
			border-radius: 50%;
			width: 120px;
			height: 120px;
			padding: 20px 0;
		}

		section p {
			padding: 20px 0;
			text-align: justify;
		}

		.social ul {
			display: flex;
			justify-content: space-between;
			align-items: center;
		}

		.social ul li {
			padding-right: 20px;
		}

		.social ul li a {
			padding-right: 10px;
			color: #B69DFC;
			transition: 0.6s all ease;
			font-weight: bold;
		}

		.social ul li a:hover {
			background-color: #B69DFC;
			color: #000;
			transition: 0.6s all ease;
		}

	</style>

</head>
<body>
	<main>
		<section>
			<img src="http://127.0.0.1/files/python/Py/webserver/me.jpg" alt="emilia img">
			<h2>Emi Mata</h2>
			<p>Hello there, I'm Emilia, <i>I'm programmer and graphic designer<i>, since two years ago I work as programmer using SQL, Python, Js, Php and Arduino also I design graphic resources as icons, illustration art, etc.
		</section>

		<section class="social">
			<ul>
				<li>
					<a href="#">Instagram</a>
				</li>
				<li>
					<a href="#">Youtube</a>
				</li>
				<li>
					<a href="#">Github</a>
				</li>
			</ul>
		</section>
	</main>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(bytes(script, 'utf-8'))

if __name__ == '__main__':
	webServer = HTTPServer((hostName, serverPort), MyServer)
	print('Server started http://%s:%s' % (hostName, serverPort))
try:
	webServer.serve_forever()
except KeyboardInterrupt:
	pass


webServer.server_close()
print('Server stopped')