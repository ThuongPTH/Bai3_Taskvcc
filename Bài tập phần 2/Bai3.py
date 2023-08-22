from flask import request, Flask
import math

app = Flask(__name__)

def check(num):
    if num < 2 : return False
    elif num == 2 : return True
    elif num % 2 == 0 : return False
    else:
        for i in range(3,int(math.sqrt(num))+1):
            if num % i == 0 : return False
    return True

@app.route('/prime', methods = ['GET'])
def my_route():
    n = int(request.args.get('n'))
    listprime = [num for num in range(1, n+1) if check(num)]
    return listprime

if __name__ == '__main__':
    app.run(port = 8080)

/* Chinh sua tren server github */
