class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {

        int size = flowerbed.size();
        int tmp = n;

        if((n == 1 && flowerbed[0] == 0 && size == 1) || n == 0) return 1;
        
        for(int i = 0;i<size;i++){
            if(i == 0){
                if(flowerbed[i] == 0 && flowerbed[i+1] == 0){ // Viable plot
                    tmp--;
                    if(tmp == 0) return 1;
                    flowerbed[i] = 1;
                }
            }
            else if(i == size - 1){
                if(flowerbed[i] == 0 && flowerbed[i-1] == 0){ // Viable plot
                    tmp--;
                    if(tmp == 0) return 1;
                    flowerbed[i] = 1;
                }
            }
            else{
                if(flowerbed[i] == 0 && flowerbed[i+1] == 0 && flowerbed[i-1] == 0){ // Viable plot
                    tmp--;
                    if(tmp == 0) return 1;
                    flowerbed[i] = 1;
                }
            }
        }
        return 0;
    }
};