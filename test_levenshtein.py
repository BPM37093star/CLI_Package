from levenshtein_base import levenshtein


def test_equal_weights():
    s1 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'library', 'stood', 'as', 'a', 'center', 'of', 'learning', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'of', 'the', 'past', 'to', 'those', 'who', 'listened', 'closely'] 
    s2 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'ancient', 'library', 'stood', 'as', 'a', 'beacon', 'of', 'knowledge', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'from', 'the', 'past', 'to', 'those', 'who', 'listened']

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=1)
    assert distance == 5

    s1 = "In the heart of the bustling city, the library stood as a center of learning, its walls lined with books that whispered secrets of the past to those who listened closely."
    s2 = "In the heart of the bustling city, the ancient library stood as a beacon of knowledge, its walls lined with books that whispered secrets from the past to those who listened"

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=1)
    assert distance == 33


def test_expensive_substitution():
    s1 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'library', 'stood', 'as', 'a', 'center', 'of', 'learning', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'of', 'the', 'past', 'to', 'those', 'who', 'listened', 'closely'] 
    s2 = ['In', 'the', 'heart', 'of', 'the', 'bustling', 'city', 'the', 'ancient', 'library', 'stood', 'as', 'a', 'beacon', 'of', 'knowledge', 'its', 'walls', 'lined', 'with', 'books', 'that', 'whispered', 'secrets', 'from', 'the', 'past', 'to', 'those', 'who', 'listened']

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=12)
    assert distance == 8

    s1 = "In the heart of the bustling city, the library stood as a center of learning, its walls lined with books that whispered secrets of the past to those who listened closely."
    s2 = "In the heart of the bustling city, the ancient library stood as a beacon of knowledge, its walls lined with books that whispered secrets from the past to those who listened"

    distance = levenshtein(s1, s2, insertion_cost=1,
                            deletion_cost=1, substitution_cost=12)
    assert distance == 40


def test_cheap_substitution():
    s1 = "Today, we're excited to launch our latest feature, designed to enhance user experience across our platform."
    s2 = "Today, we are excited to announce our latest feature, aimed at enhancing the user experience across the platform."

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=0.5)
    assert distance == 17

    s1 = ['Today', "we're", 'excited', 'to', 'launch', 'our', 'latest', 'feature', 'designed', 'to', 'enhance', 'user', 'experience', 'across', 'our', 'platform'] 
    s2 = ['Today', 'we', 'are', 'excited', 'to', 'announce', 'our', 'latest', 'feature', 'aimed', 'at', 'enhancing', 'the', 'user', 'experience', 'across', 'the', 'platform']

    distance = levenshtein(s1, s2, insertion_cost=1,
                           deletion_cost=1, substitution_cost=0.5)
    assert distance == 5

def test_empty_strings():
    assert levenshtein("", "") == 0
    assert levenshtein("", "abc", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 3
    assert levenshtein("abc", "", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 3

def test_identical_strings():
    assert levenshtein("abc", "abc", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 0
    assert levenshtein(["hello", "world"], ["hello", "world"], insertion_cost=1, deletion_cost=1, substitution_cost=1) == 0


def test_substitution_cost_effect():
    # prefer substitution
    assert levenshtein("abc", "adc", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 1
    # prefer insert + delete over substitution
    assert levenshtein("abc", "adc", insertion_cost=1, deletion_cost=1, substitution_cost=3) == 2

def test_special_unicode():
    assert levenshtein("你好", "您好", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 1
    assert levenshtein("hello!", "hello?", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 1

def test_insertion_deletion_only():
    assert levenshtein("abc", "abcd", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 1
    assert levenshtein("abc", "aXbc", insertion_cost=1, deletion_cost=1, substitution_cost=1) == 1
    assert levenshtein(["a", "b", "c"], ["a", "x", "b", "c"], insertion_cost=1, deletion_cost=1, substitution_cost=1) == 1
