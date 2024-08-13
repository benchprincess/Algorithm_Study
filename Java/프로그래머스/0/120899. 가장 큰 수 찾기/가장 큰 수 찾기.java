class Solution {
    public int[] solution(int[] array) {
        int maxNumber = array[0];
        int index = 0;
        
        for (int i = 1; i < array.length; i++) {
            if (array[i] > maxNumber) {
                maxNumber = array[i];
                index = i;
            }
        }
        return new int[]{maxNumber, index};     
    }
}