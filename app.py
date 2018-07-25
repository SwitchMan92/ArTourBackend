from services.api import app
from controlers.api import load_resources

if __name__ == '__main__':
    load_resources()
    app.run(host="0.0.0.0", debug=True)
