import java.io.*;
import java.util.*;

class Person{
    private String name;
    private ArrayList<String> classes; // given classes are reversed, since highest level of detail is on the right and lowest level on the left

    public Person(String name, ArrayList<String>classes){
        this.name = name;
        this.classes = classes;
    }

    public String getName() {return this.name;}

    public ArrayList<String> getClasses() {return this.classes;}
    // setter method to update classes with trailing middles, if any
    public void setClasses(int max_length) {
        int diff = max_length-this.classes.size();
        for (int i = 0; i < diff; i++) {
            this.classes.add("middle");
        }
    }
}
// comparator arranges in descending order by ranking of classes, and for similar class rankings, arrange by ascending order of lexicographical order of names
class hierarchyComparator implements Comparator<Person> {
	public int compare(Person p1, Person p2) {
        Hashtable<String,Integer> ranking = new Hashtable<>(); // ranking stores relative order of classes in terms of integers
        ranking.put("upper", 2); ranking.put("middle", 1); ranking.put("lower", 0);
        // compare classes starting from the one on the left first,since classes were reversed
        for (int i = 0; i < p1.getClasses().size(); i++){// all classes have same size due to appending of tailing "middle"
            int a = ranking.get(p2.getClasses().get(i)) - ranking.get(p1.getClasses().get(i));
            if (a != 0) {return a;}
        }
        // if all of the classes are the same, compare the lexicographical order of the name
        return p1.getName().compareTo(p2.getName());
    }

	public boolean equals(Object obj) {return this == obj;}
}

public class classy {
    public static void main(String[] args) throws IOException{
        hierarchyComparator hComp = new hierarchyComparator();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++){
            int n = Integer.parseInt(br.readLine()), max_length = 0;
            ArrayList<Person> persons = new ArrayList<>();
            for (int j = 0; j < n; j++){
                String[] line = br.readLine().split(" ");
                String name = line[0].substring(0, line[0].length()-1);
                // the classes given are reversed since the highest detail is on the right and lowest detail on left
                String[] temp = line[1].split("-");
                ArrayList<String> classes = new ArrayList<>();
                for (int k = temp.length-1; k >= 0; k--) {classes.add(temp[k]);}
                if (classes.size() > max_length) {max_length = classes.size();}
                persons.add(new Person(name,classes));
            }
            for (Person p: persons){p.setClasses(max_length);}
            Collections.sort(persons,hComp);
            for (Person p: persons){pw.println(p.getName());}
            pw.println("=".repeat(30));
        } 
        br.close();
        pw.close();
    }
}
