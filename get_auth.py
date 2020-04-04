import twitter
api = twitter.Api(consumer_key="KjJtIWs3M8IV5xnHcQu4GRmVG",
                  consumer_secret="0QAOdpQUWFEGVDPTwwVr5xBc9KQ0qTrNxo7mDDpKJPtaABnqc1",
                  access_token_key="396829597-rIdQWFeG5JYvs1yVX1xI1Z3HrJ7E5SgrcbeIFUKz",
                  access_token_secret="a5Ji6xzYZjEgP3j7d1n1NVNrE2iqWLoHFrm1DIjIvWbH3")
api.sleep_on_rate_limit = True
