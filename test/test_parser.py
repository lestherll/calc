import pytest

from expr_calc.calc import Calc
from expr_calc.token import Token, TokenType
from expr_calc.tree import Tree


@pytest.mark.parametrize("source, expected_shunted_tokens", [
    ("1 + 2", Tree(
        Token(TokenType.B_ADD, "+"), [
            Tree(Token(TokenType.NUMBER, 1)),
            Tree(Token(TokenType.NUMBER, 2))
        ])),
    ("-10 ^ 2", Tree(
        Token(TokenType.U_MIN, "-"), [
            Tree(Token(TokenType.B_EXP, "^"), [
                Tree(Token(TokenType.NUMBER, 10)),
                Tree(Token(TokenType.NUMBER, 2)),
            ]),
        ])),
    ("-1 ^ -2", Tree(
        Token(TokenType.U_MIN, "-"), [
            Tree(Token(TokenType.B_EXP, "^"), [
                Tree(Token(TokenType.NUMBER, 1)),
                Tree(Token(TokenType.U_MIN, "-"), [
                    Tree(Token(TokenType.NUMBER, 2)),
                ]),
            ]),
        ])),
    ("(-1) ^ -2", Tree(
        Token(TokenType.B_EXP, "^"), [
            Tree(Token(TokenType.U_MIN, "-"), [
                Tree(Token(TokenType.NUMBER, 1)),
            ]),
            Tree(Token(TokenType.U_MIN, "-"), [
                Tree(Token(TokenType.NUMBER, 2)),
            ]),
        ])),
    ("-2 ^ (2/3)", Tree(
        Token(TokenType.U_MIN, "-"), [
            Tree(Token(TokenType.B_EXP, "^"), [
                Tree(Token(TokenType.NUMBER, 2)),
                Tree(Token(TokenType.B_DIV, "/"), [
                    Tree(Token(TokenType.NUMBER, 2)),
                    Tree(Token(TokenType.NUMBER, 3)),
                ]),
            ]),
        ]))
])
def test_parse(source, expected_shunted_tokens):
    calc: Calc = Calc()
    assert calc.parse(source) == expected_shunted_tokens
