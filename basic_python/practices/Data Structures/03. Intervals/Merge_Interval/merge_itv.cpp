#include <algorithm>   // for sort, max
#include <iostream>
#include <vector>
using namespace std;

class Merge {
    public:
        vector<vector<int>> using_sorting(vector<vector<int>>& intervals) {
            sort(intervals.begin(), intervals.end());
            vector<vector<int>> output;
            output.push_back(intervals[0]);

            for (auto& interval : intervals) {
                int start = interval[0];
                int end = interval[1];
                int lastEnd = output.back()[1];

                if (start <= lastEnd) {
                    output.back()[1] = max(lastEnd, end);
                } else {
                    output.push_back({start, end});
                }
            }
            return output;
        }
};

int main() {
    // Create a Merge object
    Merge mergeObj;

    // Define test intervals (each interval: {start, end})
    vector<vector<int>> intervals = {
        {1, 3},
        {2, 6},
        {8, 10},
        {15, 18}
    };

    // Call using_sorting to merge intervals
    vector<vector<int>> mergedIntervals = mergeObj.using_sorting(intervals);

    // Print merged intervals
    cout << "Merged intervals:" << endl;
    for (auto& interval : mergedIntervals) {
        cout << "[" << interval[0] << ", " << interval[1] << "]" << endl;
    }

    return 0;
}