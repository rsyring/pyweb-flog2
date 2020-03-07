import falcon


class Response:
    count = 0

    def on_get(self, req, resp):
        self.count += 1
        resp.body = f'benchmark falcon: {self.count}'

    def on_post(self, req, resp):
        self.on_get(req, resp)


falcon_app = falcon.API(media_type=falcon.MEDIA_HTML)
falcon_app.add_route('/', Response())

if False:  # hide notes
    pass
    # notes
    # pip install falcon waitress
    # waitress-serve --port=5000 things:app
    # ab -t 5 -c 1 = 2445 / sec
    # ab -t 5 -c 5 = 3326 / sec
    # ab -t 5 -c 15 = 3401 / sec

    # pip install gunicorn meinheld
    # ab -t 5 -c 5 = 20,410 / sec
