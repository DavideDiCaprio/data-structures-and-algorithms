// src/main/java/DynamicArray.java

public class DynamicArray {
    private int[] array;
    private int nItems;

    public DynamicArray() {
        this.array = new int[1];
        this.nItems = 0;
    }

    public void add(int x) {
        this.array = resize(this.array, this.nItems);
        this.array[nItems] = x;
        this.nItems ++;
    }

    public void delete(int i) {
        if (i < 0 || i >= nItems) {
            throw new IndexOutOfBoundsException("Invalid index");
        }

        for(int j = i; j < nItems - 1; j++){
            this.array[j] = this.array[j+1];
        }
        this.nItems--;
        this.array = resize(this.array, this.nItems);
    }

    public int len() {
        return this.nItems;    
    }

    public int get(int i) {
        if (i < 0 || i >= nItems) {
            throw new IndexOutOfBoundsException("Invalid index");
        }
        return this.array[i];
    }
    
    public void set(int i, int x) {
        if (i < 0 || i >= nItems) {
            throw new IndexOutOfBoundsException("Invalid index");
        }
        this.array[i] = x;
    }
    
    public static int[] resize(int[] arr, int nItems) {
        int[] resizedArray = arr;
        // null
        if(nItems > arr.length / 2 && nItems <= arr.length - 1) {
            return arr;
        } 
        // enlarge
        if(nItems == arr.length) {
            resizedArray = new int[arr.length * 2];
        }
        // shrink
        if (nItems <= arr.length / 2 && arr.length > 1) {
            resizedArray = new int[Math.floorDiv(arr.length, 2)];
        }
        
        for(int i = 0; i < nItems; i++) {
            resizedArray[i] = arr[i];
        } 
        return resizedArray;
    }


    @Override
    public String toString() {
        if (nItems == 0) {
            return "[]";
        }
        StringBuilder sb = new StringBuilder();
        sb.append("[");

        for (int i = 0; i < nItems; i++) {
            sb.append(array[i]);
            if (i < nItems - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
}
