import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.TreeMap;

/**
 * Datastructure to represent an WordNet
 * vectors with synsets indexes are the elements
 * words are keys
 * a multimap-like structure maps each word to a array of indexes relatives
 *      to the positions of that word in the wordnet
 */
public class WordNet {

    private TreeMap<String, ArrayList<Integer>> map;
    private String filename;

    public WordNet(String filename){
        String s = null;
        String[] ss;
        BufferedReader bfr;
        this.filename = filename;
        //opening the document
        try{
            bfr = new BufferedReader(new FileReader(filename));
            //System.out.println("File \"" + filename + "\" opened successfully.");
        } catch (FileNotFoundException e) {
            //System.out.println("File \"" + filename + "\" not found.");
            return;
        }

        this.map = new TreeMap<>();

        // useful regex:
        // [. \[\]<>,{}] to split words
        // [0-9] //checks if string is number
        // ss[0] = synset number
        // ss[3] = junk
        // other junk: last one (if number) and empty ones.

        //loop through each line of the file
        do{
            try{s = bfr.readLine();}catch(Exception e){;}
            if(s != null){
                //parse each line
                ss = s.split("[. \\[\\]<>,{}]");

                //saves synset no
                int synsetNo = Integer.parseInt(ss[0]);

                //traverse through found words
                for(int i = 6; i < ss.length; i++){
                    //if it is a valid word
                    if(ss[i].length() > 0 && !MyNormalizer.isNumeric(ss[i])){
                        //check if each word found is already in the map
                        if(map.containsKey(ss[i])){
                            //if it is, inserts the corresponding synset into the word synsets array
                            map.get(ss[i]).add(synsetNo);
                        } else {
                            //if not, create nodes for each word
                            map.put(ss[i],new ArrayList<Integer>(synsetNo));
                        }
                    }
                }
            }
        } while(s != null);
    }
}
