import unittest
from unittest.mock import Mock, patch
from neura_dsp_plugin import NeuraDSPPlugin

class TestNeuraDSPPlugin(unittest.TestCase):
    def test_initialize(self):
        # Test plugin initialization
        plugin = NeuraDSPPlugin("model_path", "deepseek_api_key")
        # ...
        self.assertIsNotNone(plugin.model)
        self.assertIsNotNone(plugin.deepseek_client)

    @patch("neura_dsp_plugin.deepseek_api.DeepSeekApiClient")
    def test_process(self, mock_deepseek_client):
        # Test plugin processing
        plugin = NeuraDSPPlugin("model_path", "deepseek_api_key")
        market_data = pd.DataFrame({"column": [1, 2, 3]})
        context = TradingContext()
        context.data["market_data"] = market_data
        # ...
        self.assertIn("neura_dsp_analysis", context.data)
