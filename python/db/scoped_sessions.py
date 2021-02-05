__all__ = ["app"]

## see: https://docs.sqlalchemy.org/en/13/orm/session_basics.html

import os

from sanic import Sanic
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def app():
    app = Sanic("middleware db test", strict_slashes=True)

    #
    @app.listener('before_server_start')
    def setup_db(app, loop):
        app.db = create_engine(
            "postgres://postgres:docker@localhost:5432/postgres",
            pool_size=15,
            max_overflow=10,
            pool_timeout=20,
            echo=True,
            echo_pool="debug",
            pool_pre_ping=True,
        )

    @app.listener('after_server_stop')
    def close_db(app, loop):
        app.db.close_db()

    @app.middleware('request')
    async def print_on_request(request):
        print(f"pid/worker_id: {os.getpid()}")
        print(f"engine hash: {app.db.engine.__hash__()}")
        # that scopefunc will ensure that the session is only used within a specific request
        request.ctx.session = plz = scoped_session(sessionmaker(bind=request.app.db.engine), scopefunc=request.__hash__)
        print(f"session hash: {hash(plz)}")

    @app.middleware('response')
    async def print_on_response(request, response):
        request.ctx.session.commit()
        request.ctx.session.close()
        # must call remove to remove the scoped session from the global scope dictionary
        # see: https://docs.sqlalchemy.org/en/13/orm/contextual.html
        request.ctx.session.remove()

    # for blueprint in blueprints:
    #     app.blueprint(blueprint)
    return app
