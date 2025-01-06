import java.util.*;

public class RodCutting {
    public static void main(String[] args) {
        int[] inches = {1, 2, 3, 4};
        int[] price = {5, 4, 3, 6};
        int rodLength = 5;
        optimalCut(inches, price, rodLength);
        float[] pricePerInches = calculatePricePerInches(inches, price);
    }

    public static void optimalCut(int[] inches, int[] price, int rodLength) {
        int newRodLength = rodLength;
        
    }

    public static float[] calculatePricePerInches(int[] inches, int[] price) {
        float[] pricePerInches = new float[inches.length];

        for (int i = 0; i < inches.length; i++) {
            pricePerInches[i] = (float)price[i] / inches[i];
        }

        return pricePerInches;
    }
}