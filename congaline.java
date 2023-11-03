import java.io.*;
import java.util.*;

public class congaline {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        String[] firstLine = br.readLine().split(" ");

        int N = Integer.parseInt(firstLine[0]);
        int Q = Integer.parseInt(firstLine[1]);
        DoublyLinkedList DLL = new DoublyLinkedList();
        int[] pairings = new int[N << 1];
        HashMap<Integer, Node> mappings = new HashMap<>();
        String[] indexToName = new String[N << 1];
        Node curr = null;
        for (int i = 0; i < N; ++i) {
            String[] line = br.readLine().split(" ");
            String first = line[0], second = line[1];
            int firstIndex = (i << 1), secondIndex = (i << 1) + 1;
            indexToName[firstIndex] = first; indexToName[secondIndex] = second;
            Node node1 = new Node(firstIndex), node2 = new Node(secondIndex);
            if (curr == null) {
                curr = node1;
                DLL.pushFront(curr);
            } else {
                DLL.insertAfter(curr, node1);
                curr = curr.next;
            }
            DLL.insertAfter(curr, node2);
            curr = curr.next;
            pairings[firstIndex] = secondIndex;
            pairings[secondIndex] = firstIndex;
            mappings.put(firstIndex, node1);
            mappings.put(secondIndex, node2);
        }
        curr = DLL.head;
        String command = br.readLine().strip();
        for (int j = 0; j < Q; ++j) {
            char ins = command.charAt(j);
            if (ins == 'F') {
                curr = curr.back;
            } else if (ins == 'B') {
                curr = curr.next;
            } else if (ins == 'R') {
                Node moved = curr;
                if (curr.next != null) {
                    curr = curr.next;
                } else {
                    curr = DLL.head;
                }
                DLL.remove(moved);
                DLL.insertAfter(DLL.tail, moved);
            } else if (ins == 'C') {
                Node moved = curr;
                int person = moved.value;
                if (curr.next != null) {
                    curr = curr.next;
                } else {
                    curr = DLL.head;
                }
                DLL.remove(moved);
                DLL.insertAfter(mappings.get(pairings[person]), moved);

            } else if (ins == 'P') pw.println(indexToName[pairings[curr.value]]);
        }
        pw.println();
        DLL.listprint(pw, indexToName);
        pw.close();
    }
}

class Node { 
    int value;
    Node next;
    Node back;
  
    public Node(int value) {
        this.value = value;
        this.next = null;
        this.back = null;
    }
}
  
class DoublyLinkedList { 
    public Node head; 
    public Node tail; 

    public DoublyLinkedList() {
        this.head = null;
        this.tail = null;
    }

    // Insert new node on the front of the list
    public void pushFront(Node new_node) { 
        new_node.next = this.head;
        if (this.head !=  null) {
            this.head.back = new_node;
        } else {
            this.tail = new_node;
        }
        this.head = new_node; // Move head to point to new node
    } 

    // Insert node after given node
    public void insertAfter(Node prev_node, Node new_node) { 
        if (prev_node == null) {
            System.out.print("Previous node cannot be null!");
            return;
        }

        boolean insertTail = prev_node == this.tail ? true : false;

        new_node.next = prev_node.next;
        prev_node.next = new_node;
        new_node.back = prev_node;

        if (new_node.next != null) {
            new_node.next.back = new_node;
        }

        if (insertTail) {
            this.tail = new_node;
        }
    } 

    // Remove node
    public void remove(Node node) {
        if (this.head == null || node == null) return;

        // Case 1: node to be removed is head
        if (this.head == node) {
            this.head = node.next;
        } 

        // Case 2: node to be removed is tail
        if (this.tail == node) {
            this.tail = node.back;
        }

        // Change prev reference for next node
        if (node.next != null) {
            node.next.back = node.back;
        }

        // Change next reference for previous node
        if (node.back != null) {
            node.back.next = node.next;
        }

        // Garbage collection
        node.back = null;
        node.next = null;
    }

    // Print contents of the linked list, starting from head
    public void listprint(PrintWriter pw, String[] indexToName) {
        Node temp = this.head;
        while (temp != null) {
            pw.print(indexToName[temp.value]);
            pw.println();
            temp = temp.next;
        }
    }

}

