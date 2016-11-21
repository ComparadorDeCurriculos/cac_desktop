import java.io.*;
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

    public WordNet(String filename) throws Exception{
        String s = null;
        String[] ss;
        BufferedReader bfr;
        this.filename = filename;
        //opening the document
        try{
            bfr = new BufferedReader(new InputStreamReader(new FileInputStream(filename), "ISO-8859-1"));
            //System.out.println("File \"" + filename + "\" opened successfully.");
        } catch (FileNotFoundException e) {
            System.out.println("File \"" + filename + "\" not found.");
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
                    if(ss[i].length() > 0 && !ModeloVetorialUtils.isNumeric(ss[i])){
                        //ss[i] = ModeloVetorialUtils.normalize(ss[i]);
                        //check if each word found is already in the map
                        if(map.containsKey(ss[i])){
                            //if it is, inserts the corresponding synset into the word synsets array
                            map.get(ss[i]).add(synsetNo);
                        } else {
                            //if not, create nodes for each word
                            ArrayList<Integer> l = new ArrayList<Integer>();
                            l.add(synsetNo);
                            map.put(ss[i],l);

                        }
                    }
                }
            }
        } while(s != null);

//        System.out.println(map.size());

//        ModeloVetorialUtils.printMap(map);


        bfr.close();
    }

    /**
     *
     * @param key Search key
     * @return A Arraylist containing all synsets id's, or null if not found
     */
    public ArrayList<Integer> getSynsets(String key){
        String temp = ModeloVetorialUtils.normalize(key);
        if(this.map.containsKey(temp)){
            return this.map.get(temp);
        } else {
            return null;
        }
    }
}


