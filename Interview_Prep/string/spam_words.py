def classify_spam(texts, spam_words):
    # 1. Convert to a Set for instant O(1) lookups
    spam_set = set(spam_words)
    result = []
    
    # 2. Assume the threshold to be flagged is 2 or more spam words
    spam_threshold = 2 
    
    for text in texts:
        # 3. Split into exact words to avoid the "Summertime" vs "Summer" trap
        words = text.split()
        
        # 4. Count the exact matches
        spam_count = sum(1 for word in words if word in spam_set)
        
        # 5. Classify
        if spam_count >= spam_threshold:
            result.append("spam")
        else:
            result.append("not_spam")
            
    return result

# Testing your exact inputs
texts = ["I paid have paid", "Summertime sadness"]
spamWords = ["I", "paid", "Summer"]

print(classify_spam(texts, spamWords)) 
# Output: ['spam', 'not_spam']