import java.util.ArrayList;
import java.util.List;

public class NeuraTrade {
    private List<Trade> trades;

    public NeuraTrade() {
        this.trades = new ArrayList<>();
    }

    public void addTrade(Trade trade) {
        this.trades.add(trade);
    }

    public List<Trade> getTrades() {
        return this.trades;
    }
}
