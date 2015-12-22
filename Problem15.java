
public class Problem15 {

/*	
	Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
	Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
	Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
	Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
	*/
	
	
	public static void main(String[] args){
		int spoons = 100;
		Ingredient sprinkles = new Ingredient(2, 0, -2,  0, 3);
		Ingredient butter    = new Ingredient(0, 5, -3,  0, 3);
		Ingredient chocolate = new Ingredient(0, 0,  5, -1, 8);
		Ingredient candy     = new Ingredient(0,-1,  0,  5, 8);
		
		long bestScore = -1;
		for(int i= 0; i <= spoons; i++){
			for(int j = 0; j <= spoons - i; j++){
				for(int k = 0; k <= spoons -i -j; k++ ){
					int m = spoons -i -j-k;
					int cap =  i*sprinkles.capacity + j*butter.capacity + k*chocolate.capacity + m*candy.capacity;
					if(cap <0){
						cap = 0;
					}
					
					int dur = i*sprinkles.durability + j*butter.durability+ k*chocolate.durability+ m*candy.durability;
					if(dur <0){
						dur = 0;
					}
					int flav = i*sprinkles.flavor + j*butter.flavor + k*chocolate.flavor+ m*candy.flavor;
					if(flav <0){
						flav = 0;
					}
					int text = i*sprinkles.texture + j*butter.texture+ k*chocolate.texture+ m*candy.texture;
					if(text <0){
						text = 0;
					}
					int cals = i*sprinkles.calories+ j*butter.calories + k*chocolate.calories+ m*candy.calories;
					
					
					if(cals != 500){
						continue;
					}
					
					long score =  cap*dur*flav*text;
					
					
					if(score> bestScore){
						bestScore= score;
					}
					
				}
			}
		}
		System.out.println(bestScore);
	}
	
}

