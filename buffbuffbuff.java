import java.io.*;
import java.util.*;

public class buffbuffbuff {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int Q = Integer.parseInt(br.readLine());
        long global_offset = 0;
        HashMap<Integer,Long> card_type_offset = new HashMap<>();
        HashMap<Integer,PriorityQueue<Long>> cards = new HashMap<>();
        TreeMap<Long,Long> best_offset_cards_from_types = new TreeMap<>();
        for (int i = 0; i < Q; i++) {
            String[] line = br.readLine().split(" ");
            switch (line[0]) {
                case "ADD" -> {
                    int T = Integer.parseInt(line[1]);
                    long P = Long.parseLong(line[2]);
                    long card_offset = card_type_offset.getOrDefault(T, 0L);
                    // put new card into PQ in cards hashmap
                    PriorityQueue<Long> ct = cards.getOrDefault(T, new PriorityQueue<>(Collections.reverseOrder()));
                    long offset_P = P - global_offset - card_offset;
                    Long old_best = ct.peek();
                    ct.offer(offset_P);
                    cards.put(T, ct);
                    // update best_offset_cards_from_types with best card  
                    if (old_best != null && offset_P > old_best) {
                        old_best += card_offset;
                        long f1 = best_offset_cards_from_types.getOrDefault(old_best, 0L);
                        if (f1 == 1) best_offset_cards_from_types.remove(old_best);
                        else best_offset_cards_from_types.put(old_best, f1 - 1);
                        long best_card = offset_P + card_offset;
                        best_offset_cards_from_types.merge(best_card, 1L, (a, b) -> a + b);
                    } else if (old_best == null) {
                        long best_card = offset_P + card_offset;
                        best_offset_cards_from_types.merge(best_card, 1L, (a, b) -> a + b);
                    }
                }
                case "BUFF_ALL" -> global_offset += Long.parseLong(line[1]);
                case "BUFF" -> {
                    long offset = Long.parseLong(line[2]);
                    int T = Integer.parseInt(line[1]);
                    if (cards.containsKey(T)) {
                        // get old type offset
                        long old_offset = card_type_offset.getOrDefault(T, 0L);
                        card_type_offset.put(T, old_offset + offset);
                        // remove old card
                        long og_best = cards.get(T).peek() + old_offset;
                        long og_freq = best_offset_cards_from_types.getOrDefault(og_best, 0L);
                        if (og_freq == 1) best_offset_cards_from_types.remove(og_best);
                        else best_offset_cards_from_types.put(og_best, og_freq - 1);
                        // insert new card
                        long new_power = og_best + offset;
                        best_offset_cards_from_types.merge(new_power, 1L, (a, b) -> a + b);
                    }
                }
                case "MAX" -> {
                    long best = best_offset_cards_from_types.lastEntry().getKey();
                    pw.println(best + global_offset);
                }
            }
            /*
            if (!line[0].equals("MAX"))  {
                pw.println("******************************************************************");
                pw.printf("OPERATION = %s\n", String.join(" ", line));
                pw.printf("global_offset = %d\n", global_offset);
                pw.printf("card_type_offset = %s\n", card_type_offset);
                pw.printf("cards = %s\n", cards);
                pw.printf("best_offset_cards_from_types = %s\n", best_offset_cards_from_types);
                pw.println("******************************************************************");
            } */
        }
        br.close();
        pw.close();
    }
}