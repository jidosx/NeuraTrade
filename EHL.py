import loguru

logger = loguru.logger

try:
  # Code that may raise an exception
  agent = Agent('AAPL', '1min')
  agent.calculate_indicators()
  agent.train_model()
  agent.predict()
except Exception as e:
  # Handle exception and log error
  logger.error(f'Error: {e}')
