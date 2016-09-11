// VX false
// VV false
// II true
// IIX false
// IX true
// IM false
// XM false
// CM true
boolean validroman(String s){
    char[] romans = {'M','D','C','L','X','V','I'};
	int[] values = {1000,500,100,50,10,5,1};
	int l = s.length();
	if(l== 0)
		return false;
	boolean can_reverse = true; // next char index can be smaller than current char index; 
	for(int i=0;i<l-1;i++){
		int current = findindex(s.charAt(i));
		int next = findindex(s.charAt(i+1));
		if(current < next)
			continue;
		else if(current == next){
			if(current %2 == 0)
				continue;
		}
		else if(current - next == 2){
			if(i>0 && s.charAt(i-1) != s.charAt(i));
				continue
		}
		return false;
	}
	return true;
}
int findindex(char[] romans,char c){
    for(int i=0;i<romans.length;i++){
        if(romans[i] == c)
            return i;
    }
    return -1;
}