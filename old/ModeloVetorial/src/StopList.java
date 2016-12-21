import java.io.*;
import java.text.Normalizer;
import java.util.ArrayList;

public class StopList {
    public final String filename;
    private ArrayList<String> stopWords;


    public StopList(String filename){
        BufferedReader bfr;
        String s = "a";

        this.filename = filename;


        try {
            bfr = new BufferedReader(new InputStreamReader(new FileInputStream(filename), "ISO-8859-1"));
        } catch (Exception e){ return;}

        //creating a arrayList to store stopwords
        this.stopWords = new ArrayList<>();

        bfr = null;
        do{
            try{s = bfr.readLine();}catch(Exception e){}
            if (s != null){
                s = ModeloVetorialUtils.normalize(s);
                if(s != null && s.length() > 0){
                    if(!stopWords.contains(s))stopWords.add(s);
                }
            }
        }while(s != null);

        try{bfr.close();}catch(Exception e){}
    }

    public StopList(){
        this.filename = null;
        //creating a arrayList to store stopwords
        this.stopWords = new ArrayList<>();
    }

    public boolean hasWord(String word){
        String s = word;
        s = ModeloVetorialUtils.normalize(s);
        return stopWords.contains(s);
    }

    public void insertWord(String word) {
        String s = word;
        s = ModeloVetorialUtils.normalize(s);
        if (s != null && s.length() > 0) stopWords.add(s);
    }
}
