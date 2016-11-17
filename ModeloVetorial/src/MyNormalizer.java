public class MyNormalizer {

    public static String normalize(String str) {
        String ret = str.toLowerCase();
        return java.text.Normalizer.normalize(ret, java.text.Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "");
    }
}
