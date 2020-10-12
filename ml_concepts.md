# ML Interview question prep

This document contains my preparation notes for machine learning concept interview questions (as opposed to machine learning system design). This document is provided as-is, from my personal interview preparation, and includes answers more geared towards computer vision, since that's my field. Notes were collected during the summer of 2020.

### What is the difference between a regular autoencoder and a variational autoencoder?
    
A classic autoencoder uses an encoder/decoder architecture to do dimensionality reduction. Basically features (in feature space) get compressed (into a latent space, usually with fewer dimensions than the original feature space), and the goal when minimizing the loss (like mean-squared error between input and output) is to have the best compression and decompression possible, with as little compression loss as possible. Uses of autoencoders are generally limited to dimensionality reduction, noise removal, etc.

Variational autoencoders are generative models which use some tricks to regularize the latent space. Regular autoencoders have a problem if the goal is to generate new data by sampling the latent space, which is that a point near the latent space representation of a feature vector is not guaranteed to be similar to the feature vector itself. This is because regular autoencoders map to a single point. To get around this, variational autoencoders encode each feature vector to a distribution in the latent space (practically, this means that each feature vector gets encoded to two vectors, a mean and a variance), and then the decoder samples a point from this distribution instead of directly using the encoded point. This sampling from a distribution has the effect that the latent space is smoother and more regular. However, the means could still be far apart, with narrow variances, so an additional loss term, the Kullback-Leibler divergence, penalizes the network for choosing means and variances too far away from a mean of 0 and variance of 1. This has the effect of encouraging the network to model the latent space as a smooth space of distributions with mean roughly zero and variance roughly one. Then, when we decode another point from the latent space distribution, we are more likely to get a meaningful result.

TLDR:
- autoencoder is for dimensionality reduction, variational autoencoder can also be used for generation
- VAE regularizes points in latent space by treating feature points as distributions and sampling, and tries to keep distributions close together by putting a KL divergence term in the loss

### How does normalization of input data affect machine learning? On decision trees in particular?

Normalizing data, and also having normalized weights (so that all scales are roughly equal), makes gradient descent easier in theory, because the function to be minimized then doesn't have wildly different scales, which lead to gradients in some directions which are much larger than gradients in other directions. Vastly different scales in the loss function makes convergence of gradient descent much harder because the local gradient direction can be very different from the direction of the global minimum. In deep learning, input normalization is always a good idea, since in many cases the loss can depend on the weights directly (weight decay, etc), which means that, while weights may compensate for different scales, loss functions might penalize those weights differently as a result. Though, theoretically, for normal loss functions, deep neural networks should be resilient to input data scaling because it can learn weights which counteract the scale.

Also, when using certain activation functions like sigmoid, its important that the histogram of inputs to the activation function stays in the region where the derivative of the activation function is nonzero.

Decision trees aren't affected by data scaling because the decision threshold can just scale in the same way as the data.

TLDR:
- Normalized input makes gradient descent converge better by making sure there aren't wildly different scales in the feature space
- DNNs can theoretically be resistant to different feature scales, but still best practice to normalize input data
- Decision trees aren't affected by data scaling as long as thresholds scale with data

### What are the advantages and disadvantages of using second-order statistics in optimization?

Disadvantages are computational cost and complexity, since you need to approximate second derivatives. Advantages are potentially much faster optimization, since you are taking the second derivative into account with your optimization, so you are approximating the function locally as a quadratic instead of as linear. This means you can solve for the next update explicitly instead of deciding how far to move like with gradient descent.

The disadvantages obviously outweigh the advantages so far, because Newton's method (for optimization) is rarely used over gradient descent.

TLDR:
- Advantages are that it should be faster to converge, also instead of gradient descent where you have to decide how far you want to go, with second order methods you simply solve for the next optimal point
- Disadvantage is computational cost, you need to approximate the Hessian and solve a system of linear equations at each time step

### How does support vector regression work compared to support vector classification? How does support vector regression work compared to linear regression?

Support vector machines for classification use the soft margin loss (hinge loss plus regularization) to try to find parallel hyperplanes (for the linear case) which maximize the distance between two different classes in feature space. Support vector regression basically does the opposite of this, and tries to find a hyperplane and a margin which has as many data points inside the margin as possible, and the soft margin loss punishes points outside the margin. This differs from linear regression in that points inside the margin don't contribute to the loss at all, whereas in linear regression, all points contribute quadratically (depending on which loss function is used) to the loss.

TLDR:
- SVM is a 2-class classification problem that finds an optimal linear decision boundary by maximizing the margin between feature points of different classes, and uses the margin loss to punish points that enter or cross the margin
- SVR is a regression technique that tries to keep as many points INSIDE the margin as possible, and uses the margin loss to punish points outside the margin.

### What are some strategies for making sure machine learning models are robust? What about checking that they are robust?

Regularization techniques generally help with robustness, by making the underlying function being modeled more smooth. To check robustness of the training process, can use cross-validation, or some other technique where the training and test data is perturbed. If the model behaves differently under small perturbations of the training and test data, that's a sign it's not robust.

Metrics for model performance can be an indirect indicator of model robustness. An obvious metric for performance is how small the loss gets. Metrics like the receiver operating characteristic (ROC) curve, i.e. true positive vs false positive rate, can also be a gauge of how performant the model is.

TLDR:
- Regularization helps with robustness
- Robustness can be checked via cross-validation, and with metrics such as the ROC curve

### What is the concept of momentum in gradient descent? What happens if the momentum parameter is set to 1?

Momentum, for gradient descent, makes the next step a mix between the current gradient, and a weighted average of the previous steps. This has the effect of giving the direction a sort of inertia, so that instead of moving in whichever direction is the best gradient, the momentum term dampens the oscillating behaviour of regular gradient descent. Momentum is useful for stochastic mini-batch gradient descent because with small batches, the gradient is naturally noisy, so having some inertia can help gradient descent power out of local minima/maxima, where the gradient by itself is very small.

Mathematically, momentum is applied like
current update = momentum parameter * last update + learning rate * gradient

So if the momentum parameter is equal to or larger than one, it'll grow (accumulating all past gradients if equal to one, or exponentially if greater than one), which makes gradient descent unstable. So if beta >= 1, you should expect a large amount of oscillation and for the error to increase linearly or exponentially. So the error will likely diverge.

TLDR:
- Momentum adds a term to the gradient update which is the previous gradient update multiplied by a number, resulting in an exponentially decaying average of previous updates
- Momentum helps with SGD by adding inertia to the gradient direction
- If momentum parameter >= 1, instability will occur since the accumulation will be exponentially increasing instead of decaying

### What is the difference between regular momentum and Nesterov momentum?

The difference is at which point the gradient is computed. For regular momentum, the equation is
current update = momentum parameter * last update + learning rate * gradient

The gradient in that equation is calculated at the current values of the weights, so it's like the weights are taking two steps, one gradient step, and then one momentum step. In Nesterov momentum, the gradient is calculated at the current values of the weights plus the momentum update, so it's like the weights make a momentum step first, and then at the new value of the weights after the momentum step, the gradient is calculated, and then the gradient step is taken.

The idea is that this makes the momentum process converge better. Implementations of this don't use a 2-step computation for the momentum vector and the gradient vector I think, and use some clever one-step calculation.

TLDR:
- Nesterov momentum evaluates the gradient after the momentum step instead of before

### What is batch normalization and how does it help in training deep networks? What are some issues with it?

Batch norm is a layer which enforces that the mean and covariance coming out of a layer are standardized (typically mean 0 variance 1) to reduce the mysterious “covariant shift” effect that is supposed to happen in deep layers. A single, trainable mean shift and variance multiplier are then learned for the layer. This might seem to undo the effect of the normalization, but supposedly having a trained single value which control mean and variance makes the network easier to train compared to having the mean and variance depend on behaviour at preceding layers. At inference time, since there’s not necessarily a batch to normalize to, implementations usually keep a running average of batch mean and variances to use at inference time.

Mathematically, in the 1D case, it operates per feature, so if your tensor is batch size of 64 and feature length of 512 for a 64x512 tensor, 1D batch norm needs 512 * 2 parameters, or one mean and one variance for each feature.

Typically, both the original paper and deep learning book recommend putting a batch norm layer between the linear part of the transform (Wx+b) and nonlinearity (relu). So a typical conv layer is like conv2d->batch norm->relu->dropout.

BN works better with larger batch sizes, and since it normalizes over batches, it is undefined for batch size of 1, and has implementation problems for variable batch size.

TLDR:
- BN averages over the batch axis for each feature
- BN is supposed to bring the statistics of the features in a batch to the same place
- BN is batch-size dependent, so works better with larger batches and can't work with batch size of one

### What is the purpose of regularization, and describe some regularization methods in machine learning.

Regularization, most generally, is the process of adding information (or reducing model capacity) to make a problem more well-posed. This is to prevent overfitting, and reduce generalization error. Regularization makes the fitting or modeling you're doing more smooth -- for discrimination, this means making the function you're approximating more locally smooth, and for generation, this can also mean making the latent space more locally smooth. So, all of this makes the function or latent space more "well behaved", for the optimizer.

Learning a smooth function means that your model hasn't simply memorized the training data, and it means that points in a neighbourhood around a feature point has some meaningful relationship to the feature point.

In the extreme case, where a model is extremely overfit, the model will be a good fit to noise in the input data, and therefore useless at generalizing.

In the context of preventing overfitting, there are many examples of regularization in deep learning -- many things are said to have a "regularizing effect":
There is the classic addition of a weight decay term to the loss
Adding more data is regularizing, since more data means your model is less able to overfit the data
Reducing the fitting capacity of the model obviously has a regularizing effect
Data augmentation is like adding more data, but you're adding noise to your existing data
Certain layers have strong or weak regularizing effects. For example, dropout regularizes by preventing overreliance on any particular neuron, and layers like 
Early stopping is a form of regularization that prevents the optimizer from overfitting as the optimizer descends into a deep minimum in the loss function
The stochasticness and randomness of mini-batch gradient descent is said to have a regularizing effect

TLDR:
- Regularization tries to reduce overfitting by making the function and/or feature space more smooth, or regular
- Lots of regularizing effects, like weight decay, dropout, data augmentation

### Describe the Adaptive gradient (Adagrad), Adaptive delta (Adadelta), Root Mean Squared Propagation (RMSProp) and Adaptive Momentum (Adam) optimizers.

They are all optimization strategies that computes different updates for each weight, and also tries to be adaptive with update sizes from step to step.

Adagrad attempts to expand upon regular gradient descent by adaptively modifying the learning rate applied to each weight based on previously accumulated gradients of that weight. The idea is that not all features (and therefore not all weights) need to be updated equally -- rarely occurring features (and their associated weights) should have larger updates than frequently occurring features. Adagrad accomplishes this by dividing each weight update by something proportional to its accumulated past gradients. This, ideally, removes the need to tune the learning rate, since it adapts. However, in practice since the gradient only accumulates, the update size can only decrease, which is a problem.

Adadelta attempts to fix the monotonically decreasing update size problem of Adagrad by limiting how many steps back the gradient is accumulated (generally just two steps back I believe). The implementation has some approximation tricks, but this isn't super important.

RMSProp is closely related to Adadelta, but instead of a regular average of previous gradients, it uses an exponentially decaying average of previous gradients.

Adam does what Adadelta does, but also keeps a running momentum.

TLDR:
- All are optimizers that try to be adaptive per weight and adaptive per time step by looking at previously calculated updates

### What is layer normalization and how does it differ from batch normalization?

Layer normalization is similar to batch normalization in that it computes a mean and variance for a set of features, normalizes the features, and then learns a new affine transformation for the result. Unlike batch normalization, which normalizes over the batch axis for each feature point, layer normalization normalizes over the feature axis (or axes), and so each feature is normalized independently of the rest of the batch.

This means that LN doesn't depend on batch size like BN.

LN learns a transform of the form gamma^T x + beta after x is normalized, so there are 2 * size(x) learnable parameters for layer norm.

TLDR:
- LN averages over the feature dimension instead of the batch dimension
- No need to keep running average, no dependence on batch size

### What is gradient descent?

Gradient descent (or ascent) is an iterative minimum (or maximum) finding algorithm where the gradient of a function is approximated at a point, and then a step is taken in the direction of the negative (or positive) gradient, proportional to a learning rate.

TLDR:
- Iterative first order optimization method

### What is the difference between a generative and a discriminative model? Specifically, describe the difference between how Naive Bayes and logistic regression work.

Generative models model the full joint probability distribution, whereas discriminative models model specific conditional probabilities. A good example is the difference between Naive Bayes and logistic regression.

Naive Bayes models the joint distribution function by making the approximation that all upstream random variables are independent, i.e. P(A, B, C) = P(C|A, B)P(B|A)P(A) is approximated to be P(A)P(B|A)P(C|A). So inference, i.e. P(A|B, C) can be done via conditionalizing or marginalizing over the joint distribution. Logistic regression, on the other hand, directly models the conditional probability P(A|B, C) by giving it a specific functional form, i.e. assigning the log-odds (p/1-p) to be a linear function of the predictors.

In the parlance of deep learning, generative models often specifically refer to models which allow generation of new data by learning the distribution from which features originated.

TLDR:
- Generative models attempt to model the joint PDF, whereas discriminative models attempt to directly give the conditional probability a functional form

### Explain the bias-variance tradeoff.

The bias-variance tradeoff is pretty much the underfitting-overfitting tradeoff. Looking from the model side, complex models typically show low bias, high variance behaviour: they fit the training data TOO well (low bias), but because they also fit the noise in the training data, they have high variance, so they have greater generalization error. Simple models have low variance because they don't have a lot of parameters, but high bias error, because they fit the original data less well.

Good models need to strike a balance between bias error and variance error to make good predictions. Regularization can also make low bias high variance models work better by not allowing overfitting in various ways.

A low complexity model will have a high bias and low variance; while it has low expressive power leading to high bias, it is also very simple, so it has very predictable performance leading to a low variance. Conversely, a complex model will have a lower bias since it has more expressiveness, but will have a higher variance as there are more parameters to tune based on the sample training data.

TLDR:
- Same as underfitting-overfitting tradeoff, high bias comes from simpler models and means underfitting, high variance comes from complex models and means overfitting

### What is the curse of dimensionality and how do you combat it?

In a very general sense, the curse of dimensionality is the idea that, as the dimensions of the feature space grows (i.e. we add more features), the amount of data needed to generalize accurately increases exponentially. Equivalently, as the number of dimensions grows, the existing data becomes more sparse. Equivalently, as the number of dimensions grows, the space that each feature point takes up grows exponentially. This is bad because it leads to overfitting.

For example, think of a binary classification problem with two feature dimensions which capture the classes really well, plus a billion feature dimensions which are just noise and don't correlate with class at all. WIth the two feature case, finding a decision boundary should be easy, but with a billion and two features, all of a sudden every feature vector becomes roughly equally distant, and the feature space becomes extremely sparse.

There are various ways of combating the curse of dimensionality -- in classic machine learning, carefully selecting the features or using a dimensionality reduction technique like PCA to find the best feature subspace.

TLDR:
- The more features there are, the more data is needed to generalize adequately
- Equivalently, the more feature dimensions there are, the less volume a particular point takes up, and so the sparser feature space becomes
- Can combat via manual feature selection, or a dimensionality reduction technique like PCA

### Explain Principle Component Analysis (PCA).

PCA is a dimensionality reduction algorithm where a subspace is found for the data, usually with much fewer dimensions than the original data, and where the basis vectors of the subspace point in the directions of maximum variance of the original data. This way, we can try to capture most of the information in the original data by projecting it down to the PCA subspace.

TLDR:
- Dimensionality reduction method that ranks dimensions by amount of variance the data has along that dimension

### What are vanishing and exploding gradients, and how do we avoid them?

Vanishing gradients: With backpropagation, as the gradient gets propagated back, it gets multiplied by weights and derivatives of activations along the way. If enough of these are less than 1, the gradient becomes small exponentially fast, and in the worst case becomes so small that it's no longer possible to learn. 

Exploding gradients: The opposite of vanishing gradients. If enough activations and weights are greater than 1, your gradients can become so large that the optimizer becomes unstable.

Some models and model features attempt to deal with vanishing/exploding gradients:

- RelU activation is better than activations like sigmoid and tanh because its derivative can only be 1 or 0, so when it's active, it doesn't cause exploding or vanishing.

- When using activations like sigmoid, batch normalization layers can help with vanishing gradients because they can recenter the activations of the previous layer to a place where the activation has larger gradients.

- Residual connections help with vanishing gradients because the skip-connection allows errors to propagate directly, and residual blocks learn on top of an identity mapping, there is always a path for the gradient to flow which doesn't cause them to vanish or explode.

- LSTMs do better with vanishing/exploding gradient problems than RNNs because the cell state has an additive dependence on its dependent variables instead of a purely multiplicative one like in RNNs, and the gating functions (especially the forget gate) allows the network to decide how much the gradient vanishes, and so the gradient doesn't need to necessarily always get larger or always get smaller with each cycle.

And some training tricks can be used to solve exploding gradients:

- Gradient clipping thresholds the gradient, making exploding gradients impossible, but if the gradients were going to explode before clipping, something is probably still wrong.

- Using smaller batch sizes makes the maximum accumulated gradient per batch smaller.

TLDR:
- Due to the multiplicative nature of the chain rule, the gradient, as it propagates back through deep models, can sometimes becoming too small or too large
- Some model architectures deal with this, e.g. LSTM tries to fix vanishing gradient problem of RNNs, residual connections try to fix vanishing gradient problem of vgg-like networks
- Some layers like batch norm and activations like relu do better against vanishing/exploding gradients

### What is the significance behind using residual connections in ResNets?

Residual connections were an attempt to address the degradation problem with deep networks -- the counterintuitive fact that adding more layers often meant worse performance. Residual blocks add a skip, or residual connection which makes learning the identity transformation trivial. One way of thinking about it is that residual blocks have learn the difference between the output and the input rather than a direct mapping between the input and the output, so the part of the residual block with weights learns via refinement instead of learning a transformation from scratch -- if no refinement is needed, the skip-connection is everything that's needed, and the weighted layers can gradually adjust their weights towards zero.

The residual connection idea is THE breakthrough for convnets, pretty much every modern image and video model uses residual connections, and ResNets have spawned a whole whack of children with variations on the idea, like ResNeXt, DenseNet, etc.

TLDR:
- Residual connections combat the problem where adding more layers makes networks harder to train
- A residual block can trivially learn the identity mapping due to the skip connection, so the weighted part of the block learns a residual on top of the identity mapping instead of having to learn the optimal transformation itself

### Why is RelU used over Sigmoid as the main activation in modern neural networks?

The main reason is that sigmoid activation is susceptible to the vanishing gradient problem, since its derivative is always less than 1, and goes to zero if the input is large or small, so when we chain a lot of them together in the model, the gradient can become very small. 

Another reason is that RelU is simpler and faster to compute.

The main reason though, is probably just that empirically, it was found that RelU was fast and worked well enough for most applications, so it was widely adopted as a default.

TLDR:
- Historically, sigmoid suffered from vanishing gradients because its active region was small and its gradients were way below 1
- RelU doesn't have the vanishing problem of sigmoid/tanh, and is simpler to compute
- RelU came in and just sort of worked, and became the default. Was a right time/right place kind of thing.

### Why are convolutional layers used for images rather than just FC layers?

Convolutional layers preserve and encode positional information, whereas FC layers don't (or at least don't strongly). Secondly, convolutional layers use weight sharing, so you have a lot fewer weights than if every pixel was put through an FC layer. Finally, because of the sliding window nature of convolutions, it imparts the model with some translation-invariance.

There's also some neuroscience arguments about why convolutional layers are used, as they are supposed to mimic the mammalian visual cortex.

TLDR:
- Conv layers account for and encode spatial structure, and also add some spatial invariance
- Conv layers share weights, so they're much fewer weights than an FC of the equivalent feature map

### Why do we have max-pooling in convolutional neural networks?

Pooling is the main operation to reduce feature size, and doesn't add any new parameters. It's also said to allow some more translation-invariance, since only the maximum activation in a block of activations is allowed through.

TLDR:
- For feature map size reduction, and to endow some translational invariance

### Why do ensembles typically have higher accuracies than individual models?

The thinking is that, when using different model types and/or different data to train the models, each model makes a different type of error, so the different models should be able to compensate for each other in some sense.

TLDR:
- Different models make different errors, and so should be able to compensate for each other

### What is an imbalanced dataset, and what are some ways to deal with data imbalance?

An imbalanced dataset is one where some data types appear more frequently than others, and happens very often with real data, and with some use-cases like object detection.

Ways to deal with imbalanced data can either happen at the data end or at the model end. At the data end, obviously the best solution, if possible, is to just collect more data. Otherwise, we can oversample minority classes or undersample majority classes, or do some kind of data generation to make synthetic data. At the model end, we can use losses and/or metrics that work better for imbalanced data, like focal loss, or precision/recall/F1 score instead of accuracy. The choice of metric depends on whether you can tolerate false positives or false negatives, etc.

TLDR:
- Can deal with data imbalance at the data end (getting more data, sampling the data differently, generating synthetic data)
- Can deal with data imbalance at the model end (specialized losses or metrics)

### What is data augmentation, and what are some examples of data augmentation?

Data augmentation is the process of modifying existing data by adding noise or some kind of transform, without changing the target. Data augmentation regularizes the model by making it more robust to noise. Some examples for images are affine transforms, mirroring, modifying brightness, contrast, hue, saturation, adding noise, blurring, etc.

TLDR:
- Data augmentation is adding noise or a transform to input data without changing the target
- Data augmentation regularizes the model, making it more robust to noise and making the modeled function or space more smooth

### Explain the receiver operating characteristic (ROC) and how to interpret it.

The ROC is a plot of the model's true positive rate (TPR) vs. its false positive rate (FPR), points are generated by varying the probability threshold for counting a result as a positive. When the threshold is 0, everything counts as a positive (so the TPR and FPR can both be made 1), and when the threshold is 1, everything counts as a negative (so the TPR and FPR can both be made 0).

There are various metrics that can be derived from the ROC, one is the area under curve (AUC), which gives the probability that the model will rank a randomly chosen positive sample as having a higher probability than a randomly chosen negative one, and so is used to compare models.

### What is transfer learning?

Transfer learning, broadly, is when a model trained on one task is used as the starting point for training on a related task.

In CV, this usually means using the weights from a model trained on a general dataset and finetuning it for a smaller, more specific dataset. The idea is that the feature extractor learned by the lower layers allows the model to generalize better than the feature extractor trained on only a small, specific dataset.

### Would it be preferable to use the entire batch at once for gradient descent if we could?

The loss functions we deal with in deep learning are typically non-convex, and we are more likely to reach an undesirable minimum with full-batch gradient descent. The minimum we want should have a small loss, but should also be "smooth", or low curvature, around the minimum. Large batch sizes have been shown to produce "sharper" minima. The gradient computed from mini-batch gradient descent can be thought of as the full-batch gradient plus noise, which is thought to push the optimizer out of "sharp" minima and into "flat" minima where noise will not push the optimizer out of the minimum.

That's the optimization side of the coin. There's also the parallelization/computational side of the coin, where larger batch sizes are easier to parallelize.

### What are supervised, unsupervised, semi-supervised, self-supervised, multi-instance learning, and reinforcement learning?

Supervised: All training samples are individually labeled, e.g. classification
Unsupervised: No labels, try to learn structure, e.g. clustering, representation learning
Semi-supervised: Some training samples are labeled, can use pretext tasks on unlabeled data to help train with supervised data
Self-supervised: Labels are automatically generated somehow, then turns into a supervised problem
Multi-instance learning: Instead of every feature vector having a label, we have labeled bags of feature vectors, but not labels of the individual features. To me, this is kind of like a bag-of-words/bag-of-features approach.
Reinforcement learning: Reinforcement learning trains an agent which takes a series of discrete steps. At each step, the agent receives observations from its environment, and then chooses an action from a set of possible actions. The agent is trained to maximize a reward function (or equivalently, minimize a cost function). The agent should learn how to lose short-term rewards for larger long-term rewards.

### What are nonparametric models? What is nonparametric learning?

Nonparametric models don't make strong assumptions about the form of the function they're learning, so there's no set number of weights, etc. They're more flexible, but are often more complex and need more data.

kNN is an example of a nonparametric model.

### What is empirical risk minimization?

Empirical risk minimization refers to the fact that a learning algorithm only has access to samples of the true input domain, so the error that we're minimizing is referred to as empirical, since we're not minimizing the true error, as we would be if we had access to the entire input domain.

I think, mathematically, ERM gives an upper bound to the true error based on the empirical error.

### What is representation learning? Why is it useful?

Representation learning is any method which extracts an appropriate and meaningful representation of samples, in order to accomplish a machine learning task. So the goal of representation learning is to map raw data into a form (usually a feature vector) that allows something like classification. This can be done with supervised (final layer before classification can be used as a representation) or unsupervised (autoencoders) methods.

For example, with deep networks for classification, the network learns a nonlinear transformation which maps the input to an output space where the classes are linearly separable, and we can use a softmax classifier to classify the samples. 

Another example is in facial recognition, where representation learning can not only do dimensionality reduction, but also endow the feature space with nice properties -- for example, some measure of distance could be made to be meaningful in the feature space, which is not true for all feature spaces.

Deep networks are so powerful because they can learn abstract inner representations through hidden layers, and by learning multiple successive abstractions, they are able to learn input-output mappings which can map very complex inputs to an output space that has nice properties.

What are the reasons for choosing a deep model as opposed to a shallow model?

The idea is that, for the same number of weights, a network with more layers is better able to learn abstract concepts, or an abstract inner representations of the input. In a deep model, shallow layers are thought to learn basic features, whereas deeper layers are thought to learn combinations and relationships between lower level features, and so on, until the deepest layers learn very abstract concepts.

Thus, a shallow network would need many more weights to learn the same kind of abstract decision making that a deep network can make.

The classic example with a deep network is that the first shallow layers learn weights which filter for different types of edges and textures, intermediate layers can then use the presence of those edges and textures to learn about the presence of shapes, and the final, deep layers can use the presence of shapes to learn about the presence of things like eyes and mouths, etc.

### What is the k-nearest neighbours algorithm? What are its disadvantages?

Classical kNN is an algorithm where training means just memorizing the training data, and makes predictions based on the k nearest neighbours to an unknown sample.

kNN is O(1) training, since we just put all of the training samples into memory, but has a high memory cost, since all of the training data needs to be part of the model. Inference is also slow because nearest neighbour search is at least O(N*feature dimensions) (with quickselect). Models that are fast to train but slow to infer are generally not desirable.

### What is the Vapnis-Chervonenkis (VC) Dimension?

The VC dimension of a classifier is defined as the number of feature points where, for any particular arrangement of the feature points in feature space, the classifier is able to shatter the points. To shatter means that the classifier is able to perfectly partition the points for all possible assignments of classes. Thus, if a classifier is able to shatter any arrangement of feature points for a particular N, then N is a lower bound for the VC dimension of a classifier, and if the classifier is unable to shatter all arrangements of feature points for a particular N, then that N is an upper bound for the VC dimension of a classifier.

Basically, the VC dimension correlates with the complexity and expressiveness of a model.
