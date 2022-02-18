import java.util.*;

// Hand class has player number attribute and hand state attribute
class Hand{
    private int player;
    private String handState;

    public Hand(int player, String handState){
        this.player = player;
        this.handState = handState;
    }

    public int getPlayer() {return this.player;}

    public String getHandState() {return this.handState;}

    public void updateHandState(String state) {this.handState = state;}
}

public class coconut {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int s = input.nextInt(), n = input.nextInt(), start = 0; // start is the starting index
        // Create an arraylist of n Hands; Hands have a starting handState of "FOLDED"
        ArrayList<Hand> players = new ArrayList<>();
        for (int i = 1; i <= n; i++) {players.add(new Hand(i,"FOLDED"));} 
        // Iterate through the Hands according to game rules until one Hand is left.
        while (players.size() > 1){
            start = (start + s - 1)%players.size(); // -1 due to zero indexing
            int player = players.get(start).getPlayer();
            String handState = players.get(start).getHandState();
            if (handState.equals("FOLDED")){ //replace with two copies of fist
                players.get(start).updateHandState("FIST");
                players.add(start, new Hand(player,"FIST"));
            }
            else if (handState.equals("FIST")){// replace with palm, and increment start index by 1
                players.get(start).updateHandState("PALM");
                start = (start + 1)%players.size();
            }
            else if (handState.equals("PALM")){players.remove(start);} // remove hand 
        }
        System.out.println(players.get(0).getPlayer()); // only one hand left 
        input.close();
    }
}
