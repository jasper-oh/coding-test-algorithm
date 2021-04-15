public class Main {
    public static void main(String[] args) {

        MaxConsecutive mco = new MaxConsecutive();
        int[] nums = {1,1,0,1,1,1};
        int answer = mco.findMaxConsecutiveOnes(nums);
        System.out.println(answer);


        FindNumbersWithEvenNumberOfDigits fd = new FindNumbersWithEvenNumberOfDigits();
        int[] nums1 = {555,901,482,1771};
        int answer1 = fd.findNumbers(nums1);
        System.out.println(answer1);

    }
}





