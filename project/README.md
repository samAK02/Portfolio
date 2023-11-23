# Machine Learning Model Selector
    #### Video Demo:  <https://www.youtube.com/watch?v=S7GTbiO_3Ac>
    #### Description:

The provided code aims to assist users in choosing the most suitable machine learning model for their specific needs.
Selecting the right model is crucial but complex, as it requires considering factors like computational resources and data characteristics.
The program achieves this by using a well-designed questionnaire to gather user preferences and data details. It then evaluates these inputs using a point-based system rooted in machine learning fundamentals and guided by a scientific article.
This approach minimizes the risk of choosing inappropriate models, helping users make informed decisions efficiently.


# **Technical Overview:**


## Model Class:

-The Model class represents machine learning models.
-Each model instance contains a name and an initial score set to 0.
-This class is essential for storing and managing model data.


## Question Class:

-The Question class plays a key role in guiding users through the model selection process.
-It constructs questions based on user preferences and assigns models to "yes" or "no" responses.
-The class encapsulates methods like get_input, get_valid_answer, and ask for streamlined interaction.


## Function Usage:
-get_input Method (Inside Question Class)
-This method prompts the user for input, converting it to lowercase and stripping whitespace.
-It fosters reusable and consistent input handling throughout the project.

get_valid_answer Method (Inside Question Class):

-This method ensures valid "yes" or "no" responses from users.
-It uses get_input and enforces valid answers, promoting user-friendly interaction.

ask Method (Inside Question Class):

-The ask method prompts users with a question using get_valid_answer.
-It updates model scores based on user responses.
-This function is pivotal for accumulating user preferences.

questions_creation Function:

-The questions_creation function employs the yield statement for efficient, on-demand question generation.
-It associates questions with preferred and non-preferred models.
-This approach enhances code flexibility and readability.

validate_answer Function:

-The validate_answer function utilizes regular expressions to validate user responses.
-It safeguards against incorrect inputs, ensuring reliable interactions.

recommended_model Function:

-The recommended_model function identifies the model with the highest score.
-It enables the project to deliver a data-driven recommendation.

ranking Function:

-The ranking function sorts models by their scores in descending order.
-It prepares a ranked list of models for users to assess.


## Type Hints:
-The typing module and type hints enhance code clarity.
-Type annotations like List[Model] and str provide insights into function expectations.
-These hints bolster code comprehension and prevent type-related errors.
