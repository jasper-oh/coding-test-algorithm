/* Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
*/

public class SquaresOfSortedArray {
    public int[] sortedSquares(int[] nums) {

        int startIdx = 0;
        int endIdx = nums.length -1;
        int[] result = new int[nums.length];
        for (int idx=endIdx; idx>= 0; idx--){
            if(Math.abs(nums[startIdx]) > Math.abs(nums[endIdx])){
                result[idx] = nums[startIdx] * nums[startIdx];
                startIdx++;
            }else{
                result[idx] = nums[endIdx] * nums[endIdx];
                endIdx--;
            }
        }
        return result;
    }

}
