import numpy as np
import pandas as pd
from iNeuraTrade import BasePlugin
from .deepseek_api import DeepSeekApiClient

class NeuraDSPPlugin(BasePlugin):
    def __init__(self, model_path: str, deepseek_api_key: str):
        self.model_path = model_path
        self.deepseek_api_key = deepseek_api_key
        self.model = None
        self.deepseek_client = None

    async def initialize(self):
        # Initialize DeepSeek client
        self.deepseek_client = await self._init_deepseek_client(self.deepseek_api_key)
        # Load NeuraDSP model
        self.model = await self._load_model(self.model_path)

    async def process(self, context: TradingContext) -> TradingContext:
        market_data = context.data['market_data']
        # Perform DeepSeek analysis
        analysis = await self._perform_deepseek_analysis(market_data, self.model, self.deepseek_client)
        context.data['neura_dsp_analysis'] = analysis
        return context

    def can_handle(self, context: TradingContext) -> bool:
        return 'market_data' in context.data and 'neura_dsp_analysis' not in context.data
