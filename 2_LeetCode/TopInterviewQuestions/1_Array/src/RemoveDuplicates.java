/*
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
*/


public class RemoveDuplicates {

    int removeDuplicates(int[] nums) {
        if (nums.length < 1) {
            return nums.length;
        }
        int previousValue = Integer.MIN_VALUE;
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != previousValue) {
                nums[k] = nums[i];
                k++;
            }
            previousValue = nums[i];
        }
        return k;
    }
}