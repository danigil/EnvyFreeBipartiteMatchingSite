from website_code import app
import sys
app.config['DEBUG'] = True

if __name__ == '__main__':
    print(sys.argv[1])
    app.run(host='0.0.0.0', port = int(sys.argv[1]))
