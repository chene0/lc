class Tweet {
public:
  int timestamp;
  int tweet_id;
  Tweet *prev_tweet;

  Tweet(int timestamp, int tweet_id, Tweet *prev_tweet)
      : timestamp(timestamp), tweet_id(tweet_id), prev_tweet(prev_tweet) {}
};

struct MaxTweet {
  bool operator()(const Tweet *lhs, const Tweet *rhs) const {
    return lhs->timestamp < rhs->timestamp;
  }
};

class Twitter {
public:
  int timestamp;
  unordered_map<int, Tweet *> user_newest_tweet;
  unordered_map<int, unordered_set<int>> following_adj;

  Twitter() : timestamp(0) {}

  void postTweet(int userId, int tweetId) {
    Tweet *new_tweet =
        new Tweet(this->timestamp, tweetId, this->user_newest_tweet[userId]);
    ++this->timestamp;

    this->user_newest_tweet[userId] = new_tweet;
  }

  vector<int> getNewsFeed(int userId) {
    priority_queue<Tweet *, vector<Tweet *>, MaxTweet> pq;

    unordered_set<int> followee_set = this->following_adj[userId];
    followee_set.insert(userId);
    for (int followee : followee_set) {
      if (user_newest_tweet[followee] != nullptr) {
        pq.push(user_newest_tweet[followee]);
      }
    }

    vector<int> news_feed;
    for (int i = 0; i < 10; ++i) {
      if (pq.empty()) {
        break;
      }

      Tweet *next_tweet = pq.top();
      news_feed.push_back(next_tweet->tweet_id);
      pq.pop();
      if (next_tweet->prev_tweet != nullptr) {
        pq.push(next_tweet->prev_tweet);
      }
    }

    return news_feed;
  }

  void follow(int followerId, int followeeId) {
    if (followerId == followeeId) {
      return;
    }

    this->following_adj[followerId].insert(followeeId);
  }

  void unfollow(int followerId, int followeeId) {
    if (followerId == followeeId) {
      return;
    }

    this->following_adj[followerId].erase(followeeId);
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
