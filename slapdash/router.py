from dash.dependencies import Output, Input

from .server import app
from .pages import page_not_found, page1, page2, page3
from .layouts import navbar
from .settings import (CONTENT_CONTAINER_ID, NAVBAR_CONTAINER_ID,
                       URL_BASE_PATHNAME, NAVBAR)


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with
# URL_BASE_PATHNAME) and 'layout' is a Dash Component.
urls = (
    ('', page1),
    ('page1', page1),
    ('page2', page2),
    ('page3', page3),
)


routes = {f'{URL_BASE_PATHNAME}{route}': layout
          for route, layout in urls}


# The router callback
@app.callback(Output(CONTENT_CONTAINER_ID, 'children'),
              [Input('url', 'pathname')])
def router(pathname):
    default_layout = page_not_found(pathname)
    return routes.get(pathname, default_layout)


if NAVBAR:
    # Callback that regenerates navbar with current page as active when the URL
    # of the app changes.
    @app.callback(
        Output(NAVBAR_CONTAINER_ID, 'children'),
        [Input('url', 'pathname')])
    def update_nav(pathname):
        # note: pathname is None on the first load of the app for some reason
        return navbar(orientation=NAVBAR, active_path=pathname)
