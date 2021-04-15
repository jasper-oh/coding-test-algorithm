public class Main {
    public static void main(String[] args) {
    /*  <MaxConsecutiveOnes>
    * Input: nums = [1,1,0,1,1,1]
    * Output: 3
    * The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
        1 <= nums.length <= 105
        nums[i] is either 0 or 1.
    */
        MaxConsecutive mco = new MaxConsecutive();
        int[] nums = {1,1,0,1,1,1};
        int answer = mco.findMaxConsecutiveOnes(nums);
        System.out.println(answer);

    /* Input: nums = [555,901,482,1771]
       Output: 1
       Only 1771 contains an even number of digits.
       1 <= nums.length <= 500
       1 <= nums[i] <= 10^5
    */

    FindNumbersWithEvenNumberOfDigits fd = new FindNumbersWithEvenNumberOfDigits();
    int[] nums1 = {555,901,482,1771};
    int answer1 = fd.findNumbers(nums1);
    System.out.println(answer1);

    /* Input: nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Explanation: After squaring, the array becomes [16,1,0,9,100].
        After sorting, it becomes [0,1,9,16,100].
    */

    }
}





