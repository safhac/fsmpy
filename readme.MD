#A simple async file processor
###an opinionated interpretation of the [_Elm Architecture_](https://guide.elm-lang.org/architecture/)
***
####the app has 4 states: listen, process, send and failure.

```
class Program:
    def main(init: init, update: update, subscriptions: subscriptions)
```

###init
#####the initial `(Model, Cmd)` tuple
#### `init: (Model, Cmd) = (Listen, None)
 

###Model
#####data structure representing the state
#### `Model = Failure | Listen | Process | Send`

            
###Update function
#####called when events occur (events that affect the state)
#### `def Update(model: Model, msg: Msg) -> (Model, Cmd):...`
#####arguments are the current state `Model` and a message `MSG`, returns a tuple of `(Model, Cmd)`


###Msg
#### `class Msg(enum):...`
#####a Union representing what messages we can send within our module


###subscriptions listener
#### ``
#####listen for input
