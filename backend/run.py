# run.py
from app import create_app
from app.routes import auth, reviews

app = create_app()

# Register blueprints
app.register_blueprint(auth.auth, url_prefix='/auth')
app.register_blueprint(reviews.reviews, url_prefix='/reviews')

if __name__ == "__main__":
    app.run(ssl_context=("cert.pem", "key.pem"))
