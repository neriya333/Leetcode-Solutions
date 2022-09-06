// 100% faster, 38% less memory. great,why is that? idk yet but a 
// trick i missed is using % so that 'nums[0]>=nums[n-1]' from line 14 will be switched with
//for (int i = 0; i<n; i++){if(nums[i]> nums[(i+1)%n]) num_breaks++;} that includes the last item. this is slower(irrelevantly so), and much more elegant. 


class Solution {
public:
    // straight forwards by rules: (always asc || not asc only once and last<=first)
    bool check(vector<int>& nums) {
        int num_breaks = 0,n = nums.size();
        for (int i = 0; i<n-1; i++){
            if(nums[i]> nums[i+1]) num_breaks++;
        }
        if (num_breaks == 0 || (num_breaks==1 && nums[0]>=nums[n-1])) return true;
        return false;
    } 
};
