from project import Model
from project import validate_answer
from project import recommended_model
from project import ranking


def main():
    test_validate_answer()
    test_recommended_model()
    test_ranking()


def test_validate_answer():
    assert validate_answer("Oui") == False
    assert validate_answer("Y") == False
    assert validate_answer("yes") == True
    assert validate_answer("Yes") == False


def test_recommended_model():
    test_models = [Model("model_1"), Model("model_2"), Model("model_3")]

    test_models[0].score = 2
    test_models[1].score = 1
    test_models[2].score = 3

    result = recommended_model(test_models)
    assert result.name == "model_3"

def test_ranking():
    test_models = [Model("model_1"), Model("model_2"), Model("model_3")]

    test_models[0].score = 2
    test_models[1].score = 1
    test_models[2].score = 3

    sorted_models = ranking(test_models)

    assert sorted_models[0].name == "model_3"
    assert sorted_models[1].name == "model_1"
    assert sorted_models[2].name == "model_2"


if __name__ == "__main__":
    main()
