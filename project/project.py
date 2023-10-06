import re
import matplotlib.pyplot as plt
from typing import List


class Model:
    def __init__(self, name: str):
        self.name = name
        self.score = 0


class Question:
    def __init__(self, text: str, yes_models: List[Model], no_models: List[Model]):
        self.text = text
        self.yes_models = yes_models
        self.no_models = no_models

    def get_input(self, message) -> str:
        return input(message).lower().strip()

    def get_valid_answer(self, message: str) -> str:
        answer = self.get_input(message)
        while answer not in ["yes", "no"]:
            print('Please, answer "Yes" or "No"')
            answer = self.get_input(message)
        return answer

    def ask(self) -> None:
        answer = self.get_valid_answer(f"{self.text} (yes/no): ")
        if answer == "yes":
            for model in self.yes_models:
                model.score += 1
        elif answer == "no":
            for model in self.no_models:
                model.score += 1
        return answer


def main():
    models = [
        Model("Decision Tree"),
        Model("Neural Networks"),
        Model("Naïve Bayes"),
        Model("k-NN"),
        Model("SVM"),
        Model("Rule-learners"),
    ]

    for question in questions_creation(models):
        question.ask()

    print()

    best_model = recommended_model(models)
    print(f'the best model is: "{best_model.name}"')

    print()


    sorted_models = ranking(models)

    print("models froms best adapted to worst adapted:\n ")

    names = [model.name for model in sorted_models ]
    scores = [model.score for model in sorted_models]

    plt.bar(names, scores)

    plt.xticks(rotation = 45)
    plt.tick_params(axis='x', labelsize=8)
    plt.subplots_adjust(bottom=0.2, top=0.8)
    plt.title("Score of Models")
    plt.savefig("models_score.png")


def questions_creation(models: List[Model]) -> List[Question]:
    yield Question(
        "Do you care about the accuracy in general?",
        [models[1], models[4]],
        [models[0], models[2], models[3], models[5]],
    )

    yield Question(
        "Is the Speed of classification an important factor to you?",
        [models[0], models[1], models[2], models[4], models[5]],
        [models[3]],
    )

    yield Question(
        "Do you want a model with a tolerance of missing values?",
        [models[0], models[2]],
        [models[1], models[3], models[4], models[5]],
    )

    yield Question(
        "Do you want a model with a tolerance of irrevelant attributes?",
        [models[0], models[4]],
        [models[1], models[2], models[3], models[5]],
    )

    yield Question(
        "Do you want a model with a tolerance of redundant attributes?",
        [models[4]],
        [models[0], models[1], models[2], models[3], models[5]],
    )

    yield Question(
        "Do you want a model with a tolerance of high interdependent attributes?",
        [models[1], models[4]],
        [models[0], models[2], models[3], models[5]],
    )

    yield Question(
        "Do you want a model with a tolerance of noise?",
        [models[2]],
        [models[0], models[1], models[3], models[4], models[5]],
    )

    yield Question(
        "Do you want a model that deals with the danger of overfitting?",
        [models[2], models[3]],
        [models[0], models[1], models[4], models[5]],
    )

    yield Question(
        "Do you want a model that attempts for incremental learning?",
        [models[1], models[2], models[3]],
        [models[0], models[4], models[5]],
    )

    yield Question(
        "Do you want a model with explanation ability and transparancy of knowledge?",
        [models[0], models[2], models[5]],
        [models[1], models[3], models[4]],
    )

    yield Question(
        "Do you want a model with parameter handling?",
        [models[0], models[2], models[3], models[5]],
        [models[1], models[4]],
    )


def validate_answer(answer: str) -> bool:
    return re.match(r"^(yes|no)$", answer) is not None


def recommended_model(models):
    best_model = max(models, key=lambda x: x.score)
    return best_model


def ranking(models):
    return sorted(models, key=lambda x: x.score, reverse=True)


if __name__ == "__main__":
    main()
