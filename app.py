from services.api import app
from controlers.api import load_resources

if __name__ == '__main__':
    load_resources()
    app.run(debug=True)
