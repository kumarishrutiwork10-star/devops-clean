from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "I got it. I got the job. I got my preferred salary. I got the perfect place. I am perfect. My life is perfect 🚀"

@app.route('/health')
def health():
    return "All OK"

if __name__ == '__main__':
    app.run(host= '0.0.0.0' , port=5000)
