class Tweet {
public:
  int tweetId;
  int timestamp;
  Tweet *prevTweet;

  Tweet(int tweetId, int timestamp, Tweet *prevTweet) {
    this->tweetId = tweetId;
    this->timestamp = timestamp;
    this->prevTweet = prevTweet;
  }
};

struct CompareTweet {
  bool operator()(const Tweet *a, const Tweet *b) const {
    return a->timestamp < b->timestamp;
  }
};

class Twitter {
public:
  unordered_map<int, Tweet *> userTweet;
  unordered_map<int, unordered_set<int>> following;
  int timestamp;

  Twitter() { this->timestamp = 0; }

  void postTweet(int userId, int tweetId) {
    Tweet *newTweet =
        new Tweet(tweetId, this->timestamp, this->userTweet[userId]);

    this->userTweet[userId] = newTweet;

    ++this->timestamp;
  }

  vector<int> getNewsFeed(int userId) {
    priority_queue<Tweet *, vector<Tweet *>, CompareTweet> pq;
    if (userTweet[userId] != nullptr) {
      pq.push(userTweet[userId]);
    }
    for (int followee : following[userId]) {
      if (userTweet[followee] == nullptr) {
        continue;
      }
      pq.push(userTweet[followee]);
    }

    vector<int> res;
    for (int i = 0; i < 10; ++i) {
      if (pq.size() == 0) {
        break;
      }

      Tweet *newest = pq.top();
      pq.pop();
      res.push_back(newest->tweetId);
      if (newest->prevTweet != nullptr) {
        pq.push(newest->prevTweet);
      }
    }

    return res;
  }

  void follow(int followerId, int followeeId) {
    if (followerId == followeeId) {
      return;
    }

    following[followerId].insert(followeeId);
  }

  void unfollow(int followerId, int followeeId) {
    if (followerId == followeeId) {
      return;
    }

    following[followerId].erase(followeeId);
  }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
