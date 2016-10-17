import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.text.Normalizer;
import java.util.ArrayList;

public class StopList {
    public final String filename;
    private ArrayList<String> stopWords;


    public StopList(String filename){
        BufferedReader bfr;
        String s = "a";

        this.filename = filename;

        try{
            bfr = new BufferedReader(new FileReader(this.filename));
            System.out.println("Stoplist loaded from file \"" + this.filename + "\".");
        } catch (FileNotFoundException e) {
            System.out.println("File \"" + this.filename + "\" not found.");
            return;
        }

        //creating a arrayList to store stopwords
        this.stopWords = new ArrayList<>();

        do{
            try{s = bfr.readLine();}catch(Exception e){};
            if (s != null){
                System.out.print(s);
                s = normalize(s);
                if(s != null && s.length() > 0){
                    if(!stopWords.contains(s))stopWords.add(s);
                }
            }
        }while(s != null);
    }

    public boolean hasWord(String word){
        String s = word;
        s = normalize(s);
        return stopWords.contains(s);
    }

    public static String normalize(String str) {
        return Normalizer.normalize(str, Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "");
    }
}
