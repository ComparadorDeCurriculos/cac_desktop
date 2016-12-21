import java.util.Iterator;
import java.util.Map;

public class ModeloVetorialUtils {

    public static String normalize(String str) {
        String ret = str.toLowerCase();
        return java.text.Normalizer.normalize(ret, java.text.Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "");
    }

    public static boolean isNumeric(String str)
    {
        return str.matches("[+-]?\\d*(\\.\\d+)?");
    }

    public static void printMap(Map mp) {
        Iterator it = mp.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            System.out.println(pair.getKey() + " = " + pair.getValue());
            it.remove(); // avoids a ConcurrentModificationException
        }
    }
}
