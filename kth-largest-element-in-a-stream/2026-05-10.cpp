class KthLargest {
public:
    vector<int> pq;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;

        for (int num : nums) {
            this->pq.push_back(-num);
            push_heap(this->pq.begin(), this->pq.end());

            if (this->pq.size() > k) {
                pop_heap(this->pq.begin(), this->pq.end());
                this->pq.pop_back();
            }
        }
    }
    
    int add(int val) {
        this->pq.push_back(-val);
        push_heap(this->pq.begin(), this->pq.end());

        if (this->pq.size() > this->k) {
            pop_heap(this->pq.begin(), this->pq.end());
            this->pq.pop_back();
        }

        if (this->pq.size() == 0) {
            return -1;
        }

        return -this->pq[0];
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
