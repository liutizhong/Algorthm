package yougou.chapter1;

/**
 * Created by liutizhong on 2015/12/10.
 * 实现插入排序
 */
public class InsertionSort {
    static int[] arr = {1, 9, 10, 4, 7, 5, 8};

    public static void main(String[] args) {
        int temp = 0;
        for (int i = 1; i < arr.length; i++) {
            temp = arr[i];
            for (int j = 0; j <= i; j++) {
                if (arr[i] < arr[j]) {
                    for (int k = i; k > j; k--) {
                        arr[k] = arr[k - 1];
                    }
                    arr[j] = temp;
                }
            }
        }
        for (int m = 0; m < arr.length; m++) {
            System.out.print("\t" + arr[m]);
        }
    }
}
