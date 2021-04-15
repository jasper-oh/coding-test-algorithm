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
