import asyncio
from typing import List, Dict, Any
from abc import ABC, abstractmethod
import logging

class TradingContext:
    def __init__(self):
        self.data = {}
        self.metadata = {}
        self.logs = []

class BasePlugin(ABC):
    @abstractmethod
    async def initialize(self) -> None:
        pass

    @abstractmethod
    async def process(self, context: TradingContext) -> TradingContext:
        pass

    @abstractmethod
    def can_handle(self, context: TradingContext) -> bool:
        pass

class NeuraTrade:
    def __init__(self, plugins: List[BasePlugin], config: Dict[str, Any]):
        self.plugins = plugins
        self.config = config
        self.running = False

    async def start(self):
        logging.info("Starting NeuraTrade system")
        self.running = True
        # Initialize all plugins
        for plugin in self.plugins:
            await plugin.initialize()
        while self.running:
            try:
                context = TradingContext()
                await self._process_trading_cycle(context)
                await asyncio.sleep(self.config.get('cycle_delay', 1))
            except Exception as e:
                logging.error(f"Error in trading cycle: {e}")

    async def _process_trading_cycle(self, context: TradingContext):
        for plugin in self.plugins:
            if plugin.can_handle(context):
                context = await plugin.process(context)
                logging.debug(f"Processed {plugin.__class__.__name__}")

    async def stop(self):
        self.running = False
        logging.info("Stopping NeuraTrade system")
