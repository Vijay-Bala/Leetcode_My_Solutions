class Solution {
    public int finalValueAfterOperations(String[] a) {
        int c=0;
        for(String x:a){
            if (x.contains("--")) c--;
            else c++;
        }
        return c;
    }
}