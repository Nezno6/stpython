from text_alignment import drawing_logo

def test_drawing_logo():
    assert drawing_logo(5) =="""    H    \n   HHH   \n  HHHHH  \n HHHHHHH \nHHHHHHHHH\n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHHHHHHHHHHHHHHHHHHHHHH   \n  HHHHHHHHHHHHHHHHHHHHHHHHH   \n  HHHHHHHHHHHHHHHHHHHHHHHHH   \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n  HHHHH               HHHHH             \n                    HHHHHHHHH \n                     HHHHHHH  \n                      HHHHH   \n                       HHH    \n                        H     """
