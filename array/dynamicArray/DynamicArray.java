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


/*

Test class:

src/test/java/DynamicArrayTest.java

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

public class DynamicArrayTest {

    private DynamicArray buildArray(int... elements) {
        DynamicArray arr = new DynamicArray();
        for (int e : elements) {
            arr.add(e);
        }
        return arr;
    }

    @Test
    public void testAdd() {
        DynamicArray arr = buildArray(1, 2, 3, 4);
        assertEquals(arr.get(0), 1);
        assertEquals(arr.get(1), 2);
        assertEquals(arr.get(2), 3);
    
        try {
            arr.get(10);
            fail("Expected an IndexOutOfBoundsException to be thrown");
        } catch (IndexOutOfBoundsException e) {
            System.out.println("IndexOutOfBoundsException caught as expected");
        }
        System.out.println("testAdd passed!"); 
    }


    @Test
    public void testDelete(){
        DynamicArray arr = buildArray(1,2,3,4);
        arr.delete(0);
        assertEquals(arr.get(0), 2);
        
        try {
            arr.delete(3);
            fail("Expected an IndexOutOfBoundsException to be thrown");
        } catch (IndexOutOfBoundsException e) {
            System.out.println("IndexOutOfBoundsException caught as expected");
        }
        System.out.println("testDelete passed!"); 
    }

    @Test
    public void testGet(){
        DynamicArray arr = buildArray(1,2,3,4);
        assertEquals(arr.get(0), 1);
        assertEquals(arr.get(2), 3);
        
        try {
            arr.get(10);
            fail("Expected an IndexOutOfBoundsException to be thrown");
        } catch (IndexOutOfBoundsException e) {
            System.out.println("IndexOutOfBoundsException caught as expected");
        }
        System.out.println("testGet passed!");    
    }

    @Test
    public void testSet(){
        DynamicArray arr = buildArray(1,2,3,4);
        arr.set(0, 5);
        assertEquals(arr.get(0), 5);
        arr.set(3, 4);
        assertEquals(arr.get(3), 4);

        try {
            arr.set(10, 5);
            fail("Expected an IndexOutOfBoundsException to be thrown");
        } catch (IndexOutOfBoundsException e) {
            System.out.println("IndexOutOfBoundsException caught as expected");
        }
        System.out.println("testSet passed!");    
    }

    @Test
    public void testLen(){
        DynamicArray arr = buildArray(1,2,3,4);
        assertEquals(arr.len(), 4);

        DynamicArray arr_2 = buildArray(1);
        assertEquals(arr_2.len(), 1);
        System.out.println("testLen passed!");
    }

    @Test
    public void testResizeEnlarge(){
        int[] arr = {1,2,3,4,5,6};
        int n_items = 6;
        
        int[] resizedArray = DynamicArray.resize(arr, n_items);
        for (int i = 0; i < arr.length; i++) {
            assertEquals(arr[i], resizedArray[i]);
          }
        assertEquals(arr.length * 2, resizedArray.length);
        System.out.println("testResizeEnlarge passed!");    
    }

    @Test
    public void testResizeShrink(){
        int[] arr = {1,2,3,4,5,6};
        int n_items = 3;

        int[] resizedArray = DynamicArray.resize(arr, n_items);
        for (int i = 0; i < resizedArray.length; i++) {
            assertEquals(arr[i], resizedArray[i]);
          }
        assertEquals(arr.length / 2, resizedArray.length);
        System.out.println("testResizeShrink passed!"); 
    }

    @Test
    public void testNoOpResize_(){
        int[] arr = {1,2,3};
        int n_items = 2;

        int[] resizedArray = DynamicArray.resize(arr, n_items);
        assertEquals(arr, resizedArray);
        System.out.println("testNoOpResize passed!");
    }

    @Test
    public void testUsage(){

        System.out.println(" ");
        
        DynamicArray arr = new DynamicArray();

        arr.add(1);
        arr.add(2);
        arr.add(3);
        System.out.println(arr);

        arr.delete(2);
        arr.delete(1);
        arr.delete(0);
        System.out.println(arr);

        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        
        arr.add(5);
        arr.add(6);
        arr.add(7);
        System.out.println(arr.toString());
    
        arr.delete(0);
        arr.delete(5);
        arr.delete(4);
        arr.delete(3);
        System.out.println(arr);
        arr.delete(2);
        arr.delete(1);
        arr.delete(0);
        System.out.println(arr.toString());

        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        arr.add(5);
        arr.add(6);
        arr.add(7);
        arr.add(8);
        arr.add(9);
        arr.add(10);
        arr.add(11);
        arr.add(12);
        arr.add(13);
        System.out.println(arr.toString());

        arr.delete(12);
        arr.delete(11);
        arr.delete(10);
        arr.delete(9);
        arr.delete(8);
        arr.delete(7);
        arr.delete(6);
        arr.delete(5);
        arr.delete(4);
        arr.delete(3);
        arr.delete(2);
        arr.delete(1);
        arr.delete(0);

        System.out.println(arr.toString());
        System.out.println(" ");
        System.out.println("testUsage passed!");
    }

}
 */