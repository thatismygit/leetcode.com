/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let ans=0
    for (let i=(s.length-1);i>-1;i--){
        if (s[i]!=' '){
            ans+=1;
            continue;
        }
        else if (s[i]==' ' && ans){
            return ans;
        }
        continue;
    }
    return ans;
};
