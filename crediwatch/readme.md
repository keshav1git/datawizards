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

## Download your dependencies
    cd to root of the project repository 
    pip install -r requirements.txt

## How to run tests

    cd test
    python -m unittest test_analyse_credit_score.py

## How to run server

    python app.py
    visit http://127.0.0.1:5000/ to check swagger docs
``````