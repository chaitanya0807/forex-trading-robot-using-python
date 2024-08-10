# Forex Trading Robot

## Overview

This project is a Forex trading robot built using Python. The robot analyzes historical data, calculates various trading indicators like MACD and EMA, and makes trading decisions based on these indicators. It also incorporates risk management strategies to optimize trading performance.

## Features

- **Historical Data Analysis:** Analyzes past Forex data to identify trading opportunities.
- **Indicator Calculations:** Computes trading indicators such as MACD and EMA.
- **Trading Decisions:** Makes trade decisions based on indicator values and analysis.
- **Risk Management:** Implements strategies for position sizing, risk per trade, stop-loss, and target exits.

## Requirements

- Python 3.x
- pandas
- numpy
- MetaTrader 5 (or other trading platforms as needed)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/forex-trading-robot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd forex-trading-robot
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Configure the settings:** Update the configuration file with your trading preferences, such as indicator parameters and risk management settings.

2. **Run the trading script:**
    ```bash
    python trading_robot.py
    ```

3. **Monitor performance:** The robot will analyze the data, make trading decisions, and execute trades based on the configured strategies.

## Files

- `trading_robot.py`: Main script for executing the trading strategy.
- `indicators.py`: Functions for calculating MACD, EMA, and other indicators.
- `risk_management.py`: Functions for managing position sizing and risk per trade.
- `config.yaml`: Configuration file for setting parameters and preferences.
- `requirements.txt`: List of required Python packages.

## Configuration

### Configuration File (`config.yaml`)

```yaml
indicator_parameters:
  macd_fast: 12
  macd_slow: 26
  macd_signal: 9
  ema_period: 20

risk_management:
  risk_per_trade: 0.02
  position_size: 10000
  stop_loss_percentage: 1.0
  take_profit_percentage: 2.0
