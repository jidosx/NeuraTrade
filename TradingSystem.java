import java.util.ArrayList;
import java.util.List;

public class TradingSystem {
    private NeuraTrade neuraTrade;
    private CryptoCompareAPI cryptoCompareAPI;

    public TradingSystem(NeuraTrade neuraTrade, CryptoCompareAPI cryptoCompareAPI) {
        this.neuraTrade = neuraTrade;
        this.cryptoCompareAPI = cryptoCompareAPI;
    }

    public void startTrading() throws Exception {
        // Get live price from CryptoCompare API
        String symbol = "BTC";
        String livePrice = this.cryptoCompareAPI.getLivePrice(symbol);

        // Make trading decision based on live price
        if (livePrice != null) {
            double price = Double.parseDouble(livePrice);
            if (price > 10000) {
                // Buy
                Trade trade = new Trade(symbol, price, 1);
                this.neuraTrade.addTrade(trade);
            } else {
                // Sell
                Trade trade = new Trade(symbol, price, -1);
                this.neuraTrade.addTrade(trade);
            }
        }
    }
}
