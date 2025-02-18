import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class OKExPlugin {
    private String apiKey;
    private String apiSecret;

    public OKExPlugin(String apiKey, String apiSecret) {
        this.apiKey = apiKey;
        this.apiSecret = apiSecret;
    }

    public String getLivePrice(String symbol) throws Exception {
        URL url = new URL("https://www.okex.com/api/v1/ticker.do?symbol=" + symbol);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("OK-ACCESS-KEY", this.apiKey);
        connection.setRequestProperty("OK-ACCESS-SIGN", this.apiSecret);

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
