class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int n = sentences.size();
        int ma=0;
        for(int i=0;i<n;i++){
            int t=0;
            for(int j=0;j<sentences[i].size();j++){
                if(sentences[i][j]==' ')
                    t++;
            }
            ma=max(ma,t);
        }
        return (ma+1);
    }
};
