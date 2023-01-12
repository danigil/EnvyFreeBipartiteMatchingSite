from website_code import app

# import logging
# logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
  app.run(debug=True, host="localhost", port=25656)
