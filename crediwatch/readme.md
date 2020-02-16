#CrediWatch

##Architecture Overview

```buildoutcfg
                                             User interface makes
      +----------------+  +--------------->  use of stacks like JS,Bootstrap
      |                |
      |                |
      | User Interface |                          +------------------------------+
      |                +<----------+              |                              |
      |                |           |              |                              |
      |                |           |              |                              |
      |                |           |              |                              |
      |                |           |              |                              |
      +----------------+           |              |   CrediWatch Flask server    +<-------+       +----------------+
                                   +--------------->                             |        |       |                |
                                                  |                              |        +------>+                |
                                                  |                              |                |    Mongo DB    |
                                                  |                              |                |                |
                                                  |  python flask server         |                |                |
                                                  |  python version-3.7          |                |                |
                                                  |                              |                +----------------+
                                                  |                              |
                                                  +------------------------------+

                                                                                                   DataBase layer
          Client layer                                   Middle-ware/server layer
                                                                                             <------------------------------>
<------------------------------>                    <-------------------------------->

```