import java.io.*;
import java.util.Arrays;
// defined my own deque since the ArrayDeque in Java does not support random access
class Deque{
    public int[] arr;
	public int front, back, capacity, size;
	public final int INITSIZE = 2;

    public Deque() {
		arr = new int[INITSIZE]; // create array of integers
		front = 0;
		back = 0;
		size = 0;
		capacity = INITSIZE;
	}

    public boolean empty() {return (size == 0);}

    public void addFirst(Integer item) { 
		if (size + 1 == capacity) // array is full
		  enlargeArr();
        front = (capacity + front - 1) % capacity;
		arr[front] = item;
		size += 1;
		
	}

    public void addLast(Integer item) {
		if (size + 1 == capacity) // array is full
		  enlargeArr();
		arr[back] = item;
		back = (back + 1) % capacity;
		size += 1;
	}

	public Integer removeFirst(){
        if (empty()) return null;
		Integer item = arr[front];
		front = (front + 1) % capacity; 
		size -= 1;
		return item;
    }

    public Integer removeLast(){
        if (empty()) return null;
		back = (capacity + back - 1)%capacity;
		Integer item = arr[back]; 
		size -= 1;
		return item;
    }

    public void enlargeArr() {
		int newSize = capacity * 2;
		int[] temp = new int[newSize];
		for (int j = 0; j < capacity; j++) {
			// copy the front (1st) element, 2nd element, ...,  in the 
			// original array to the 1st (index 0), 2nd (index 1), ...,
			// position in the enlarged array
			temp[j] = arr[(front+j) % capacity];
		}
		front = 0; 
		back = capacity - 1;
		arr = temp;
		capacity = newSize;
	}

    public int get(int index) {return arr[(front+index)%capacity];} 

	public int getSize() {return size;}

	public String toString() {return Arrays.toString(arr);} // for debugging purposes
}
// use two deques to simulate a teque; d1 = front deque, d2 = back deque
class tripleEndedQueue{
	private Deque d1,d2;

	public tripleEndedQueue(){
		d1 = new Deque();
		d2 = new Deque();
	}

	public void pushFront(int item) {
		d1.addFirst(item);
		// rebalance if d1 has a greater number of elements than d2 by at least 2
		if (d1.getSize() - d2.getSize() > 1) {d2.addFirst(d1.removeLast());}
	}

	public void pushMiddle(int item){
		if (d2.getSize() >= d1.getSize()) {d1.addLast(item);}
		else {d2.addFirst(item);}
	}

	public void pushBack(int item) {
		d2.addLast(item);
		// rebalance if d2 has a greater number of elements than d1 
		if (d2.getSize() > d1.getSize()) {d1.addLast(d2.removeFirst());}
	}
	
	public int get(int index){
        if (index >= d1.getSize()) {return d2.get(index%d1.getSize());}    
        else {return d1.get(index);}
	}
}

public class teque {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		int n = Integer.parseInt(br.readLine());
		tripleEndedQueue t1 = new tripleEndedQueue();
		for (int i = 0; i < n; i++){
			String[] line = br.readLine().split(" ");
			if (line[0].equals("push_front")) {t1.pushFront(Integer.parseInt(line[1]));}
			else if (line[0].equals("push_middle")) {t1.pushMiddle(Integer.parseInt(line[1]));}
			else if (line[0].equals("push_back")) {t1.pushBack(Integer.parseInt(line[1]));}
			// get command
			else {pw.println(t1.get(Integer.parseInt(line[1])));}
		}
        br.close();
        pw.close();
    }
}
