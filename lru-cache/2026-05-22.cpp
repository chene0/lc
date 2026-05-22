class LRUCache {
public:
  using entry = pair<int, int>; // (key, value)

  int capacity;
  unorderd_map<int, list<entry>::iterator> d;
  list<entry> q;

  LRUCache(int capacity) { this->capacity = capacity; }

  int get(int key) {
    auto i_pair = this->d.find(key);
    if (i_pair == this->d.end()) {
      return -1;
    }

    list<entry>::iterator i_entry = i_pair->second;
    this->q.splice(this->q.end(), this->q, i_entry);

    return i_entry->second;
  }

  void put(int key, int value) {
    auto i_pair = this->d.find(key);
    if (i_pair != this->d.end()) {
      list<entry>::iterator i_entry = i_pair->second;
      i_entry->second = value;
      this->q.splice(this->q.end(), this->q, i_entry);
      return;
    }

    list<entry>::iterator i_entry = this->q.insert(this->q.end(), {key, value});
    this->d[key] = i_entry;

    if (this->d.size() > this->capacity) {
      entry pop = this->q.front();
      this->q.pop_front();

      this->d.erase(pop.first);
    }
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
