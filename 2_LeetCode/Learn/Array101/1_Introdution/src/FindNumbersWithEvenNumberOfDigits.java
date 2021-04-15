public class FindNumbersWithEvenNumberOfDigits {
    public int findNumbers(int[] nums1) {
        int count = 0;
        int evenNumber = 0;
        for(int i = 0;i < nums1.length;++ i) {
            int number = nums1[i];
            count = 0;
            while(number > 0) {
                number = number / 10;
                ++ count;
            }
            if(count % 2 == 0) {
                evenNumber += 1;
            }
        }
        return evenNumber;
    }
}
