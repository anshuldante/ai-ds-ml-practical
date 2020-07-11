# Recommendations

## The Basics

* A recommendation system is a computer program that helps a user discover product or content by predicting the user's rating for each item and then showing them the items they'd rate highly.
* Uses:
  * Rank products by user preferences
  * Product similarity
  * User similarity
  * Shopping (products, books eyc.), Social Media, music recommendations, movie/tv content recommendations.
  * Dating apps, Banking products, insurance products.

## Ways of Making Recommendations

* **Content Based Recommendations**: use knowledge about each product to recommend new products.
  * The advantage is that is works even when a product has no reviews.
  * The disadvantage is that descriptive data is required for every product that you want to recommend, so it's difficult to implement for a large product database.
* **Collaborative Filtering**: making recommendations only based on how users rated have rated products in the past, not based on anything about the product.
  * The advantage is that you don't need any knowledge of the products.
  * The disadvantages:
    * Can't recommend products if we don't have reviews.
    * Difficult to make good recommendations for brand-new users.
    * Tends to favor popular products with lots of reviews.

## Building the Framework for the Recommendation System

* We'll assume that user ratings are a reflection of how much a movie appeals to that user's unique set of interests.
* We'll follow the following steps to calculate a User's ratings.
  * Model how much a movie appeals to every possible interest.
  * Model the user's interests.
  * User-rating: measure how well the user's interests match the movie attributes.
* The attributes we will use to model a movie's appeal and a user's interests are:
  * Action appeal rating
  * Drama appeal rating
  * Romance appeal rating
  * Art-house appeal rating
  * Crowd-pleaser appeal rating
* We'll multiply user's interests rating by the corresponding movie appeal ratings to calculate a score and then recommend the movie with the highest score.
* Finally, the score calculation turns out to be a matrix multiplication for each user's interest * appeals for all movies.
* In conclusion, we can predict how much a user will like a movie, if we have appeal/interest ratings for every user and movie.

## Collaborative Filtering with Matrix Factorization

* We'll use the following process to build the movie appeal matrix:
  * Create a matrix of known user reviews.
  * Factor out a U (user attribute) matrix and an M (movie attribute) matrix from the known reviews.
  * Multiply the U and M matrices we found to get review scores for every user and every movie.
  * Since we won't know what the values in teh matrices represent (drama/comedy etc.) the vectors are called Latent (hidden) vectors.
* After generating the movie rating matrix, we recommend the users movies with the highest ratings which they haven't watched yet.
* If the a user rates a movie we recommend, we put the actual movie rating in and recalculate the matrix.
* For finding the matrices, we have the **Matrix Factorization Problem**
  * It assumes that there's a large matrix of numbers.
  * We want to satisfy the rule: Small matrix 1 x Small matrix 2 = Large matrix
  * The goal is to find Small Matrices 1 & 2 that satisfy the above equation.
* Standard matrix factorization approaches won't work because the matrix we want to factor has some missing values.
* Instead, we'll estimate the matrix factorization using an iterative algorithm.
* Here's what the algorithms looks like:
  * Set all elements in U and M to random numbers, the movie rating matrix will now result in random numbers
  * Create a **cost function** that checks how far off **U x M** currently is from equaling the known values of the Movie Ratings matrix.
  * Using a numerical optimization algorithm, tweak the numbers i U and M a little a a time.
  * The goal is to get the **cost function** a little closer to zero with every iteration.
  * We'll use **SciPy's fmin_cg()** optimization function to find the minimum cost. It searches for inputs that make the function return the minimum output.
  * The **U** and **M** values we find will be the estimates: **U x M ~ Movie Ratings**.
  * Even after hitting the iteration.min_cost limit, we will not get the exact result matrix, but it'll be pretty close.
* **Usage of Latent Vectors**
  * Especially useful for brand-new users who haven't reviewed anything yet.
  * Show more products **similar** to the current product.
* To suggest movies similar to the user has watched:
  * We use the matrices to find the movie which is the closest rating set to selected one.
  * We first find the features for the selected movie.
  * Then we find the difference, get the absolute values for the differences and find the sums.
  * On sorting the results, we get the movies that are most similar to the selected one in decreasing order.

## Testing Our System

* Finding the list of recommendations for a user that has reviewed some movies:
  * We load the row with the predicted ratings for the user and skip the ones he's already watched.

* ### Regularization

  * Our current system can run into the problem of overfitting. For ex. If Movie-1 is a horror-comedy and Movie-2 is a serious horror movie, a good recommendations system should keep them in separate groups, but an overfit system can concentrate on the horror aspect and keep them in the same bucket.
    * To avoid this, we can use **regularization**.
    * It limits how much weight to place on a single attribute when modeling users and products. The higher the regularization amount, the less weight we can put on any single attribute.
    * We've been using 0.1 for the example data set.
    * But for a larger data set, larger numbers (1.0, 10.0 etc.) are used.
    * Finding the right value requires  experimentation.
    * We should try out different regularization values to find the best fit.

* ## Measuring Recommendation Accuracy

  * **RMSE (Root-Mean-Square Error)**
    * RMSE is a measurement of the difference between the user's real rating and the rating we predicted.
    * The lower the RMSE, the more accurate the model is. An RMSE of 0 means we have a perfect model, and 1 means our prediction is off by 1 star.
    * Split the review data into two groups: training and testing data.
    * Do Matrix factorization only on the training data.
    * Check accuracy using the withheld testing data.
  * Our training RMSe turns out to be 0.25 which means that our basic algorithm is working.
  * But the testing RMSE is 1.2 which means that the system is off by 1+ star.
  * We can play around with the regularization values to get better results.

## Using the Recommendation System in a Real World Program

* We'll save **U, M and U x M** so that we don't have to perform the slow process of recalculating the matrices every time.
* Ways to handle First-Time users:
  * Do not make any recommendations.
  * Recommend based on product similarity
  * Recommend based on overall ratings
    * This can work because there are some movies that have a better average rating overall.
* We subtract the average rating of a movie from all of its ratings and then calculate U and M.
* Then we add the averages back to M, now whenever we need to make a recommendation, we just list out the top movies using the new dataset.

Can try out the learnings on the MovieLens dataset.
