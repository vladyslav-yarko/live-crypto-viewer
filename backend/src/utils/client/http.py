from typing import Optional
# from functools import wraps

from aiohttp import ClientSession, ClientResponse

from src.utils.client.client import Client


class HTTPClient(Client):
    def __init__(
        self,
        base_url: str,
        endpoint: str ='',
        params: Optional[dict] = None,
        payload: Optional[dict] = None
        ):
        self.session: ClientSession = None
        self.base_url = base_url
        self.endpoint = endpoint
        self.params = params
        self.payload = payload

    async def open_session(self) -> None:
        self.session = ClientSession(
            base_url=self.base_url
        )

    async def close_session(self) -> None:
        await self.session.close()

    async def get(self) -> ClientResponse:
        response = await self.session.get(
            url=self.endpoint,
            params=self.params
            )
        return response

    async def post(self) -> ClientResponse:
        response = await self.session.post(
            url=self.endpoint,
            json=self.payload,
            params=self.params
            )
        return response
