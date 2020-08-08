from todo import app
import os


print(os.path.dirname(__file__))
if __name__ == '__main__':
    
    app.run()
    # app.run(port = int(os.environ.get('PORT', 33507)))

