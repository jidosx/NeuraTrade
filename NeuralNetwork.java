import java.util.ArrayList;
import java.util.List;

public class NeuralNetwork {
    private List<Layer> layers;

    public NeuralNetwork() {
        this.layers = new ArrayList<>();
    }

    public void addLayer(Layer layer) {
        this.layers.add(layer);
    }

    public List<Layer> getLayers() {
        return this.layers;
    }
}
