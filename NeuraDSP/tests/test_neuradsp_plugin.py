# tests/test_neuradsp_plugin.py
import unittest
from neuradsp_plugin import NeuraDSPPlugin

class TestNeuraDSPPlugin(unittest.TestCase):
    def test_initialize(self):
        plugin = NeuraDSPPlugin("path/to/model", "your_api_key")
        plugin.initialize()
        self.assertIsNotNone(plugin.model)

    def test_process(self):
        plugin = NeuraDSPPlugin("path/to/model", "your_api_key")
        plugin.initialize()
        trading_context = {"data": {"market_data": np.random.rand(10, 1)}}
        result = plugin.process(trading_context)
        self.assertIn("predicted_trends", result["data"])

if __name__ == "__main__":
    unittest.main()
