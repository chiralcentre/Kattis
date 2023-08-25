import java.io.*;
import java.util.*;

class Quest{
    private int E,G,id;

    public Quest(int energy,int gold, int id){
        this.E = energy;
        this.G = gold;
        this.id = id; // index is added to allow for duplicate quests
    }

    public int getEnergy() {return this.E;}

    public int getGold() {return this.G;}

    public int getId() {return this.id;}
}

class questComparator implements Comparator<Quest> {
    // sort by energy in ascending order, and for songs with same energy sort by gold. If energy and gold are the same, pick quest with lower id
	public int compare(Quest s1, Quest s2) {
        int a = Integer.compare(s1.getEnergy(), s2.getEnergy()), b = Integer.compare(s1.getGold(), s2.getGold()), c = Integer.compare(s1.getId(), s2.getId());
        return (a != 0 ? a : (b != 0 ? b : c));
    }

	public boolean equals(Object obj) {return this == obj;}
}

public class kattissquest {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine());
        questComparator qComp = new questComparator();
        TreeSet<Quest> ts = new TreeSet<>(qComp);
        for (int i = 0; i < N; i++){
            String[] line = br.readLine().split(" ");
            if (line[0].equals("add")){
                int E = Integer.parseInt(line[1]), G = Integer.parseInt(line[2]);
                ts.add(new Quest(E, G, i));
            }
            else { //query command
                int X = Integer.parseInt(line[1]);
                long rewards = 0;
                //find quest with highest energy <= X, 100001 is chosen for gold value since 100000 is the max for G
                Quest q = ts.floor(new Quest(X,100001,1)); 
                while (q != null && X > 0){ // if treeset is not empty and q exists
                    X -= q.getEnergy();
                    rewards += q.getGold();
                    ts.remove(q);
                    q = ts.floor(new Quest(X,100001,1));
                }
                pw.println(rewards);
            }
        }
        br.close();
        pw.close();
    }
}
