from api.routers import orders, ratings, customers, payments, promotions, resources, menu_items


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(ratings.router)
    app.include_router(customers.router)
    app.include_router(payments.router)
    app.include_router(promotions.router)
    app.include_router(menu_items.router)
    app.include_router(resources.router)


