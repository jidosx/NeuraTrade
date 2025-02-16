import asyncio
import json

class DeepSeekApiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v2"

    async def _make_request(self, endpoint: str, method: str, data: dict = None):
        # Make asynchronous request to DeepSeek API
        async with aiohttp.ClientSession() as session:
            async with session.request(method, self.base_url + endpoint, headers={"Authorization": f"Bearer {self.api_key}"}, data=data) as response:
                return await response.json()

    async def get_market_data(self, symbol: str):
        # Retrieve market data for the specified symbol
        return await self._make_request(f"/market-data/{symbol}", "GET")

    async def analyze_market_data(self, market_data: pd.DataFrame):
        # Perform analysis on the provided market data
        return await self._make_request("/analyze", "POST", data=market_data.to_dict())
