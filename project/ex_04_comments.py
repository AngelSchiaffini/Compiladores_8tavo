from delta import Compiler, Phase


source = """
    /**/
    1
    // A line comment.

        +

        /* 
        A block
        comment.
        */
    2
    """

c = Compiler('program')
c.realize(source)
print(c.result)
