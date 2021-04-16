public class Main {
    public static void main(String[] args) {

        int[] nums = {0,0,1,1,1,2,2,3,3,4};
        RemoveDuplicates rd = new RemoveDuplicates();
        int answer = rd.removeDuplicates(nums);
        System.out.println(answer);

    }
}
