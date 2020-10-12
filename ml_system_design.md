# Machine learning system design interview prep

This document contains my personal preparation notes for machine learning system design interviews. This document is provided as-is, and contains my personal preparation material. Notes were collected during the summer of 2020.

### News Feed Rankers

- Objective is to get users to stay and engage with the site as much as possible, to keep coming back, to make the service a daily utility in your life
- Candidate posts from liked pages and friends, maybe also local posts, promoted posts, and important news, kept fresh via some time threshold
- Ranked based on the post's predicted interest to the user, i.e. relevance. Supervision signals could be:
    - User's interaction with the post (like, share, comment, those stupid emoji things)
    - Implicit signals, like user's time spent on a page or post
- Baseline and fallback can be newest first only
- Pipeline:
    - Collect candidates. Can have multiple candidate generators for diversity
    - Rank via model scores
    - Rerank based on freshness, diversity, fairness, and filtering out certain types of content
- Data:
    - What is a training sample?
        - A post plus most recent user history and user and environmental features. We **must** consider at the very least the user and the post, because different users obviously have different preferences
    - What is the label?
        - There are likely multiple labels, but we can try to combine them into a single of a few engagement score(s) heuristically (i.e. total score is predicted probability of an event multiplied by the heuristic value of the event), in which case we can use a regression loss like MSE to optimize for scores
        - Certain events can have positive value (like, share, etc) and certain events, especially hide, or dislike, can have negative value
    - Recency effects?
        - Yes, a user can be shown a post and not interact with it until later. So would need to set a time to wait until data can be collected
    - Annotation?
        - Posts come pre-annotated via user interaction or lack of interaction
        - Can also perform manual labeling for post quality, or a manual ranking, and use the manual dataset as a finetune
- Features:
    - Post features (time, content embedding, number of comments, user embedding)
    - User features (past history and preferences, profile (age, gender, etc) embedding)
    - Environmental features (time of day, user's device, etc)
- Model:
    - Hard to do collaborative filtering, since there's not a relatively fixed set of items
    - Can train a shallow (linear or lightly nonlinear) model to take in features and regress an engagement value which combines various supervision signals heuristically (i.e. a comment might be worth more than a like)
    - Would probably need a **filter for clickbait, offensive, violent, or explicit content**
    - Model choice depends on need for interpretability and explainability to the user. Probably something like gradient boosted trees are a good middle ground.
- Evaluation
- Can look at precision/recall tradeoff, what the business case is, and what is acceptable. Can also look at loss and accuracy
- Can train with next round of data such that prediction errors (i.e. posts which the model said was less relevant had high user engagement) are weighted more heavily
- Can do offline testing for model exploration, online A/B testing for evaluation
- Can use certain metrics like model calibration to monitor model behaviour, as a sanity check
- Productionizing
    - Facebook, as large as it is, with billions of users and hundreds of billions of posts, definitely has in-house proprietary tools for building data, training, and deployment pipelines to make it easy for engineers and data scientists to iterate
- Problems:
    - Gauging positive vs. negative engagement. Do we care if a user engages with a post because they feel strongly positively or negatively about the post?
    - **Metric simplicity vs user experience trade-off!** Optimizing for click-through maximizes short-term engagement, gives rise to clickbait. Really want to maximize long-term engagement. However, it's hard to turn long-term engagement into a machine learning supervision signal for newsfeed ranking. Perhaps expert guidance (i.e. knowledge and intuition about human behaviour) can help map short-term supervision signals to approximate long-term engagement. Also, perhaps some manual annotation or ranking of the posts could be leveraged.
    - Optimizing for engagement without consideration for anything else can lead to **feedback loops** where users are put into echo chambers and radicalized. This is a **known problem** with Facebook.
    - Cold start problem - new users won't have many user features, so need a fallback ranking model for new users
    - Post modalities and multimodal posts - posts can be text, images, videos, or a combination. Features are different, but also, supervision signals can be different, so it's hard to fairly compare engagement with different types of posts. Two solutions:
        - Can artificially normalize scores for comparison
        - Can use heuristics for composition patterns, e.g. text, image, video, text, image, video
    - User privacy - are users okay with us running ML models on their data? Need to make sure things we are doing are legal, opt-outs are presented to the user, and that we can ensure security and anonymity 

### Recommender systems

I can create an embedding space for users. I can create an embedding space for items. I can do it in such a way that the user vector times the feature vector is meaningful... i.e. how much that user prefers that item.

Baseline can be the performance of a model which simply recommends the globally most popular items.

Recommender systems have two categories:
1. Content-based filtering
    - Only similarity between items are used to make recommendations
    - For example, if user A clicks on a video of a cat, the system will recommend videos similar to the video of a cat
    - Works by engineering a latent embedding space of items, selects candidates close to items that the user has previously indicated a preference
    - Needs hand-engineered features vectors for the items. Then we can construct a linear regression optimization problem which solves for user vectors which, when multiplied by the item vectors, reconstruct the feature matrix.
    - Advantages:
        - Doesn't need data on other users -- easier to scale to a large number of users
        - Easier to capture specific interests a particular user -- more personalized
        - Engineered features are interpretable
    - Disadvantages
    - Doesn't branch out past what the user has historically liked -- limited capacity to expand
    - Features must be hand-engineered to an extent -- requires domain knowledge
2. Collaborative filtering
    - Similarity between items and similarity between users are simultaneously used to make recommendations
    - For example, if user A is similar to user B, and user B liked a video, then that video can be recommended to user A
    - Classic example is matrix factorization of a user x item preference matrix, A. Prediction for a user's preference for an item is the similarity metric (dot product usually) between the user vector and the item vector
    - Even simpler than matrix factorization, we can create a nonlinear regression optimization problem to pick user vectors and item vectors that form our preference matrix. (or we can alternate between two linear regression problems)
    - Advantages:
        - Only needs user preferences for items (query and item id)
        - Automatically learns user and item feature embeddings
        - Can help users discover new interests
    - Disadvantages:
        - Learned features are harder to interpret than engineered ones
        - Cold start problem - new and users items not seen during training don't have embeddings, so can't take dot product to find preference without retraining the whole model. Can try to solve this by somehow generating an embedding for new users and items using an algorithm or heuristic
        - Hard to incorporate features other than user and item id (side features), though it's possible (e.g. using a block matrix where A(0,0) is the original preference matrix, A(0,1) is the multi-hot encoded user features, block A(1, 0) is the multi-hot encoded item features, and A(1,1) is typically left blank)

Recommender systems are have two (and a half) components:
1. A candidate selection system
    - Turns many options into a few eligible options
    - Does this by building a feature embedding so entities can be transformed into features in a latent embedding space, endowed with a similarity measure such as the cosine similarity, dot product, or Euclidian distance
    - Options:
        - Collaborative filtering/matrix factorization
        - An entity2vec system, like the word2vec system, to build embeddings via context
        - Can learn embeddings as a layer in a neural network
2. A ranking system
    - Scores eligible candidates. Real systems may have multiple candidate generation models, like:
        - The collaborative filtering recommendations
        - Popular or trending items
        - Geographically local or relevant items
        - Items liked by friends
        
        These different candidates are then put into the same pool and scored by the scoring system
    - Why not let the candidate generator score?
        - Multiple candidate generators might not have comparable metrics
        - With a smaller pool of candidates, the system can afford to use a more complex model to make final ranking decisions
    - Options
        - Supervised classification algorithms on the concatenated user/item/environmental embedding vectors like logistic regression, SVM, neural networks, decision tree-related algorithms like gradient boosted trees
3. (Re-ranking/reranking)
    - Re-rank final candidates based on additional criteria or constraints
        - For example, can run models to filter out click-bait
    - Want to emphasize
        - **Freshness - Recommendations should stay up to date**
            - Keeping the model fresh by retraining or fine-tuning often to incorporate newest items and user interactions
            - Add item age or time of last viewing as a feature
            - DNN models can account for new users/items more easily
        - **Diversity - No diversity leads to boring recommendations**
            - Keep the recommendations diverse by using multiple candidate generators with different metrics
            - Train multiple rankers with different criteria
            - Re-rank items based on genre or other metadata to ensure diversity
        - **Fairness - No unconscious bias from training data, treat every user and item fairly**
            - Make separate models for underserved groups
            - Track metrics for different demographics to watch for biases
            - Include diverse perspectives in the design and development process
            - Make sure the training data is inclusive and balanced

Collaborative filtering via deep learning
- Matrix factorization works well, but has some issues
    - Hard to incorporate side features other than user id and item id
    - Popular items tend to be recommended for everyone
- Deep neural networks are typically used for modern recommender systems
- DNNs for recommender systems work like the following:
    - For a single network, the user features (including side features) are the input to the model, and output is the user preferences (i.e. the user's row in the preference matrix A). The final FC layer's weights are the learned embeddings for each item. So a single neural network learns a mapping from a user to its predicted preferences for items, and a single embedding per item
    - For a dual neural network, one network can learn embeddings for users, and another can learn embeddings for items, and the dot product of the two embeddings can be compared to the (user, item) cell in the preference matrix A.
- Advantages:
    - Designed to allow side features
    - Designed to easily handle new users and items
- Disadvantages
    - Harder to train, needs careful regularization to not have a messed up latent space
    - Harder to interpret
    - Embeddings typically calculated at serving time, which is more computationally expensive

Issues:
- Cold start - May not have enough user data at the beginning. Can use some form of entity-only similarity to begin recommendations
- Cold start II - Some systems may have trouble with new users and items without retraining. Can use some algorithm to generate approximate embeddings
Data:
- User data
    - User profile data (age, sex, location, etc)
    - User historical data (past preferences, etc)
    - Environmental data (time of day, user's device, etc)

### Some sources for ranking and recommender systems:
General:
https://towardsdatascience.com/recommender-systems-the-most-valuable-application-of-machine-learning-part-1-f96ecbc4b7f5
https://developers.google.com/machine-learning/recommendation
https://medium.com/recombee-blog/machine-learning-for-recommender-systems-part-1-algorithms-evaluation-and-cold-start-6f696683d0ed
https://www.youtube.com/watch?v=giIXNoiqO_U&list=PL-6SiIrhTAi6x4Oq28s7yy94ubLzVXabj
https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-recommendation-engine-python/

Case studies:
https://blog.twitter.com/engineering/en_us/topics/insights/2018/embeddingsattwitter.html
https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429
https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-2-d9b96aa399f5

Papers:
https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf
https://arxiv.org/pdf/1409.2944.pdf

### Broad steps for system design:
####1. Problem definition/Problem exploration
- What are we trying to do, how do we define success, what are the metrics we should be using?
- Right setups and correct choices here can be more important than choosing the most optimal model
- What are the ultimate goals? How do we break these down into problems that machine learning can solve? For example, if the relevant metric is "user enjoyment", which is complex and difficult to define and measure, we might use a proxy metric like "sessions per week", which is easier to measure and model.
- Need to consider user experience - how exactly will the user interact with the predictions of the model. How personalized do the predictions need to be?
- When **choosing metrics**, need to consider
    - **performance constraints** - how good and/or fast does the model have to be? What's more costly, false positives or false negatives?
    - **response time** - how long it takes for a proxy event to be measured greatly affects how long it takes to iteratively refine your strategy
    - **data sparsity** - if positive examples are extremely rare, this affects which models can be chosen and accuracy down the line. Often, dataset imbalance is counted via the rarest labels. Different algorithms are better suited for different amounts of data and different levels of sparsity
    - do **features contain information about the event**
    - is the event **affected by a large amount of variance**
    - Consider user experience tradeoffs and pitfalls to metrics. For example, when considering maximizing user engagement for a video site:
        - If the scoring function optimizes for clicks, the systems may recommend click-bait videos. This scoring function generates clicks but does not make a good user experience. Users' interest may quickly fade.
        - If the scoring function optimizes for watch time, the system might recommend very long videos, which might lead to a poor user experience. Note that multiple short watches can be just as good as one long watch.
- Try to pare down the problem as much as possible, to **leave as little room for interpretation as possible**. Real world problems often have a huge amount of room for interpretation, which is bad for creating well-defined machine learning problems
- **Be very precise about what a training example is**, how the label is obtained, and what the metric we're trying to improve with machine learning actually is
- **Metrics should be:**
    - **interpretable**
    - **sensitive to improvements in the model**
- Types of metrics:
    - regression: mse, mae (doesn't punish outliers as extremely as mse), r^2 ([mse(baseline) - mse(model)]/mse(baseline), for comparing against a baseline)
    - classification: accuracy, precision (tp/(tp+fp) if we care about maximizing true positives amongst positive predictions), recall (tp/(tp+fn) if we care about maximizing true positives amongst actual positives), F1 (precision*recall/(precision+recall), harmonic mean of precision and recall), AUC (aggregate measure of performance across all classification thresholds -- gives probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one)

TLDR: 
- What is the machine learning task for the problem
- Simple is better than complicated
- Be as precise as possible when defining what a training sample and a label are
- Think about edge cases up front
- Don't prematurely optimize
- End with a well-defined machine learning task

#### 2. Data gathering/parsing
- It may be that it turns out to be too difficult or impossible to gather the data that step 1 requires, which means further iteration is required
- What are the **inputs and outputs** of the model?
    - There can be **user-related data, event-related data, environmental data**, etc. For example, when considering a model which recommends apps to a user, we might have access to the user's profile (age, occupation, sex, etc), app history, environmental variables (time, location), and the app profile for every app on the system, and our output could be a binary classification of match-ness for the user given all the variables
    - Consider data types:
        - Categorical (ordinal, nominal, etc) - needs to be encoded
        - Continuous - needs to be normalized
- **How do we collect and annotate data?**
    - **What kind of data and how much of it is available**
    - Are labels already annotated, and **how good are the annotations**
    - If more annotation is needed, **how expensive is it to hand-annotate?** How are disagreements between human annotators settled?
    - Are there ways to **leverage unlabeled or partially labeled data** to pretrain the model or to automatically generate labeled data?
- Data issues:
    - **Data recency/seasonality** (sensitivity to time) - It may be that older data doesn't contain as relevant information, or it may be that data at different times give different results. Something to test here is if a progressive evaluation of a model training up to day N on new data gathered on days N+1, N+2, N+3 shows progressively worsening results, it may mean that the model is very sensitive to how recently it was last trained. Can consider engineering a real time data gathering/training system -- real time systems have their own pitfalls, since there may be a delay between when an event starts to when a label is available (i.e. how long do you wait for a user to click on a post after its shown before you say whether or not they would have clicked on it)
    - **Online/offline consistency** - making sure that the data used in training is actually the same as the live data being shown to users. One option is to save the entirety of the live data, but this requires logging and storage. Another option is to save just an identifier which points to a copy of the data offline, or allows us to recreate the live data, but then we have to make sure that the offline and online data are identical
    - How is the data **stored**?
    - How do we handle **multimodal data**, i.e. text and images?
    - **How much data is needed**, trade-off between more data and heavier compute loads and iteration times
    - How to handle **incomplete or missing data** - this is almost always a problem. What happens if our model uses the age of the user, but the age is missing? How do we handle this during training and inference?
        - An option is to **impute** the data, i.e. replace it with the mean value from the dataset, or a constant like 0 (or a one-hot vector of zeroes), or a random value from another sample, or a value estimated via building another predictive model
        - We can select algorithms that are **robust to missing data**. For example, kNN can be made to ignore a column when computing distance, naive bayes doesn't care about missing values, and some tree-based models can treat missing data as a special case or specifically account for missing values
        - We can make our model more robust to missing data via **regularization**. For example, in computer vision, missing pixels are no big deal usually, since we can specifically augment with missing pixels if needed
    - In the worst case, sometimes we just can't make a prediction practically, if most data is missing. In this case, we may present the user with an **alternative or default**.
    - How to handle **imbalance** - usually some kind of sampling is used
    - Sources of **bias** in the data
        - i.e. if there was a **hard-to-control problem in data collection**, like if certain devices captured less clicks. Then the model would still be faithfully predicting from the training data, but the training data would no longer be the same as the ground truth data
        - Is the data inclusive, or will it reinforce existing **societal biases**?
    - **Privacy** - need to consider how data collection impacts the user's privacy. Could we **anonymize the data** if privacy is a concern? Are we allowed to **store user data on servers, or can we only access it on the user's system?**
- Train/eval/test split
    - Train is for learning parameters, eval is for tuning hyperparameters, and test is for final result only
    - Classic approach is to do **k-fold cross-validation with random splits**. However, might want to consider factors like time and data recency here -- with a random split, some training data might be more recent than test data, which wouldn't happen in the case for online prediction
    - A **progressive evaluation approach**, where data is split in time (eval and test data is newer than training data), and new data gets added to the test and eval sets first, might mimic the true use case better
    - Might want to **split the evaluation set into distinct subgroups** (this is like looking at a confusion matrix), to see where accuracy and loss in accuracy occurs

TLDR:
- Identify the model inputs and outputs
- Consider data collection and annotation
- Consider data-related problems: recency, online/offline consistency, storage needs, multimodality, imbalance, missing data, bias, and privacy
- Consider how to do data splitting for evaluation and testing

#### 3. Feature selection
- **Features should be:**
    - **relevant to the output**
    - **interpretable by the model**
- Feature types:
    - categorical
    - continuous
        - Less interpretable
    - derived
- When selecting features, want to choose ones with high correlation with the output, and discard ones with high correlation with other features that are already used. 
- Things to watch out for:
    - Some features can have a **feedback loop**! Features used to train models which then affect future values of that feature. Need to carefully consider implications and dependencies of features when using them to train models - https://www.youtube.com/watch?v=QWCSxAKR-h0&feature=emb_title
    - Feature breakage - **Features with changing semantics over time** -- for example, a feature derived from a user's interaction with a front-end element can have its meaning and context changed if the front-end element is changed. There must be clear agreement with partner teams over what exactly a feature means.
    - When a feature changes semantic meaning, it's usually better to design a new feature instead of using the old feature, train a model with the new feature, and then deprecate the old one
    - Also feature breakage - **Features with different meanings between training and the live system**. Need to make sure features are constant in definition throughout the system. Should only have one interpretation of the feature computation code
    - Feature leakage - **direct information about the output can erroneously end up in the training data**, leading to results that are too good
    - Feature coverage - **what percentage of the data contains a feature**. Perhaps it's not worth it to design and use a feature if less than 10% of the data includes that feature
   
TLDR:
- When selecting and designing features, make sure features are relevant to the output, and are interpretable by the model
- Consider potential issues like feature coverage, feedback loops, feature leakage, and feature breakage

#### 4. Model choosing/training/debugging
- Might be that, at this stage, we find that we need more data or need to relabel our data, which means further iteration is required
- Data and features should weigh heavily in the choice of model
- Don't always want to choose the fanciest model. Some practical considerations:
    - Interpretability and reproducibility
    - Ease of debugging
    - Data volumes
- Linear models are fast, interpretable, easy to debug, and can handle different data volumes, and are good choices for cases where there is little data. Also, we can inject nonlinearity into linear models by, for instance, transforming our features into a representation which a linear model can handle
- **Complex, difficult to interpret models are good if you only care about accuracy**. On the other hand, if you need to, for example, explain to users why the machine learning model did something, a more interpretable model would be a good choice
- Feature selection and engineering
    - Identify features which have high predictive power
    - May want to remove features which are often missing or incorrect
- Break the task down into types for choosing a model type
    - supervised vs unsupervised vs semi-supervised
    - discriminative vs generative
    - classification vs regression
    - linear vs nonlinear
- Frame each objective as a machine learning task
    - regular classification or regression from features
    - text classification
    - image classification
    - sequence prediction
    - object detection
    - dimensionality reduction
    - recommender system
    - etc
- Start simple, add complexity as needed. Deep learning is cool, but often not needed for many tasks, and they are much harder to train and explain
- Establish a **baseline**. The model might need to outperform a heuristic baseline significantly to justify its existence
    - **Random baseline** (How well would a choice at random do?)
    - **Simple heuristic** (i.e. base an app recommendation only on past-week app frequencies)
    - **Human baseline** (how well would a human do at the task)
    - **Model baseline** (i.e. choose a simple, well-established, easier to train model for a base, and/or look at the cutting edge research for a cap)
- Identify effective heuristics
- **Optimize parameters**
    - **Hyperparameters** (learning rate, regularization, etc)
    - **Model architecture parameters** (number of trees in a decision tree, layer size in neural networks)
- **Reproducibility is important** -- should keep track of training data and parameters, so that comparison between different iterations and different models is possible
- **Ablation studies** (turning on or off one model aspect at a time and keeping the rest off or on) can help to understand what the model is doing

TLDR:
- Establish a baseline to compare with
- Don't worry too much about the model choice at first - start simple and iterate
- A little nonlinearity often goes a long way
- Be careful and systematic about keeping track of model iterations
- Consider tradeoffs between accuracy and interpretability
- Consider running hyperparameter optimization and ablation studies

#### 5. Accuracy testing/experimentation
- Types of evaluation
    - **Offline** evaluation with logged data - for some models, like image and speech recognition, offline evaluation is representative of real life
    - **Online evaluation** with live data
- **Online-offline gap** - difference between online and offline performance, want to minimize
- **Look out for feedback loops** - if the model affects future data on which it will be trained, we need a different approach
- **Aim to have some form of online testing as soon as possible**
- Make sure one is **able to triangulate the cause of the shift in metrics from a test** - often it's not good to bundle multiple improvements into a single test. Given a neutral result, some changes could be helping, and some could be hurting, or they could all be neutral.
- **Online experimentation: A/B test** - Split live users into a control and test group
- Usually, use **offline evaluation to narrow down candidates, validate with online experiments**. Must validate with online experiments, because that is the ultimate goal of the model
- Important to choose a **baseline** so that model results can be put into context
- **Model calibration** (making sure the predicted frequency of labels matches the empirical frequency of labels) is a quick sanity check -- can try label smoothing maybe!
    - If the model is miscalibrated on the training set, then it means that it hasn't learned properly
    - If the model is miscalibrated on the test set, then it means that it doesn't generalize well
    - If the model is miscalibrated on the live system, then it means that there's some kind of online/offline gap
- What are some important sources of error?
    - Avoidable vs unavoidable errors
    - **Errors originating from the data**, e.g. incorrect, missing, or mislabeled data, also variance in data, outliers, etc. Biases in the data, i.e. biases originating from the data collection method, or from structural biases in society. Also, time and recency effects in the data
    - **Errors originating from the model**, so basically underfitting and overfitting (generalization error)

TLDR:
- Offline evaluation for wide exploration and candidate selection, online evaluation for live testing
- Online testing: A/B (test/control) test
- The data evaluated on and the statistics calculated both should aim to reflect the use case as closely as possible
- When evaluating your model, understand where the performance (or lack of performance) comes from, i.e. sources of error

#### 6. Model serving/deployment, performance monitoring
- At this stage, it may be that, after serving the model to users, the way they are using it is very different from the assumption made during step 1, which means further iteration is required
- Need to consider scalability
    - Do we run models on user devices, or the cloud?
    - When training or predicting, how do we make use of parallelism?
- What are some sources of misuse of our model, and how do we address them?
- What is a fall-back, or default, if our model fails or runs into an error, or we don't think our prediction is valid? The system should handle errors gracefully.
- How does one introduce updates to the model once its deployed? Can use online machine learning, incremental stochastic gradient descent, etc.
- Logging and monitoring - keep track of model performance (model calibration, for example)

## Case Studies

#### 1. Predicting Fraud at Stripe 
(https://www.youtube.com/watch?v=QWCSxAKR-h0&feature=emb_title)
- Machine learning system for classifying fraudulent transactions
- Time lag of months between event and truth label
- Metrics:
    - Precision/recall curve
    - ROC curve/AUC
- Precision/recall tradeoff
- Future training data are only transactions which are allowed -- missing big chunk of samples from the actual distribution -- feedback loop
- Solution: let in samples which have scores which would have normally disallowed them some percentage of the time
- Set training weights higher for let-through transactions during training, since they represent a sample of a much larger set of data points
- "Exploration/Exploitation tradeoff" - The more transactions you let through, the better you're able to measure performance and train your model ("exploration"), but because you're letting things through, the less you're actually able to exploit the performance of your model ("exploitation")

#### 2. Amazon recommender system from 2003
(https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf)
- Machine learning system for making online store recommendations
- Metrics:
    - Click-through rate (item clicked)
    - Conversion rate (item purchased)
- Preference matrix is very sparse -- new customers have very few entries, old customers might have lots of entries
- Customer data is volatile: each new customer interaction is valuable new data, must respond and incorporate into model asap
- Rejected methods:
    - "Traditional (user-to-user)" collaborative filtering: 
        - customer vector of size N, where N is the number of items.
        - recommendations generated based on cosine similarity between user and similar users. Items liked by similar users are recommended
        - Disadvantages:
            - Computationally expensive. O(MN) (M users, N items) worst case, but O(M) average case because users are typically sparse in N
            - Can reduce M randomly sampling users, discarding users with few purchases, reduce N by discarding rarely purchased items, dimensionality reduction with PCA, but all degrade recommendation quality
    - Clustering:
        - Divide users into clusters based on their customer feature vector via an unsupervised learning algorithm
        - assign a user to a cluster, then use preferences of that cluster to generate recommendations
        - Usually, N is too high, need some kind of dimensionality reduction
        - Better scalability because each user is compared to a small number of cluster centroids instead of every other user
        - Disadvantages:
            - Low recommendation quality, clusters are too general so it's hard to make very personalized recommendations
    - Search-based:
        - Recommend via search for related items via tags
        - Scales well for users with a few purchases
        - Disadvantages:
            - Doesn't scale well for users with lots of purchases
            - Poor recommendation quality - either too general (popular items) or too specific (only books by a specific author)
- Selected method:
    - "Item-to-item" collaborative filtering:
        - Build item similarity table based on items purchased together
        - Item vector from user purchases, cosine similarity
        - Makes recommendations by aggregating most similar items to the user's purchases as candidates, then recommends the most popular or most similar items
        - Advantages:
            - Very fast online computation
            - Higher recommendation quality
        - Disadvantages:
            - Very slow offline computation

#### 3. Instagram's Explore recommendation system
(https://ai.facebook.com/blog/powered-by-ai-instagrams-explore-recommender-system/)
- Machine learning system to recommend posts to instagram users
- Building blocks (needed work in three areas):
    - ability to rapidly experiment at scale
    - stronger signal on breadth of people's interests
    - computationally efficient way to make sure recommendations were high quality and fresh
- For rapid experimentation, implemented a custom querying language for building and testing recommender pipelines (IGQL)
- For capturing interests, created an account-level embedding, ig2vec, like word2vec. Account and content likes made by a user are treated as context elements  in chronological order, like words in a sentence. Can then search for similar accounts via kNN, and can assess how good the embedding does at capturing account topic via training a classifier against human-annotated account topics
- For computational efficiency in creating candidates, more complex models are compressed via model distillation. Distilled models pre-select candidate models before passing on to more complex models for final ranking
- Recommendation pipeline:
    - Accounts a user has interacted with are seed accounts
    - Use embedding to find accounts similar to seed accounts (more than one candidate generator)
    - Posts by accounts similar to seed accounts are candidates -- tens of thousands of candidates generated for a single person
    - Sample 500 candidates from eligible candidates, send to downstream ranking
    - Ranking narrows down in 3 stages:
        1. Distilled ranking model with minimal features goes from 500 to 150 of the highest quality and most relevant
        2. Lightweight neural network with full, dense features goes from 150 to 50
        3. Deep neural network with full, dense features goes from 50 to 25
        4. Final re-ranking with diversity heuristic
    - Neural networks trained on user previous positive and negative actions. Inputs are concatenated viewer, creator, and content feature vectors. Outputs are user actions (like, share, subscribe, etc)

To summarize:
- Custom language (IGQL) for rapid prototyping
- Account-level embeddings are created via ig2vec (context-based embedding)
- Candidate generation via accounts similar to accounts a user has interacted with
- Ranking narrows down via neural networks trained on past user preferences. For scaling up, distilled and lightweight models pre-narrow candidates.

#### 4. Airbnb predicting home values
(https://medium.com/airbnb-engineering/using-machine-learning-to-predict-value-of-homes-on-airbnb-9272d3d4739d)
- Tries to predict LTV (user lifetime value) of new listings: the predicted value, usually in dollars, of a listing over a fixed time horizon
- Overall ML pipeline:
    - Feature engineering - define relevant features
    - Prototyping and training - train a model prototype
    - Model selection & validation - model selection and tuning
    - Productionization - taking a model to production
- Feature engineering:
    - 150 features, including:
        - Location: country, market, neighbourhood, geography, etc
        - Price: nightly rate, cleaning fees, price point relative to similar listings, etc
        - Availability: Total nights available, % of nights manually blocked
        - Bookability: Number of nights booked in the past X days, etc
        - Quality: review scores, number of reviews, amenities, etc
    - Custom internal tool to aggregate and design features (zipline)
    - Missing values understood and imputed
    - Categorical features one-hot or ordinally encoded
- Prototyping:
    - Used tools for rapid prototyping - data transforms and training
- Model selection
    - Interpretability/accuracy tradeoff - some models need to be explainable
    - Bias/variance tradeoff
    - AutoML tools enable fast evaluation of multiple models
    - Gradient boosted trees (xgboost) found to be the best
- Productionization:
    - Need to periodically retrain
    - Need to efficiently predict on a large number of samples
    - Performance monitoring pipeline
    - Used a tool which automatically transforms models in a jupyter notebook into a production pipeline

#### 5. Dropbox OCR Pipeline
(https://dropbox.tech/machine-learning/creating-a-modern-ocr-pipeline-using-computer-vision-and-deep-learning)
- OCR tool for portable document scanner
- Started with off-the-shelf library, integrated into tool, to gauge user demand
- With user demand, decided to build in-house OCR tool
- Three broad stages:
    - Research and prototyping
    - Productionizing model
    - Refinement in the real world
- Research and prototyping:
    - Collected data from users, optionally, and with strong privacy considerations
    - Annotated using MTurk-ish tools, either for crowdsourced annotation or using contractors (DropTurk)
    - Two model components
        - Detect lines and words from a document
            - Precision/recall tradeoff - chose to have high recall, which meant a lot of false positives
            - Injected negatives (non-words) into training set to deal with false positives
            - CNN object detectors not suitable for detecting thousands of words in a document
            - Used maximal stable external regions (MSER) OpenCV algorithm, basically a blob detector
        - Deep neural network to recognize words
            - Used the standard pipeline for word-level OCR
            - CNN -> Bi-LSTM -> Connectionist Temporal Classification loss
                - Chop up input image into overlapping segments
                - CNN on all the segments in order to produce features
                - Bi-LSTM on features to classify into single characters. Bi-LSTM used so that characters are not just classified based on visual features, but also based on context for letters before and after
    - This is a use-case where synthetic data could be generated, i.e. text with different font, underlines, rotations, shears, blurs, crops, etc.
    - Iteratively improved dataset until accuracy peaked
    - Divided evaluation set into different types of documents, e.g. scanned documents, receipts, screenshots, etc
    - Trained on synthetic data to 80% single word accuracy, finetuned on annotated real images to 90% accuracy
- Productionizing:
    - Created abstractions for OCR pipelines, including the existing off-the-shelf solution and in-house solution
    - Ported model to Tensorflow
    - Security considerations
    - Uploaded images gets sent to server cluster for OCR processing, returned text is merged with original PDF
    - Used CPU servers instead of GPU servers after testing for performance
- Refinement
    - Tested new system vs old system with user-donated images
    - Needed to create a CNN classifier for document orientation

Key take-aways:
- Baselined against off-the-shelf OCR library
- Lots of work put into building and refining dataset, getting user data, annotating user data, and creating synthetic data
- Model broken down into two parts: word detection, and word recognition
- Iterative improvements to model and dataset through offline testing -- supplementing training set in various ways after identifying issues, dividing evaluation set into categories to more finely track issues, etc
- Lots of production considerations, like deployment alongside existing OCR infrastructure, which type of servers to use, performance tuning, etc
- Online testing of new vs old system on actual user data
- Resolving in-production issues like document orientation

#### 6. Automated fashion advice at Chicisimo
(https://medium.com/hackernoon/how-we-grew-from-0-to-4-million-women-on-our-fashion-app-with-a-vertical-machine-learning-approach-f8b7fc0a89d7)
- Getting people to use an app is easy, retaining them is difficult:
    - Need to identify which levers can be adjusted to increase retention
    - Use retention understanding to tailor on-boarding process
- Understand how people relate to the problem, and how people relate to the product --> understand through direct user feedback
- Created an ontology - a hierarchical list of descriptors for fashion, and connections between the descriptors - this facilitated classification
- User input:
    - Taste
    - Which articles of clothing they own
- Collaborative filtering to make recommendations

#### 7. Fraud detection at Lyft
(https://eng.lyft.com/from-shallow-to-deep-learning-in-fraud-9dafcbcef743)
(https://eng.lyft.com/interactions-in-fraud-experiments-a-case-study-in-multivariable-testing-e0525b11751)
- Classification of users and transactions as fraudulent
- Model selection
    - Logistic regression is a good baseline -- regression coefficients are easily interpretable as how much a feature correlates to the output
        - However, logistic regression requires laborious hand-engineering of features in order to cover more complex feature interactions
    - XGBoost
        - Big boost in precision compared to logistic regression
        - However, boosted trees are less explainable and less interpretable
        - Explainers and feature importance tools exist to help with interpretability and explainability
    - Deep learning models in Tensorflow currently used in production
        - Better able to handle sequential inputs than XGBoost
- Productionizing:
    - Needed to build a pipeline to serialize models and deploy them
    - Currently using modern, containerized model execution

## Summary Notes

#### Tradeoffs:
- **Metric ease-of-implementation and simplicity vs. user experience** - often, optimizing for the simplest metrics, like click-through rate, can have a negative impact on user experience
- **Model accuracy vs. interpretability** - more complex and expressive models are usually less interpretable
- **Precision vs. recall** - Precision and recall naturally trade off. Having a high prediction threshold means high recall, having a low prediction threshold means high precision
- **Exploration vs. exploitation** - sometimes, aiming to improve the model and test new models (exploration) can mean the benefits of using the model (exploitation) are reduced
- **Bias vs. variance, or underfitting vs. overfitting** - Simpler models have high bias, i.e. they fit the training data poorly since they aren't very expressive, but they have low variance since they are so simple. This is underfitting. Complex models fit the training data very well, sometimes TOO well, so they have low bias. However, they have high variance since they are so complex. This is overfitting.
- **Model accuracy vs. speed**

#### Special considerations/pitfalls:
- **Time/recency effects** - Time between an event and when an event has occurred, and how strongly the prediction depends on time/seasonality, or the recency of the data
- **Missing/imbalanced data, feature coverage** - Consider how the data pipeline and model handles missing/imbalanced data. Consider how much of the data actually contains a feature and whether it's worth to design a feature around it
- **Online/offline consistency, feature breakage** - Make sure features mean the same thing between the offline and online versions, and that they don't change semantic meanings without the model being aware
- **Feature leakage** - Make sure direct information about the output doesn't erroneously get into the data
- **Bias in data** - Look for possible biases in data collection, societal biases
- **Feedback loops** - Model can affect future data, which is used to train the model. Need to carefully consider data dependencies to catch feedback loops
- **User data privacy** - Privacy concerns over collecting and using user data. Can directly ask users to volunteer data. Consider whether user data can stay on their device or needs to be uploaded to somewhere else. Consider whether it's possible to anonymize data.
- **Fallback mechanism** - When a model is in production, need a fallback for if the model fails to make a prediction or runs into an error. Also need a default behaviour if the entire model breaks.

#### Key points:
- Business problem definition -> Data -> Features -> Model -> Evaluation -> Production -> Refinement
- Turn business goals into objectives, frame objectives into machine learning tasks!
- Be precise about model inputs and outputs!
- Be precise about what a training example and label is!
- Start simple and iterate!
- Baseline!
- Break tasks down into components!
- Start linear!
- Test! Offline testing for exploration, online testing for evaluation!
