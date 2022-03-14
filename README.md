# Pod
### Serializing and Deserializing Plain Old Data

Pod allows easily describing the byte format of dataclasses with all the usual 
conveniences of working with native python objects. 

```rust
struct Message {
    upvotes: u8,
    message: String,
}
```

```python
from pod import pod, U8, Str

@pod
class Message:
    upvotes: U8
    message: Str

Message.to_bytes(Message(25, "Go Brazil for world cup!!"))
```