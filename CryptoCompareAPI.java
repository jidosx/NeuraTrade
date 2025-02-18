import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class CryptoCompareAPI {
    private String apiKey;

    public CryptoCompareAPI(String apiKey) {
        this.apiKey = apiKey;
    }

    public String getLivePrice(String symbol) throws Exception {
        URL url = new URL("https://min-api.cryptocompare.com/data/price?fsym=" + symbol + "&tsyms=USD");
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Apikey " + this.apiKey);

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
