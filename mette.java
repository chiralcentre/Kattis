import java.io.*;

class AVLVertex {
    // all these attributes remain public to slightly simplify the code
    public AVLVertex parent, left, right;
    public int height,size,key,level;
    AVLVertex(int v) {key = v; parent = left = right = null; height = 0; size = 1; level = 0;}
}
    
// adapted from lecture slides
class IntegerAVL {
    public AVLVertex root;

    public IntegerAVL() {root = null;}
    // helper method to check if x is a valid vertex and to return number of nodes in subtree
    public int size(AVLVertex T) {
        if (T == null) return 0;
        return T.size;
    }
    // helper method to check if x is a valid vertex and to return height of subtree
    // The height of an empty tree is -1 and the height of a tree with just one node is 0.
    public int height(AVLVertex T) {
        if (T== null) return -1;
        return T.height;
    }
    // public method called to search for a value v. 
    // Return v if it is found in the BST otherwise return -1
    public int search(int v) {
        AVLVertex res = search(root, v);
        return res == null ? -1 : res.key;
    }

    // helper method to perform search
    public AVLVertex search(AVLVertex T, int v) {
        if (T == null) return null;                     // not found
        else if (T.key == v) return T;                        // found
        else if (T.key < v)  return search(T.right, v);       // search to the right
        else return search(T.left, v);        // search to the left
    }
    
    // public method called to find Minimum key value in BST
    public int findMin() {return findMin(root);}

    // helper method to perform findMin
    // Question: What happens if BST is empty?
    public int findMin(AVLVertex T) {
        if (T.left == null) return T.key;                    // this is the min
        else return findMin(T.left);           // go to the left
    }

    // public method called to find Maximum key value in BST
    public int findMax() {return findMax(root);}

    // helper method to perform findMax
    public int findMax(AVLVertex T) {
        if (T.right == null) return T.key;                   // this is the max
        else return findMax(T.right);        // go to the right
    }

    // public method to find successor to given value v in BST.
    public int successor(int v) { 
        AVLVertex vPos = search(root, v);
        return vPos == null ? null : successor(vPos);
    }

    // helper recursive method to find successor to for a given vertex T in BST
    public int successor(AVLVertex T) {
        if (T.right != null)                 // this subtree has right subtree
            return findMin(T.right);  // the successor is the minimum of right subtree
        else {
            AVLVertex par = T.parent;
            AVLVertex cur = T;
            // if par(ent) is not root and cur(rent) is its right children
            while ((par != null) && (cur == par.right)) {
                cur = par;                                         // continue moving up
                par = cur.parent;
            }
            return par == null ? null : par.key;           // this is the successor of T
        }
    }

    // public method to find predecessor to given value v in BST
    public int predecessor(int v) { 
        AVLVertex vPos = search(root, v);
        return vPos == null ? null : predecessor(vPos);
    }

    // helper recursive method to find predecessor to for a given vertex T in BST
    public int predecessor(AVLVertex T) {
        if (T.left != null)                         // this subtree has left subtree
        return findMax(T.left);  // the predecessor is the maximum of left subtree
        else {
            AVLVertex par = T.parent;
            AVLVertex cur = T;
            // if par(ent) is not root and cur(rent) is its left children
            while ((par != null) && (cur == par.left)) { 
                cur = par;                                         // continue moving up
                par = cur.parent;
            }
            return par == null ? null : par.key;           // this is the successor of T
        }
    }

    // public method called to perform inorder traversal
    public void inorder() { 
        inorder(root);
        System.out.println();
    }

    // helper method to perform inorder traversal
    public void inorder(AVLVertex T) {
        if (T == null) return;
        inorder(T.left);                               // recursively go to the left
        System.out.printf(" %s", T.key);                      // visit this BST node
        inorder(T.right);                             // recursively go to the right
    }
    // helper method to find balance factor
    public int balanceFactor(AVLVertex T) {
        return height(T.left) - height(T.right);
    }
    // Helper method which rotates the given subtree to the right
    // return the root of right rotated subtree
    public AVLVertex rotateRight(AVLVertex T) { 
        AVLVertex w = T.left;
        w.parent = T.parent;
        T.parent = w;
        T.left = w.right;
        if (w.right != null) w.right.parent = T;
        w.right = T;
        w.size = T.size;
        T.size = 1 + size(T.left) + size(T.right);
        T.height = 1 + Math.max(height(T.left), height(T.right));
        w.height = 1 + Math.max(height(w.left), height(w.right));
        return w;
    }

    // Helper method which rotates the given subtree to the left
    // return the root of left rotated subtree
    public AVLVertex rotateLeft(AVLVertex T) {
        AVLVertex w = T.right;
        w.parent = T.parent;
        T.parent = w;
        T.right = w.left;
        if (w.left != null) w.left.parent = T;
        w.left = T;
        w.size = T.size;
        T.size = 1 + size(T.left) + size(T.right);
        T.height = 1 + Math.max(height(T.left), height(T.right));
        w.height = 1 + Math.max(height(w.left), height(w.right));
        return w;
    }
    // balance method
    public AVLVertex balance(AVLVertex T) {
        if (balanceFactor(T) < -1) {
            if (balanceFactor(T.right) > 0) {
                T.right = rotateRight(T.right);
            }
            T = rotateLeft(T);
        }
        else if (balanceFactor(T) > 1) {
            if (balanceFactor(T.left) < 0) {
                T.left = rotateLeft(T.left);
            }
            T = rotateRight(T);
        }
        return T;
    }
    // public method called to insert a new key with value v into BST
    public AVLVertex insert(int v) {root = insert(root, v); return root;}

    // helper recursive method to perform insertion of new vertex into BST
    public AVLVertex insert(AVLVertex T, int v) {
        if (T == null) return new AVLVertex(v);          // insertion point is found
        if (T.key < v) {                             // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        }
        else {                                                 // search to the left
            T.left = insert(T.left, v);
            T.left.parent = T;
        }
        T.size = 1 + size(T.left) + size(T.right);
        T.height = Math.max(height(T.left), height(T.right)) + 1; //update height
        return balance(T);                                          // return the updated BST
    }  

    // public method to delete a vertex containing key with value v from BST
    public void delete(int v) {root = delete(root, v);}

    // helper recursive method to perform deletion 
    public AVLVertex delete(AVLVertex T, int v) {
        if (T == null)  return T;              // cannot find the item to be deleted

        if (T.key < v)                                   // search to the right
            T.right = delete(T.right, v);
        else if (T.key > v)                               // search to the left
            T.left = delete(T.left, v);
        else {                                            // this is the node to be deleted
            if (T.left == null && T.right == null)                   // this is a leaf
                T = null;                                      // simply erase this node
            else if (T.left == null && T.right != null) {   // only one child at right        
                T.right.parent = T.parent;
                T = T.right;                                                 // bypass T        
            }
            else if (T.left != null && T.right == null) {    // only one child at left        
                T.left.parent = T.parent;
                T = T.left;                                                  // bypass T        
            }
            else {                                 // has two children, find successor
                int successorV = successor(v);
                T.key = successorV;         // replace this key with the successor's key
                T.right = delete(T.right, successorV);      // delete the old successorV
            }
        }
        if (T != null){
            T.size = 1 + size(T.left) + size(T.right);
            T.height = 1 + Math.max(height(T.left), height(T.right));
            return balance(T);
        }
        else return T;
    } 
    // public method to find rank of an integer
    public int rank(int v) {
        if (search(v) != -1)
            return rank(root,v);
        else {
            insert(v);
            int a = rank(root,v);
            delete(v);
            return a;
        }
    }

    // helper method 
    public int rank(AVLVertex T, int v) {
        if (T == null) return 0;
        if (T.key > v) return rank(T.left, v);
        else if (T.key < v) return 1 + size(T.left) + rank(T.right,v);
        else return size(T.left) + 1;
    }

    // public method to select node with rank k
    public int select(int r){
        AVLVertex x = select(root,r);
        return x.key;
    }

    // helper method
    public AVLVertex select(AVLVertex T, int r)  {
        int s = size(T.left);
        if (s + 1 == r) return T;
        else if (s + 1 > r) return select(T.left, r);
        else return select(T.right, r - s - 1);
    }                                    
}

public class mette {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int N = Integer.parseInt(br.readLine()); String[] A = br.readLine().split(" ");
        IntegerAVL tree = new IntegerAVL();
        for (int i = 0; i < A.length; i++) tree.insert(Integer.parseInt(A[i]));
        pw.println(tree.select(2));
        for (int j = 0; j < (N - 1) / 2 - 1; j++){
            String[] B = br.readLine().split(" ");
            tree.insert(Integer.parseInt(B[0]));
            tree.insert(Integer.parseInt(B[1]));
            pw.println(tree.select((tree.size(tree.root) + 1) / 2));
        }
        br.close();
        pw.close();
    }
}
