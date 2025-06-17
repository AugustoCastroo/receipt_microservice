class Route():

    def init_app(self, app):
        from app.controllers import receipt_bp
        app.register_blueprint(receipt_bp, url_prefix='/api/v1')