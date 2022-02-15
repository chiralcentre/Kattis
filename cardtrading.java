import java.util.*;

class Card {
	public long type,buy,sell;
    public long[] d;

	public Card(long type,long buy,long sell,long[] d) {
		this.type = type;
		this.buy = buy;
        this.sell = sell;
        this.d = d;
	}

	public long getCardType() {return type;}

	public long getBuyPrice() {return buy;}

    public long getSellPrice() {return sell;}
    // For each card type, the "net cost" of making a combo is the cost for buying missing cards plus the loss of profit for not selling cards of that type.
    public long getNetCost() {return Math.max(2-d[(int)type],0)*buy + d[(int)type]*sell;}

	public String toString() {return type + " - " + buy + "-" + sell;}
}

class netCostComparator implements Comparator<Card> {

	public int compare(Card c1, Card c2) {return Long.compare(c1.getNetCost(), c2.getNetCost());}

	public boolean equals(Object obj) {return this == obj;}
}

public class cardtrading {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        netCostComparator netCostComp = new netCostComparator();
        String[] firstLine = s.nextLine().split(" "), secondLine = s.nextLine().split(" ");
        int T = Integer.parseInt(firstLine[1]), K = Integer.parseInt(firstLine[2]); // value of N not needed
        long[] deck = new long[T]; // deck keeps track of number of each card type, and card type is stored in the index
        for (String type: secondLine){deck[Integer.parseInt(type)-1] += 1;} // zero indexing, offset by one
        List<Card> prices = new ArrayList<>();
        for (long i = 0; i < T; i++){
            long B = s.nextLong(), S = s.nextLong();
            prices.add(new Card(i,B,S,deck));
        }
        // sort by net cost
        Collections.sort(prices,netCostComp);
        // optimal combination should have lowest net cost
        // sell T-K card types with higher net cost, and buy K card types with lower net cost, since we must have at least K combos
        long profit = 0;
        for (int j = 0; j < T - K; j++){
            Card c = prices.remove(prices.size()-1);
            profit += c.getSellPrice()*deck[(int)c.getCardType()];
        }
        for (int j = 0; j < K; j++){
            Card c = prices.remove(prices.size()-1);
            if (deck[(int)c.getCardType()] <= 2){
                // buying to make up the combo
                profit -= c.getBuyPrice()*(2 - deck[(int)c.getCardType()]);
            }
            else {
                // sell off any excess
                profit += c.getSellPrice()*(deck[(int)c.getCardType()] - 2);
            }
        }
        System.out.println(profit);
        s.close();
    }
}
