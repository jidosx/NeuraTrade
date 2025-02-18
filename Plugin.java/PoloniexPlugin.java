import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class PoloniexPlugin {
    private String apiKey;
    private String apiSecret;

    public PoloniexPlugin(String apiKey, String apiSecret) {
        this.apiKey = apiKey;
        this.apiSecret = apiSecret;
    }

    public String getLivePrice(String symbol) throws Exception {
        URL url = new URL("https://poloniex.com/public?command=returnTicker&currency
