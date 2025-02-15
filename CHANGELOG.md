# Changelog

All notable changes to this project will be documented in this file.
See Conventional Commits for commit guidelines.
0.1.2 (2025-03-15)
NeuraTrade v0.1.2: "Market Pulse" Evolution

The initial release of NeuraTrade, a composable, plugin-based AI trading framework, has evolved to include:

    Enhanced trading strategies with customized model implementations
    Expanded market connectors for increased platform coverage
    Improved error handling for robustness and reliability
    Comprehensive documentation for seamless integration and development

Packages

    Core
        @neuratrade/core - The core framework for building AI trading agents
    Official Plugins
        Trading Strategies
            @neuratrade/strategy-lstm - A customized Long Short-Term Memory (LSTM) trading strategy provider
            @neuratrade/strategy-gru - A customized Gated Recurrent Unit (GRU) trading strategy provider
        Market Connectors
            @neuratrade/plugin-alpaca - A plugin for integrating with Alpaca API for trading
            @neuratrade/plugin-tdameritrade - A plugin for integrating with TD Ameritrade API for trading
            @neuratrade/plugin-interactivebrokers - A plugin for integrating with Interactive Brokers API for trading
            @neuratrade/plugin-kraken - A plugin for connecting to the Kraken exchange
        Data Storage
            @neuratrade/storage-mongodb - A MongoDB-based data storage provider for storing trading data
            @neuratrade/storage-postgresql - A PostgreSQL-based data storage provider for storing trading data
            @neuratrade/storage-timescaledb - A TimescaleDB-based data storage provider for storing trading data

All notable changes to this project will be documented in this file.

## [0.1.2] - 2025-03-14

### Added

* Enhanced trading strategies with customized model implementations
* Expanded market connectors for increased platform coverage
* Improved error handling for robustness and reliability
* Comprehensive documentation for seamless integration and development

### Changed

* Updated dependencies to ensure compatibility with latest versions
* Refactored code for improved readability and maintainability

### Removed

* Removed deprecated code and unnecessary dependencies

## [0.1.1] - 2025-02-10

### Added

* Initial release of NeuraTrade, a composable, plugin-based AI trading framework
* Core framework for building AI trading agents
* Official plugins for trading strategies, market connectors, and data storage

### Changed

* Initial commit of project structure and documentation

## [0.1.0] - 2025-01-28

### Added

* Initial commit of project idea and proposal
