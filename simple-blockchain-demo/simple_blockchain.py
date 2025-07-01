
---

## simple-blockchain-demo/simple_blockchain.py

```python
import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

def create_genesis_block():
    return Block(0, time.time(), "Genesis Block", "0")

def main():
    blockchain = [create_genesis_block()]
    blockchain.append(Block(1, time.time(), "First block data", blockchain[-1].hash))
    blockchain.append(Block(2, time.time(), "Second block data", blockchain[-1].hash))

    for block in blockchain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}\n")

if __name__ == "__main__":
    main()
