/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let record={};
    for (const num of nums){
        if (!(num in record)){
            record[num]=1;
            continue;
        }
        return true;
    }
    return false; 
};
