from api.routers import orders


def load_routes(app):
    app.include_router(orders.router)
