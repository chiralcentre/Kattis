import java.util.*;

class Sprinter {
	public String name;
	public double t1,t2; // t1 represents first leg timing, t2 represents other leg timings

	public Sprinter(String name,double t1,double t2) {
		this.name = name;
		this.t1 = t1;
        this.t2 = t2;
	}

	public String getName() {return name;}

	public double getT1() {return t1;}

    public double getT2() {return t2;}

	public String toString() {return name + " - " + t1 + "-" + t2;}
}

class t2Comparator implements Comparator<Sprinter> {

	public int compare(Sprinter p1, Sprinter p2) {
		// Returns the difference:
		// if positive, T2 of p1 is greater than p2
		// if zero, the ages are equal
		// if negative, T2 of p1 is less than p2
		return Double.compare(p1.getT2(), p2.getT2());
	}

	public boolean equals(Object obj) {return this == obj;}
}

public class bestrelayteam{
    public static void main(String[] args){
		t2Comparator t2Comp = new t2Comparator();
        Scanner s = new Scanner(System.in);
        int n = Integer.parseInt(s.nextLine());
		List<Sprinter> runners = new ArrayList<>();
		for (int i = 0; i < n; i++){
			String[] line = s.nextLine().split(" ");
			Sprinter person = new Sprinter(line[0],Double.parseDouble(line[1]),Double.parseDouble(line[2]));
			runners.add(person);
		}
		double bestTime = 99999999; //arbitrary large number
		List<String> bestTeam = new ArrayList<>();
		// sort by fastest flying start timing first
		Collections.sort(runners, t2Comp);
		// try every runner on first leg and fill up the team with the fastest three remaining flying start timings
		for (int i = 0; i < n; i++){
			double counter = runners.get(i).getT1();
			List<String> team = new ArrayList<>();
			team.add(runners.get(i).getName());
			if (i <= 2){ // choosing from top three in flying start rankings
				for (int j = 0; j < 4; j++){
					if (i != j){
						counter += runners.get(j).getT2();
						team.add(runners.get(j).getName());
					}
				}
			}
			else {
				for (int j = 0; j < 3; j++){
					counter += runners.get(j).getT2();
					team.add(runners.get(j).getName());
				}
			}
			if (counter < bestTime){bestTime = counter; bestTeam = team;}
		}
		System.out.println(bestTime);
		for (String name: bestTeam){System.out.println(name);}
        s.close();
    }
}