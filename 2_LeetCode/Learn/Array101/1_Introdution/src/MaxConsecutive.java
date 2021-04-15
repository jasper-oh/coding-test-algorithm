/*  <MaxConsecutiveOnes>
    * Input: nums = [1,1,0,1,1,1]
    * Output: 3
    * The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
        1 <= nums.length <= 105
        nums[i] is either 0 or 1.
*/
public class MaxConsecutive {
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
