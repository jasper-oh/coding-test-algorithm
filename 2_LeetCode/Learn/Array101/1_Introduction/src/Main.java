public class Main {
    public static void main(String[] args) {
    /*  <MaxConsecutiveOnes>
    * Input: nums = [1,1,0,1,1,1]
    * Output: 3
    * The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
        1 <= nums.length <= 105
        nums[i] is either 0 or 1.
    */
    MaxConsecutiveOnes mco = new MaxConsecutiveOnes();
    int[] nums = {1,1,0,1,1,1};
    mco.findMaxConsecutiveOnes(nums);

    /* Input: nums = [555,901,482,1771]
       Output: 1
       Only 1771 contains an even number of digits.
       1 <= nums.length <= 500
       1 <= nums[i] <= 10^5
    */

    FindNumbersWithEvenNumberOfDigits fd = new FindNumbersWithEvenNumberOfDigits();
    int[] nums1 = {555,901,482,1771};
    fd.findNumbers(nums1);

    /* Input: nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Explanation: After squaring, the array becomes [16,1,0,9,100].
        After sorting, it becomes [0,1,9,16,100].
    */

    }
}

class MaxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int consecutive = 0;
        int count= 0;
        for(int i = 0;i < nums.length;++ i) {
            if(nums[i] == 1) {
                consecutive += 1;
            }
            else
            if(count <= consecutive) {
                count = consecutive;
                consecutive = 0;
            }
            else
                consecutive = 0;
        }
        if(count < consecutive) {
            count = consecutive;
        }
        return count;
    }
}

class FindNumbersWithEvenNumberOfDigits {
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

class SquaresOfSortedArray {

}