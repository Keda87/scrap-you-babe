from sanic import Sanic
from sanic.response import json

from services import do_scrap_askfm
from utils import render_error_response, render_success_response

app = Sanic(strict_slashes=True)


@app.route('/')
async def index(request):
    return json({'hello': 'world'})


@app.route('/scrap/askfm', methods=['POST'])
async def scrap_askfm(request):
    username = request.json.get('username', None)
    if username is None:
        message = 'Username is required.'
        response = render_error_response(message=message)
        return json(response, status=400)
    scrap_result = do_scrap_askfm(username=username)
    response = render_success_response(result=scrap_result)
    return json(response)


@app.route('/scrap/success')
async def result(request):
    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

