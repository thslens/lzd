import fastapi
import lazop_sdk
from lazop_sdk.base import *
import datetime

app = fastapi.FastAPI()

@app.get("/create_token")
async def create_token(code ='0_100132_2DL4DV3jcU1UOT7WGI1A4rY91' , uuid: str = None):
    url = "https://auth.lazada.com/rest"
    client = lazop.LazopClient(url, appkey="118458", appSecret="aWAppvLaHEqBYFlacDcY7TFnlk68rYpX")
    request = lazop.LazopRequest('/auth/token/create')
    request.add_api_param('code', code )
    request.add_api_param('uuid', uuid)
    response = await client.execute(request)

    return {
        "type": response.type,
        "body": response.body,
    }

@app.get("/refresh_token")
async def refresh_token(refresh_token = '50001600212wcwiOabwyjtEH11acc19aBOvQr9ZYkYDlr987D8BB88LIB8bj'):
    url = "https://auth.lazada.com/rest"
    client = lazop.LazopClient(url, appkey="118458", appSecret="aWAppvLaHEqBYFlacDcY7TFnlk68rYpX")
    request = lazop.LazopRequest('/auth/token/refresh')
    request.add_api_param('access_token', create_token)
    
    request.add_api_param('refresh_token', '50001600212wcwiOabwyjtEH11acc19aBOvQr9ZYkYDlr987D8BB88LIB8bj')
    request.add_api_param('refresh_expires_in', '60')
    request.add_api_param('expires_in', '10')
    request.add_api_param('timestamp', datetime.datetime.now().timestamp())
    request.add_api_param('sign_method', 'HMAC-SHA256')
    response = await client.execute(request)
    return {
        "type": f"{response.type}",
        "body": f"{response.body}",
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



"""
@app.get("/get_vouchers")
async def get_vouchers(access_token: str, cur_page: int = 1, voucher_type: str = "COLLECTIBLE_VOUCHER", name: str = None, page_size: int = 10, status: str = None):
    url = "https://api.lazada.vn/rest"
    client = lazop.LazopClient(url, appkey, appSecret)
    request = lazop.LazopRequest('/promotion/vouchers/get', 'GET')
    request.add_api_param('cur_page', cur_page)
    request.add_api_param('voucher_type', voucher_type)
    request.add_api_param('name', name)
    request.add_api_param('page_size', page_size)
    request.add_api_param('status', status)
    response = await client.execute(request, access_token)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) """
