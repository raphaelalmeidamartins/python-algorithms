import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(2, 1)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("anyt message", "invalid type key")

    assert encrypt_message("AABBCC", -1) == "CCBBAA"

    assert encrypt_message("AABBCC", 3) == "BAA_CCB"

    assert encrypt_message("ABBCCA", 4) == "AC_CBBA"
