import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.lang.reflect.Array;
import java.util.ArrayList;

public class WordVector {
    private ArrayList<String> bagOfWords;
    private ArrayList<String> documents;
    private StopList stopList;

    public WordVector(){
        bagOfWords = new ArrayList<>();
        documents = new ArrayList<>();
        stopList = new StopList();
    }

    public WordVector(StopList stopList){
        bagOfWords = new ArrayList<>();
        documents = new ArrayList<>();
        this.stopList = stopList;
    }

    public void addDocument(String filename){
        BufferedReader bfr;
        String s = "a";
        String[] ss;

        //opening the document
        try{
            bfr = new BufferedReader(new FileReader(filename));
//            System.out.println("File \"" + filename + "\" opened successfully.");
        } catch (FileNotFoundException e) {
//            System.out.println("File \"" + filename + "\" not found.");
            return;
        }

        //inserting document in the list of documents
        documents.add(filename);

        //reading the document
        do{
            try{s = bfr.readLine();}catch(Exception e){};

            if (s != null){

                //spliting line read in array of words
                ss = s.split("[! .,():]");

                //iterating through each found word
                for(int i = 0; i < ss.length; i++){

                    //normalizes the word
                    ss[i] = StopList.normalize(ss[i]);

                    //if word isnt in the bag of words and isnt a stop word,
                    //inserts it in bag of words
                    if(ss[i] != null && ss[i].length() > 0){
                        if(!bagOfWords.contains(ss[i]) && !this.stopList.hasWord(ss[i]))
                            bagOfWords.add(ss[i]);
                    }
                }
            }

        }while(s != null);

        try{bfr.close();}catch(Exception e){}
    }

    private double cos(int[] vec1, int[] vec2, int size){
        double upsum = 0;
        double lowersum1 = 0;
        double lowersum2 = 0;
        for(int i = 0; i < size; i++){
            upsum += vec1[i]*vec2[i];
            lowersum1 += vec1[i]*vec1[i];
            lowersum2 += vec2[i]*vec2[i];
        }

        lowersum1 = Math.sqrt(lowersum1);
        lowersum2 = Math.sqrt(lowersum2);

        return upsum/(lowersum1*lowersum2);
    }

    //params doc1 and doc2 are the index of the documents in the "documents" arrayList.
    //more easily, its the order that the docs were added to an WordVector object
    public double checkSimilarity(int doc1, int doc2){
        BufferedReader bfr1;
        BufferedReader bfr2;
        int[] vec1 = new int[bagOfWords.size()];
        int[] vec2 = new int[bagOfWords.size()];

        String s = "a";
        String[] ss;

        //opening doc1
        try{
            bfr1 = new BufferedReader(new FileReader(documents.get(doc1)));
//            System.out.println("File \"" + documents.get(doc1) + "\" opened successfully.");
        } catch (FileNotFoundException e) {
//            System.out.println("File \"" + documents.get(doc1) + "\" not found.");
            return -1;
        }

        //opening doc2
        try{
            bfr2 = new BufferedReader(new FileReader(documents.get(doc2)));
//            System.out.println("File \"" + documents.get(doc2) + "\" opened successfully.");
        } catch (FileNotFoundException e) {
//            System.out.println("File \"" + documents.get(doc2) + "\" not found.");
            return -1;
        }

        //reading doc1
        do{
            try{s = bfr1.readLine();}catch(Exception e){};

            if (s != null){

                //spliting line read in array of words
                ss = s.split("[! .,():]");

                //iterating through each found word
                for(int i = 0; i < ss.length; i++){

                    //normalizes the word
                    ss[i] = StopList.normalize(ss[i]);

                    //if word is in bagOfWords[j], vec[j]++
                    //note: j isnt explicitly used in here
                    if(ss[i] != null && ss[i].length() > 0){
                        if(bagOfWords.contains(ss[i])) vec1[bagOfWords.indexOf(ss[i])]++;
                    }
                }
            }

        }while(s != null);

        //reading doc2
        do{
            try{s = bfr2.readLine();}catch(Exception e){};

            if (s != null){

                //spliting line read in array of words
                ss = s.split("[! .,():]");

                //iterating through each found word
                for(int i = 0; i < ss.length; i++){

                    //normalizes the word
                    ss[i] = StopList.normalize(ss[i]);

                    //if word is in bagOfWords[j], vec[j]++
                    //note: j isnt explicitly used in here
                    if(ss[i] != null && ss[i].length() > 0){
                        if(bagOfWords.contains(ss[i])) vec2[bagOfWords.indexOf(ss[i])]++;
                    }
                }
            }

        }while(s != null);

        return cos(vec1,vec2,bagOfWords.size());
    }


}
