/*
 *     Projeto sem nome
 *     Copyright (C) 2016 Rafael Augusto Monteiro
 *
 *     This program is free software: you can redistribute it and/or modify
 *     it under the terms of the GNU General Public License as published by
 *     the Free Software Foundation, either version 3 of the License, or
 *     (at your option) any later version.
 *
 *     This program is distributed in the hope that it will be useful,
 *     but WITHOUT ANY WARRANTY; without even the implied warranty of
 *     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *     GNU General Public License for more details.
 *
 *     You should have received a copy of the GNU General Public License
 *     along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

import java.util.Scanner;

/**
 *  Main program class
 */
public class Principal {
    public static void main(String[] args){
//        Scanner in = new Scanner(System.in);
//        String s;
//
//        System.out.println("Insert stoplist filename:");
//        s = in.nextLine();
        StopList sl = new StopList("stoplist_portugues.txt");
        StopList sls = new StopList("stoplist_portugues.txt2");

        //creates an wordVector class, passing a stopList as argument
        WordVector wv = new WordVector(sl);

        //adds two documents to the wordVector
        wv.addDocument("doc1.txt");
        wv.addDocument("doc2.txt");

        //calculates their similarity based on vector cos
        System.out.println("Using a stopList:");
        System.out.printf("Documents similarity is %.0f percent\n",wv.checkSimilarity(0,1)*100);

        WordVector wv2 = new WordVector();

        //adds two documents to the wordVector
        wv2.addDocument("doc1.txt");
        wv2.addDocument("doc2.txt");

        //calculates their similarity based on vector cos
        System.out.println("Not using a stopList:");
        System.out.printf("Documents similarity is %.0f percent\n",wv2.checkSimilarity(0,1)*100);
    }
}
