class Solution {
    public List<String> removeInvalidParentheses(String s) {
        /**
         * This solution should work for all cases when no other characters are involved.
         */
        return helper(s, false);
    }
    
     public List<String> helper(String s, boolean reverse) {
        List<String> result = new LinkedList<String>();
        String validParentheses = "";
        int left = 0, right = 0;
        char temp, open='(', close=')';
        if (reverse) {
            open = ')';
            close = '(';
        }
         
        List<Integer> cBP = new ArrayList<Integer>();
        
        for (int i=0; i<s.length();++i) {
            temp = s.charAt(i);
            if (reverse)
                validParentheses = temp + validParentheses;
            else
                validParentheses += temp;
            if (temp != close) {
                if (temp == open)
                    ++left;
            } else {
                ++right;
                cBP.add(i);
                if (right > left) {
                    Set<String> set = new HashSet<String>();
                    for (int j=0;j<cBP.size();++j) {
                        if (!reverse)
                            set.add(validParentheses.substring(0, cBP.get(j)) +
                                    validParentheses.substring(cBP.get(j)+1));
                        else
                            set.add(validParentheses.substring(0, i-cBP.get(j)) +
                                validParentheses.substring(i-cBP.get(j)+1));
                    }
                        
                    
                    List<String> validParaOfRemaining;
                    if (!reverse)
                        validParaOfRemaining = helper(s.substring(i+1), reverse);
                    else
                        validParaOfRemaining = helper(s.substring(i+1), reverse);
                        
                    Iterator<String> setIt = set.iterator(), remainingIt;
                    while (setIt.hasNext()) {
                        String a = setIt.next();
                        remainingIt = validParaOfRemaining.iterator();
                        while (remainingIt.hasNext())
                            result.add(a + remainingIt.next());
                    }
                    break;
                }
            }
        }
        
        if (result.size() == 0) {
            if (left == right)
                return new ArrayList<String>(Arrays.asList(validParentheses));
            byte [] strAsByteArray = s.getBytes(); 
            byte [] reverseByteArray = new byte [strAsByteArray.length]; 
  
            for (int i = 0; i<strAsByteArray.length; i++) 
                reverseByteArray[i] =  strAsByteArray[strAsByteArray.length-i-1];
            return helper(new String(reverseByteArray), !reverse);
        }
        
        return result;
    }
}