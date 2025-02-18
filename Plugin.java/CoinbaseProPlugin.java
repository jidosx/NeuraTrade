import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class CoinbaseProPlugin {
    private String apiKey;
    private String apiSecret;
    private String passphrase;

    public CoinbaseProPlugin(String apiKey, String apiSecret, String passphrase) {
        this.apiKey = apiKey;
        this.apiSecret = apiSecret;
        this.passphrase = passphrase;
    }

    public String getLivePrice(String symbol) throws Exception {
        URL url = new URL("https://api.pro.coinbase.com/products/" + symbol + "/ticker");
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("CB-ACCESS-KEY", this.apiKey);
        connection.setRequestProperty("CB-ACCESS-SIGN", this.apiSecret);
        connection.setRequestProperty("CB-ACCESS-PASSPHRASE", this.passphrase);

        int responseCode = connection.getResponseCode();
        if (responseCode == 200) {
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            return response.toString();
        } else {
            return null;
        }
    }
}
