# Patrick 05.12.2025.

from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did your first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses