from app import create_app
from config import PostgresSqlConfig


if __name__ == '__main__':
    my_app = create_app(PostgresSqlConfig)
    my_app.run(debug=True)
